def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 分割数组
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 递归排序左右子数组
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 合并两个有序数组
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 合并两个有序数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 将剩余部分加入结果数组
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 测试数据
arr = [2, 6, 10, 3, 8, 4]

# 归并排序
sorted_arr = merge_sort(arr)
print("排序后的数组:", sorted_arr)