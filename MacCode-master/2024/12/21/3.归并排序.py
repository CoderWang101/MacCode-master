def merge_sort(Alist):
    if len(Alist) <= 1:
        return Alist
    #递归边界条件
    mid = len(Alist) // 2
    left = merge_sort(Alist[:mid])
    right = merge_sort(Alist[mid:])

    #归并操作:把连个有序子序列合并为一个大有序序列
    result = []
    i=j=0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #处理剩余元素,追加到result后
    if i==len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])

    return result        


result = merge_sort([2,6,10,3,8,4])
print(result)  # 输出结果