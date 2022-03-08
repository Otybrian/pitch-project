import os


class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:user@localhost/pitches'
    SECRET_KEY = '30011397'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}