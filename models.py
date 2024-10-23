from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Relationship with Patient model
    patients = db.relationship('Patient', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tumor_type = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    recommended_medication = db.Column(db.String(120))
    duration = db.Column(db.String(50))
    side_effects = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'tumor_type': self.tumor_type,
            'description': self.description,
            'recommended_medication': self.recommended_medication,
            'duration': self.duration,
            'side_effects': self.side_effects,
        }

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    tumor_type = db.Column(db.String(80), nullable=True)  # Updated to store predicted tumor type
    diagnosis_date = db.Column(db.Date, nullable=False)
    image_path = db.Column(db.String(200), nullable=True)  # Column to store the image file path
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to User model
    # treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'), nullable=True)  # Link to Treatment model
