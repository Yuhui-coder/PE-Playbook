import os
import sys


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig:
    SECRET_KEY = 'j\x1c\t\x01\x9b,3\x02\xea\xc4\x96d\xbbDEa\x99\xda\xc5\xc8D\xcb\xf3\xc2'

    # SQL_HOSTNAME = 'localhost'
    # SQL_DATABASE = 'wjgx'
    # SQL_USER = 'root'
    # SQL_PASS = 'root'
    #
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (SQL_USER, SQL_PASS, SQL_HOSTNAME, SQL_DATABASE)
    # SQLALCHEMY_MAX_OVERFLOW = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data.db')

    UPLOAD_PATH = os.path.join(basedir, "app", "static", "uploads")


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
