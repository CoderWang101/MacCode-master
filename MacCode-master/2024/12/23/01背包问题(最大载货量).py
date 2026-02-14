def select_containers_dp(weights, c):
    n = len(weights)
    dp = [[0] * (c + 1) for _ in range(n + 1)]
    # 记录选择的物品
    selected = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):    # 填充 dp 表
        for w in range(c + 1):
            if weights[i - 1] <= w:
                if dp[i - 1][w - weights[i - 1]] + 1 > dp[i - 1][w]: # 选择第 i 个物品
                    dp[i][w] = dp[i - 1][w - weights[i - 1]] + 1
                    selected[i].append(i)  # 记录选择的物品
                else:
                    dp[i][w] = dp[i - 1][w]
            else:
                # 不选择第 i 个物品
                dp[i][w] = dp[i - 1][w]
    # 回溯找出选择的物品编号
    result = []
    i, w = n, c
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            result.append(i)
            w -= weights[i - 1]
        i -= 1
    return result[::-1]  # 返回选择的物品编号
weights = [10, 4, 2, 5, 7]
c = 15
selected_items = select_containers_dp(weights, c)
print("Selected items:", selected_items)
