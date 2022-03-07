from distutils.debug import DEBUG
import os
from pickle import TRUE

class Config:

    pass


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production' : ProdConfig
}