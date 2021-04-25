from wsgiref.simple_server import make_server

def app(env,make_response):
    "处理业务的核心函数"
    """
    请求路径：PATH_INFO
    请求方法：REQUEST_METHOD
    请求查询参数：QUERY_STRING
    客户端地址：REMOTE_ADDR
    请求上传的数据类型：CONTENT_TYPE
    客户端的代理（浏览器）：HTTP_USER_AGENT
    读取请求上传的字节数据对象：wsgi.input
    wsgi是否使用了多线程：wsgi.multithread : True
    wsgi是否使用了多进程：wsgi.multiprocess : False
    

    """
    for k,v in env.items():
        print(k,":",v)


    #生成响应头信息
    make_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
    return ['<h3>Hi,WSGI</h3>'.encode('utf-8')]




if __name__ == '__main__':
    #生册web服务器应用进程
    httpd = make_server('',8090,app)
    print("running")
    httpd.serve_forever()
