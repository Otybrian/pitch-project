import os


class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:user@localhost/mypitch'
    SECRET_KEY = '30011397'
    UPLOADED_PHOTOS_DEST = 'app/static/profiles'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME='otbrayo@gmail.com'
    MAIL_PASSWORD='Year2030#'
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}
