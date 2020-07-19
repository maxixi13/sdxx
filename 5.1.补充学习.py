def ff():
    try:
        print("1")
        return "1.1"
    finally:
        print("0")
        # return "0.0"


print(ff())

# try-finally语句无论是否有异常都会进行执行，try如有异常会暂时保存 执行finally
