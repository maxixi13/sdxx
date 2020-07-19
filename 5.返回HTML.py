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


def guochan(url):
    return "欢迎访问 国产板块{}".format(url)


def shouye(url):
    # with as 无论错误与否执行完成之后都会杀掉内存
    with open("home.html","r",encoding="utf-8") as f:
        ret = f.read()
        return ret


list1 = [
    ("/rihan", rihan),
    ("/oumei", oumei),
    ("/guochan", guochan),
    ("/", shouye),
]

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 持续等待链接

while True:
    conn, addr = sk.accept()
    data = conn.recv(2048).decode("UTF-8")
    url = data.split()[1]
    print(url)
    # 头文件
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html;charset=utf-8\r\n\r\n')

    func = None

    for i in list1:
        if url == i[0]:
            func = i[1]
            break
    if func:
        # 路径匹配上
        ret = func(url)
    else:
        ret = "404 not found"

    conn.send(ret.encode('utf-8'))
    # 断开链接
    conn.close()
