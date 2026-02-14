#include <iostream>
#include <array>
using namespace std;
// 希尔排序函数，对std::array<int, 10>进行排序
void shellSort(array<int, 10> &arr)
{
    int n = arr.size(); // 获取数组的长度
    int gap = n / 2;    // 初始gap设为数组长度的一半

    // 外层循环：控制gap的逐渐减小，直到gap为0
    while (gap > 0)
    {
        // 内层循环：对每个子数组进行插入排序
        for (int i = gap; i < n; ++i)
        {
            int temp = arr[i]; // 保存当前元素的值
            int j = i;         // 初始化j为当前元素的索引

            // 在子数组中找到temp的正确位置
            while (j >= gap && arr[j - gap] > temp)
            {
                arr[j] = arr[j - gap]; // 将较大的元素向右移动
                j -= gap;              // j向左移动gap个位置
            }

            arr[j] = temp; // 将temp放入正确的位置
        }

        gap /= 2; // 缩小gap为原来的一半
    }
}

// int main() {
//     // 初始化一个数组
//     std::array<int, 10> arr = {9, 5, 1, 3, 7, 2, 8, 4, 6, 0};

//     // 输出排序前的数组
//     std::cout << "排序前的数组: ";
//     for (int num : arr) {
//         std::cout << num << " ";
//     }
//     std::cout << std::endl;

//     // 调用希尔排序函数进行排序
//     shellSort(arr);

//     // 输出排序后的数组
//     std::cout << "排序后的数组: ";
//     for (int num : arr) {
//         std::cout << num << " ";
//     }
//     std::cout << std::endl;

//     return 0;
// }