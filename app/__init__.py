import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
import pymysql


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://testman:Jhayg3309]]:P@vultr-prod-85f8d360-5bbf-4d05-ad2d-01cc47768728-vultr-prod-995c.vultrdb.com:16751/sample_crud'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'pgenon53@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'yuvb yunz zbzn gjcp') 
mail = Mail(app)


# - keys for managing user sessions
login_manager = LoginManager(app)   # - validation for user session 
login_manager.login_view = 'login'   # - login end point  @login_rquired will redirect to 'login' page
login_manager.login_message_category = 'info'      

from app import routes