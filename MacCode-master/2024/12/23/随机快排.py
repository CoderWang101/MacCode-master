import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # 随机选择一个枢轴元素
        pivot = random.choice(arr)
        # 将数组分区为小于、等于和大于枢轴的元素
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        # 递归排序小于和大于枢轴的元素，并组合结果
        return quicksort(less) + equal + quicksort(greater)

# 测试序列
arr = [5, 8, 2, 15, 32, 3]
sorted_arr = quicksort(arr)
print("排序后的序列:", sorted_arr)