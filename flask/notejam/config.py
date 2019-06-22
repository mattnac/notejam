import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'notejam-flask-secret-key'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notejam.db')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    sql_password = os.environ.get('SQL_PW')
    sql_host = os.environ.get('CLOUDSQL_HOST')
    sql_user = os.environ.get('SQL_USER')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + sql_user + ':' + sql_password + '@' + sql_host + '/notejam'


class TestingConfig(Config):
    TESTING = True
