#配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'demo'
USERNAME = 'root'
PASSWORD = 'xxxxxxxx'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8' .format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "123456"

#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "xxxxxxxxxx@qq.com"
MAIL_PASSWORD = "xxxxxxxxxxx"
MAIL_DEFAULT_SENDER = "xxxxxxxxx@qq.com"