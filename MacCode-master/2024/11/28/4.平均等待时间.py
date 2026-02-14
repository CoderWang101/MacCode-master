def min_average_wait_time(service_times):
    # 对服务时间进行排序
    sorted_times = sorted(service_times)
    
    # 计算总等待时间
    total_wait_time = 0
    current_wait_time = 0
    
    for time in sorted_times:
        total_wait_time += current_wait_time
        current_wait_time += time
    
    # 计算平均等待时间
    average_wait_time = total_wait_time / len(service_times)
    
    return total_wait_time, average_wait_time

# 测试数据
service_times = [30, 50, 100, 20, 120, 70]

# 计算平均等待时间
total_wait_time, average_wait_time = min_average_wait_time(service_times)
print(f"总等待时间: {total_wait_time}")
print(f"平均等待时间: {average_wait_time}")