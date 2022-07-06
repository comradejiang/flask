# 从python的flask包中获取flask
from flask import Flask

# 从exts里获取db
from exts import db,mail

# 导入配置
import config

# 从蓝图中获取qa和user
from blueprints.qa import bp as qa_bp
from blueprints.user import bp as user_bp


app = Flask(__name__)

# 配置项来自config.py文件中
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)



# 注册qa和user
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run()
