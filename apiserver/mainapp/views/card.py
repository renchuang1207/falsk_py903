from flask import Blueprint
from flask import url_for

blue = Blueprint('cardBlue',__name__)

@blue.route('/add/<bankName>')
def addCard(bankName):
    return "%s 开户成功!"%bankName



# @blue.route('/select_bank')
# def selectBank():
#     #查询所有银行，供用户选择
#     #用户选择完以后，进入开户页面
#     bankName = "中国银行"
#     return """
#     选择银行成功，3秒后<a href="%s">进入开户页面</a>
#     """%("/card/add/"+bankName)


@blue.route('/select_bank')
def selectBank():
    #查询所有银行，供用户选择
    #用户选择完以后，进入开户页面
    bankName = "中国银行"
    next_url = "/card/add/"+bankName
    return """
    选择银行成功，3秒后<a href="%s">进入开户页面</a>
    """%url_for('cardBlue.addCard',bankName=bankName)