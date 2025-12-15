from dotenv import load_dotenv
load_dotenv()

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import ConfigDevelopment

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()   # - keys for managing user sessions

login_manager = LoginManager()  # - validation for user session 
login_manager.login_view = 'users.login'   # - login end point  @login_rquired will redirect to 'login' page
login_manager.login_message_category = 'info'      



def create_app(config_class=ConfigDevelopment):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app