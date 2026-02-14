# def knapsack(weights, values, W):
#     n = len(weights)
#     dp = [[0] * (W + 1) for _ in range(n + 1)]#初始化
#     for i in range(1, n + 1):
#         for j in range(W + 1):
#             if j >= weights[i - 1]:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
#             else:
#                 dp[i][j] = dp[i - 1][j]
#     return dp[n][W]

# # 示例
# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 6]
# W = 8#背包容量
# print(knapsack(weights, values, W))

def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    # 回溯 dp 数组，找出选择的物品
    selected = []
    i, j = n, W
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected.append(i - 1)  # 物品索引从0开始
            j -= weights[i - 1]
        i -= 1
    selected.reverse()
    
    return dp[n][W], selected

# 示例
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 8
max_value, selected_items = knapsack(weights, values, W)
print("最大价值:", max_value)
print("选择的物品索引:", selected_items)
print("选择的物品权重:", [weights[i] for i in selected_items])
print("选择的物品价值:", [values[i] for i in selected_items])