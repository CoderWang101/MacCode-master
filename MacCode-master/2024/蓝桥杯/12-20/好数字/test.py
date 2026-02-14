def good(x):
    i = 1
    while x > 0:
        if i % 2 == 1:
            if (x % 10) % 2 == 0:
                return 0
        else:
            if (x % 10) % 2 == 1:
                return 0
        x = x // 10
        i += 1
    return 1

def main():
    N = int(input())  # 读取用户输入的 N
    ans = 0  # 存储答案（“好数”个数）
    for i in range(1, N + 1):
        if good(i) == 1:
            ans += 1  # 满足“好数”，答案加 1
    print(ans)

# 调用主函数
if __name__ == "__main__":
    main()