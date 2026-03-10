# 自己抛出异常
def get_password():
    while True:
        password = input("请输入密码:")
        if len(password) >= 8:
            return password
        print("密码长度不足8位，请重新输入")


if __name__ == '__main__':
    try:
        pw = get_password()
    except Exception as e:
        print(e)
