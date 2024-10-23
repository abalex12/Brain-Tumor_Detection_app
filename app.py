from flask import Flask
from flask_login import LoginManager
from models import db, User
from route import configure_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tumor_app.db'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
app.config['JSON_AS_ASCII'] = False  


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

configure_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)