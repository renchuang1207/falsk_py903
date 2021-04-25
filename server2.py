from flask import Flask
from flask import request,render_template


#创建flask服务对象


app = Flask(__name__)

#声明请求资源(动态资源)
@app.route('/hi',methods = ['get','post'])
def hi():
    #使用request请求对象来获取请求方法
    platform = request.args.get('platform','pc')
    if platform.lower() != 'android':
        return """
            <h2>目前只支持Android设备</h2>
        """

    if request.method == 'GET':

        return """
        <h1>用户登录页面</h1>
        <form action="/hi?platform=android" method="post">
            <input name="name" placeholder="用户名"><br>
            <input name="pwd" placeholder="口令"><br>
            <button>提交</button>
        </form>
        """
    else:
        #获取表单的参数
        name = request.form.get('name')
        # print(name)
        pwd = request.form.get('pwd')
        # print(pwd)

        if name.strip() == 'disen' and pwd.strip() == '987':
            return """
                <h2 style="color:blue;">登录成功</h2>
             """
        else:
            return """
            <h2 style="color:orange;">登录失败，<a href="/hi?platform=android">重试</a></h2>
         """

@app.route('/bank',methods = ['get','post'])
def addBank():
    # 家在数据P(Model 交互操作)
    data = {'title':'绑定银行卡',
            'error_message':''
            }

    if request.method == "POST":
        #处理post请求
        #获取表单参数
        name = request.form.get("name",None)
        card_num = request.form.get("card_num",None)
        if all((name,card_num)):
            #使用flask中的日志记录器（名称为当前脚本名称）  [2021-04-17 23:06:15,495] INFO in server2: name:1111->card:1111
            app.logger.info('name:%s->card:%s'%(name,card_num))
            return """
            <h2>绑定银行卡成功</h2>
            <h4 id="result"></h4>
            <script>
                let steps = 5;
                let interval_id = 0;
                interval_id = setInterval(() => {
                    if(steps >= 0){
                        document.getElementById('result').innerText= steps--
                    }
                    else{
                        //取消定时器
                        clearInterval(interval_id);
                        window.open('/hi', target='_self')
                    }
                },1000)               
            </script>
            """
        data['error_message'] = '银行名称卡号不能为空'
    return render_template("bank_edit.html",**data)

    # 渲染模版

#阿里云镜像 https://mirrors.aliyun.com/pypi/simple
#启动服务
#注意事项：多进程和多线程不可以同时开启。只可以选择一种，如 processes=4同时threaded=True则会报错
app.run('',
        5000,
        debug=True, #默认未开启调试模式，True开启调试模式
        # threaded=True, #默认是单线程，即为False
        processes=1) #默认只有一个进程