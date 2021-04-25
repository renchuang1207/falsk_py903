from flask import Blueprint

#创建蓝图时：第一个参数：name。可以任意命名
# 第二个参数：必须使用__name__表示导包的名称
blue = Blueprint('userBlue',__name__)


#声明的API接口
@blue.route('/find', methods=['GET'])
def find():
    return "<h2>hi,user-Blueprint</h2>"