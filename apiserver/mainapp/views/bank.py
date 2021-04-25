from flask import request, Blueprint, jsonify
from dao import student_dao

blue = Blueprint('bankblue',__name__)

@blue.route('/finds',methods=['GET','POST'])
def bank():
    dao = student_dao.StudentDao()
    data = dao.find_all() #[{},{}....]
    return jsonify({
        'status':200,
        'message':'find all ok',
        'data':data
    })

@blue.route('/edit/<int:bankId>',methods=['GET'])
def edit(bankId):
    return "正在编辑：银行编号%s"%bankId


@blue.route('del/<int:bank_id>',methods=['GET'])
def delbank(bank_id):
    return "正在删除：银行编号%s" % bank_id



@blue.route('/find/<keyword>/')
def find(keyword):
    #keyword有可能是银行的id，名称，地址
    return "keyword是string类型，值是%s"%(keyword)



@blue.route('/forward/<path:url>',methods=['GET'])
def forward(url):
    return """
        <div id="result"></div>
        <script>
            let steps = 5;
            let id = setInterval(()=>{
                if (steps > 1){
                    document.getElementById("result").innerText="剩余" + (--steps) + "秒";  
                }
                else{
                    open("%s",target="_self")
                }
            }
            ,1000)
        </script>
    """%url



@blue.route('/delbank',methods=['GET'])
def del_bank():
    bank_id = request.args.get('id')
    return "<h3>正在删除：%s</h3>"%bank_id