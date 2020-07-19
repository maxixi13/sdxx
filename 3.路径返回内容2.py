import socket
import time

# 创建对象
sk = socket.socket()

# 绑定IP端口
sk.bind(('127.0.0.1', 8000))

# 监听
sk.listen()

def rihan(url):
    return "欢迎访问 日韩板块{}".format(url)

def oumei(url):
    return "欢迎访问 欧美板块{}".format(url)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 持续等待链接
while True:
    conn, addr = sk.accept()
    data = conn.recv(2048).decode("UTF-8")
    url = data.split()[1]
    print(url)
    # 头文件
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html;charset=utf-8\r\n\r\n')
    if url == "/rihan":
        ret = rihan(url)
    elif url == "/oumei":
        ret = oumei(url)
    elif url == "/":
        ret = "<h1>欢迎访问 首页</h1>"
    else:
        ret = "<h1>404 not found</h1>"

    conn.send(ret.encode('utf-8'))
    # 断开链接
    conn.close()
