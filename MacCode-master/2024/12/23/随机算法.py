import random

def sherwood_quicksort(A, left, right):
    if left < right:
        pivot_index = random_partition(A, left, right)
        sherwood_quicksort(A, left, pivot_index - 1)
        sherwood_quicksort(A, pivot_index + 1, right)

def random_partition(A, left, right):
    ini_index = random.randint(left, right)
    A[left], A[ini_index] = A[ini_index], A[left]
    pivot = A[left]
    i = right + 1
    for j in range(right, left, -1):
        if A[j] > pivot:
            i -= 1
            A[i], A[j] = A[j], A[i]
    A[left], A[i - 1] = A[i - 1], A[left]
    return i - 1

while True:
    try:
        input_str = input("待排序: \n")
        if input_str.lower() == 'exit':
            break
        le = input_str.split()
        A = [int(t) for t in le]
        sherwood_quicksort(A, 0, len(A) - 1)
        print("\n")
        print("排序后： \n")
        for item in A:
            print(item, end=" ")
        print("\n")
    except ValueError:
        print("请输入有效的整数列表，或输入 'exit' 退出。\n")
        continue
    except KeyboardInterrupt:
        print("\n用户中断，程序退出。\n")
        break

