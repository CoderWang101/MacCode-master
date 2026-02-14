def waiting_service(w):
    """
    参数:w (list): 每个客户的等待时间列表。
    """
    w_sorted = sorted(w)# 对等待时间进行排序（从小到大）
    n = len(w)# 获取客户数量
    sum_time = 0
    
    for i in range(n): # 计算总等待时间
        sum_time += w_sorted[i] * (n - i - 1) # 每个客户的等待时间会被后面 (n-i-1) 个客户等待

    return sum_time# 返回总等待时间

w = [30, 50, 100, 20, 120, 70]
result = waiting_service(w)
print(result)  # 输出结果