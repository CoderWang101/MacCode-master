class SortingAlgorithms:
    def __init__(self, array):
        self.array = array.copy()
        self.original_array = array.copy()

    def reset_array(self):
        self.array = self.original_array.copy()

    def print_step(self, msg):
        print(f"{msg}: {self.array}")

#希尔排序
    def shell_sort(self):
        self.reset_array()
        n = len(self.array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j -= gap
                    self.print_step(f"希尔排序 (gap={gap}) 步骤 {i}")
                self.array[j] = temp
                self.print_step(f"希尔排序 (gap={gap}) 步骤 {i}")
            gap //= 2
#计数排序
    def counting_sort(self):
        self.reset_array()
        max_val = max(self.array)
        count = [0] * (max_val + 1)
        for num in self.array:
            count[num] += 1
            self.print_step(f"计数排序 步骤 {num}")
        sorted_array = []
        for i, cnt in enumerate(count):
            sorted_array.extend([i] * cnt)
            self.array = sorted_array.copy()
            self.print_step(f"计数排序 完成计数 {i}")
#桶排序
    def bucket_sort(self):
        self.reset_array()
        max_val = max(self.array)
        min_val = min(self.array)
        bucket_range = (max_val - min_val) // len(self.array) + 1
        buckets = [[] for _ in range(len(self.array))]
        for num in self.array:
            index = (num - min_val) // bucket_range
            buckets[index].append(num)
            self.print_step(f"桶排序 分配元素 {num} 到桶 {index}")
        sorted_array = []
        for i, bucket in enumerate(buckets):
            bucket.sort()
            sorted_array.extend(bucket)
            self.array = sorted_array.copy()
            self.print_step(f"桶排序 排序桶 {i} 并合并")
#基数排序
    def radix_sort(self):
        self.reset_array()
        max_val = max(self.array)
        exp = 1
        while max_val // exp > 0:
            self.array = self.counting_sort_by_digit(self.array, exp)
            exp *= 10
            self.print_step(f"基数排序 (exp={exp}) 步骤")
    def counting_sort_by_digit(self, array, exp):
        n = len(array)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (array[i] // exp) % 10
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            index = (array[i] // exp) % 10
            output[count[index] - 1] = array[i]
            count[index] -= 1
            self.print_step(f"基数排序 (exp={exp}) 处理元素 {array[i]}")
        return output
#堆排序
    def heap_sort(self):
        self.reset_array()
        n = len(self.array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
            self.print_step(f"堆排序 构建初始堆 步骤 {i}")
        for i in range(n - 1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)
            self.print_step(f"堆排序 堆排序结果 步骤 {i}")
    #小堆
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[left] > self.array[largest]:
            largest = left
        if right < n and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heapify(n, largest)
    #大堆
    # def heapify(self, n, i):
    #     largest = i
    #     left = 2 * i + 1
    #     right = 2 * i + 2
    #     if left < n and self.array[left] <self.array[largest]:
    #         largest = left
    #     if right < n and self.array[right] <self.array[largest]:
    #         largest = right
    #     if largest != i:
    #         self.array[i], self.array[largest] = self.array[largest], self.array[i]
    #         self.heapify(n, largest)
    
    
#快速排序
    def quick_sort(self, low, high):
        self.reset_array()
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
            self.print_step(f"快速排序 步骤 {low} 到 {high}")
    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.print_step(f"快速排序 分区 步骤 {j}")
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1
#选择排序
    def selection_sort(self):
        self.reset_array()
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.print_step(f"选择排序 步骤 {i}")
#直接插入排序
    def insertion_sort(self):
        self.reset_array()
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.print_step(f"直接插入排序 步骤 {i}")
            self.array[j + 1] = key
            self.print_step(f"直接插入排序 步骤 {i}")
#冒泡排序
    def bubble_sort(self):
        self.reset_array()
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.print_step(f"冒泡排序 步骤 {i}")
#归并排序
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1
                self.print_step(f"归并排序 合并步骤 {k}")

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1
                self.print_step(f"归并排序 合并步骤 {k}")

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1
                self.print_step(f"归并排序 合并步骤 {k}")

        self.array = array.copy()

    def test_all_sorts(self):
        sorts = [
            self.shell_sort,
            self.counting_sort,
            self.bucket_sort,
            self.radix_sort,
            self.heap_sort,
            lambda: self.quick_sort(0, len(self.array) - 1),
            self.selection_sort,
            self.insertion_sort,
            self.bubble_sort,
            lambda: self.merge_sort(self.array)
        ]
        for sort in sorts:
            self.reset_array()
            print(f"测试 {sort.__name__.replace('_', ' ')} 排序算法")
            sort()
            print(f"最终结果: {self.array}\n")

# 测试代码
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    sorter = SortingAlgorithms(array)
    sorter.test_all_sorts()