#include <iostream>
#include <vector>
using namespace std;

/**
 * 二分查找的迭代实现
 * @param arr 有序数组
 * @param target 目标值
 * @return 目标值在数组中的索引，如果不存在则返回 -1
 */
int binarySearch(const vector<int> &arr, int target)
{
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high)
    {
        // 计算中间索引，避免整数溢出
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            // 目标值在右半部分
            low = mid + 1;  //缩小查找范围
        else
            // 目标值在左半部分
            high = mid - 1; //缩小查找范围
    }
    // 目标值不存在于数组中
    return -1;
}

// int main()
// {
//     vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15};
//     int target = 7;
//     int result = binarySearch(arr, target);
//     if (result != -1)
//         cout << "目标值 " << target << " 在数组中的索引为 " << result << endl;
//     else
//         cout << "目标值 " << target << " 不在数组中" << endl;

//     return 0;
// }