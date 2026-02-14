def minimum_cost(cost):
    # 按价格从高到低排序
    cost.sort(reverse=True)
    
    total_cost = 0
    n = len(cost)
    
    # 每次购买两粒糖果，免费送一粒糖果
    for i in range(0, n, 3):
        total_cost += sum(cost[i:i+2])
    
    return total_cost

# 示例测试
cost1 = [1, 2, 3]
cost2 = [2, 6, 5, 7, 2, 9]
cost3 = [5, 5]

print("cost=[1, 2, 3] 的最小开销:", minimum_cost(cost1))
print("cost=[2, 6, 5, 7, 2, 9] 的最小开销:", minimum_cost(cost2))
print("cost=[5, 5] 的最小开销:", minimum_cost(cost3))