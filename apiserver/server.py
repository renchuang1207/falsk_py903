from mainapp import app
from flask_script import Manager
from mainapp.views import bank, card
from mainapp.views import user
from flask_cors import CORS

if __name__ == '__main__':
    CORS().init_app(app)
    #讲蓝图对象注册到flask服务中
    app.register_blueprint(bank.blue,url_prefix='/bank')
    #url_prefix设置蓝图中子路由的前缀
    app.register_blueprint(user.blue,url_prefix='/user')
    app.register_blueprint(card.blue,url_prefix='/card')
    #以脚本的方式启动flask的应用服务
    #python server.py -h 0.0.0.0 runserver -p 6000 -d     (-d开启debug模式运行，-p端口号，-h启动主机)
    manger = Manager(app)
    manger.run()