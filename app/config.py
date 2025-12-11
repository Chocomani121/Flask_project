import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Production Configuration (Uses environment variables)
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', '')

    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', '')


# Development Configuration (Hardcoded - for local development only)
class ConfigDevelopment:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://testman:Jhayg3309]]:P@vultr-prod-85f8d360-5bbf-4d05-ad2d-01cc47768728-vultr-prod-995c.vultrdb.com:16751/sample_crud'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pgenon53@gmail.com'
    MAIL_PASSWORD = 'yuvb yunz zbzn gjcp'


# Documentation Example
class ConfigExample:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://testman:password@vultr-host.vultrdb.com:16751/sample_crud'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pgenon53@gmail.com'
    MAIL_PASSWORD = 'app_password_here'
