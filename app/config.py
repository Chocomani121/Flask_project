import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "True") == "True"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")


class ConfigDevelopment(Config):
    # """Uses the same env vars, but allows debug mode"""
    DEBUG = True


class ConfigExample:
    # """Documentation only — never used"""
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host:port/db"
