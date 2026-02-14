def max_path_sum(triangle):
    # 获取三角形的行数
    n = len(triangle)
    
    # 创建一个二维数组来存储每个位置的最大路径和
    dp = [[0] * (i + 1) for i in range(n)]
    
    # 初始化三角形顶层
    dp[0][0] = triangle[0][0]
    
    # 从第二行开始，逐行计算最大路径和
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                # 最左边的元素只能从上一行的最左边元素下来
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                # 最右边的元素只能从上一行的最右边元素下来
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                # 中间的元素可以从上一行的左边或右边元素下来
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    # 返回最后一行的最大值，即最大路径和
    return max(dp[n-1])

# 示例三角形
triangle = [
    [3],
    [7, 8],
    [8, 1, 0],
    [2, 7, 7, 4],
    [5, 5, 2, 6, 3]
]

# 计算并输出最大路径和
print("最大路径和为:", max_path_sum(triangle))