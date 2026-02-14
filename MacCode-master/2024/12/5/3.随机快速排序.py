import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # 随机选择枢轴元素
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 示例无序序列
arr = [5, 8, 2, 15, 32, 3]

# 运行排序并输出结果
sorted_arr = quicksort(arr)
print("排序后的数组:", sorted_arr)