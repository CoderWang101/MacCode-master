import random

def partition(arr, left, right, pivot_index):
    """
    将数组分为两部分：小于基准的元素在左边，大于基准的元素在右边。
    :param arr: 输入数组
    :param left: 子数组的左边界
    :param right: 子数组的右边界
    :param pivot_index: 基准元素的索引
    :return: 基准元素的最终位置
    """
    pivot_value = arr[pivot_index]
    # 将基准元素放到数组的最后
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # 分区操作，将小于基准的元素放到左边
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # 将基准元素放到正确的位置
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

def quickselect(arr, left, right, k):
    """
    快速选择算法，查找数组中第k小的元素。
    :param arr: 输入数组
    :param left: 子数组的左边界
    :param right: 子数组的右边界
    :param k: 要找的第k小的元素（k从1开始）
    :return: 第k小的元素
    """
    # 如果子数组只有一个元素，直接返回
    if left == right:
        return arr[left]

    # 随机选择一个基准元素
    pivot_index = random.randint(left, right)

    # 对数组进行分区，返回基准元素的最终位置
    pivot_index = partition(arr, left, right, pivot_index)

    # 根据基准元素的位置，决定下一步操作
    if k - 1 == pivot_index:  # 如果基准元素就是要找的第k小的元素
        return arr[pivot_index]
    elif k - 1 < pivot_index:  # 如果第k小的元素在左半部分
        return quickselect(arr, left, pivot_index - 1, k)
    else:  # 如果第k小的元素在右半部分
        return quickselect(arr, pivot_index + 1, right, k)

def find_kth_smallest(arr, k):
    """
    查找数组中第k小的元素。
    :param arr: 输入数组
    :param k: 要找的第k小的元素（k从1开始）
    :return: 第k小的元素
    """
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")
    return quickselect(arr, 0, len(arr) - 1, k)

# 测试用例
def test_find_kth_smallest():
    # 测试用例1：正常情况
    arr1 = [3, 2, 1, 5, 4]
    k1 = 3
    result1 = find_kth_smallest(arr1, k1)
    assert result1 == 3, f"Test Case 1 Failed: Expected 3, got {result1}"

    # 测试用例2：边界情况，k=1
    arr2 = [3, 2, 1, 5, 4]
    k2 = 1
    result2 = find_kth_smallest(arr2, k2)
    assert result2 == 1, f"Test Case 2 Failed: Expected 1, got {result2}"

    # 测试用例3：边界情况，k=5
    arr3 = [3, 2, 1, 5, 4]
    k3 = 5
    result3 = find_kth_smallest(arr3, k3)
    assert result3 == 5, f"Test Case 3 Failed: Expected 5, got {result3}"

    # 测试用例4：重复元素
    arr4 = [3, 2, 3, 5, 4]
    k4 = 3
    result4 = find_kth_smallest(arr4, k4)
    assert result4 == 3, f"Test Case 4 Failed: Expected 3, got {result4}"

    # 测试用例5：空数组
    arr5 = []
    try:
        find_kth_smallest(arr5, 1)
    except ValueError:
        print("Test Case 5 Passed: Caught ValueError for empty array.")
    else:
        print("Test Case 5 Failed: Expected ValueError for empty array.")

    print("All test cases passed!")

# 运行测试用例
test_find_kth_smallest()