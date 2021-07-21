import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '_N3Xt+GeN3RaT10n')
    DEBUG = False


class LocalConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'flask+mongoengine=<3'


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'flask+mongoengine=<3'
    # BASE_URL = "http://127.0.0.1:5000"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '#Test123'


config_by_name = dict(
    LOCAL=LocalConfig,
    DEV=DevelopmentConfig,
    PROD=ProductionConfig
)

key = Config.SECRET_KEY
