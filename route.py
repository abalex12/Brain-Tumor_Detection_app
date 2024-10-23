from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os
from datetime import datetime

from models import User, Treatment,Patient
from operations import add_user, get_user_by_username, add_treatment, get_treatment_by_tumor_type,add_patient
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import jsonify
import traceback

model = load_model('model/brains.h5')

def configure_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            user = get_user_by_username(request.form['username'])
            if user and user.check_password(request.form['password']):
                login_user(user)
                return redirect(url_for('dashboard'))
            flash('Invalid username or password')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('home'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            user = add_user(request.form['username'], request.form['email'], request.form['password'])
            if user:
                flash('Registration successful. Please login.')
                return redirect(url_for('login'))
            flash('Username or email already exists')
        return render_template('register.html')

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    

    @app.route('/predict', methods=['GET', 'POST'])
    @login_required
    def predict():
        if request.method == 'POST':
            try:
                # File handling
                if 'file' not in request.files:
                    return jsonify({'error': 'No file part'}), 400
                file = request.files['file']
                if file.filename == '':
                    return jsonify({'error': 'No selected file'}), 400
                
                if file:
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)
                    
                    # Process the image and get the prediction
                    try:
                        prediction, confidence = predict_image(filepath)
                    except Exception as e:
                        app.logger.error(f"Error in predict_image: {str(e)}")
                        return jsonify({'error': 'Error during image prediction'}), 500
                    
                    # Get treatment by tumor type
                    treatment_instance = get_treatment_by_tumor_type(prediction)

                    # Ensure treatment_instance is serializable
                    treatment_data = treatment_instance.to_dict() if treatment_instance else None

                    # Save patient data
                    try:
                        name = request.form['name']
                        age = request.form['age']
                        gender = request.form['gender']
                        diagnosis_date_str = request.form['diagnosis_date']
                        diagnosis_date = datetime.strptime(diagnosis_date_str, '%Y-%m-%d').date()
                        user_id = current_user.id
                        
                        add_patient(name, age, gender, prediction, diagnosis_date, filepath, user_id)
                    except Exception as e:
                        app.logger.error(f"Error in add_patient: {str(e)}")
                        return jsonify({'error': 'Error saving patient data'}), 500

                    return jsonify({
                        'prediction': prediction,
                        'confidence': confidence,
                        'treatment': treatment_data  # Return serialized treatment data
                    })
            except Exception as e:
                app.logger.error(f"Unexpected error: {str(e)}")
                return jsonify({'error': 'An unexpected error occurred'}), 500
        
        return render_template('predict.html')

     

    
    @app.route('/patients')
    @login_required
    def patients_list():
        patients = Patient.query.all()
        
        return render_template('patients.html', patients=patients)
    @app.route('/about')
    def about():
        return render_template("about.html")



def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))  # Resizing to the model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize the image data
    return img_array

def predict_image(img_path):
    # Preprocess the image
    preprocessed_img = preprocess_image(img_path)

    # Run the prediction
    prediction = model.predict(preprocessed_img)

    # Get the class index with the highest probability and its confidence score
    predicted_class = np.argmax(prediction, axis=1)[0]
    categories = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]
    predicted_category = categories[predicted_class]
    confidence_score = round(np.max(prediction) * 100, 2)
    return predicted_category,confidence_score

