from models import db, User, Treatment,Patient

def add_user(username, email, password):
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return None
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def add_treatment(tumor_type, description, recommended_medication, duration, side_effects):
    new_treatment = Treatment(
        tumor_type=tumor_type,
        description=description,
        recommended_medication=recommended_medication,
        duration=duration,
        side_effects=side_effects
    )
    db.session.add(new_treatment)
    db.session.commit()
    return new_treatment

def get_treatment_by_tumor_type(tumor_type):
    return Treatment.query.filter_by(tumor_type=tumor_type).first()

def add_patient(name,age,gender,prediction,diagnosis_date,filepath,user_id):
    new_patient = Patient(
        name=name,
        age=age,
        gender=gender,
        tumor_type=prediction, 
        diagnosis_date=diagnosis_date,
        image_path=filepath,
        user_id=user_id
        )

    db.session.add(new_patient)
    db.session.commit()
    return new_patient
