import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    
    DEBUG = True



Config_options = {
    'development':DevConfig,
    'production':ProdConfig
}