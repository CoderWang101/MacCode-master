#include <vector>
#include <cmath>     // 用于计算平方根
#include <algorithm> // 用于std::lower_bound

using namespace std;

/**
 * 分块查找函数
 * @param arr 有序数组
 * @param target 目标值
 * @return 目标值在数组中的索引，如果不存在则返回 -1
 */
int blockSearch(const vector<int> &arr, int target)
{
    int n = arr.size(); // 数组的大小
    if (n == 0)
        return -1; // 空数组，直接返回-1

    int blockSize = sqrt(n); // 计算块的大小，通常取平方根
    int low = 0;
    int high = n - 1;
    int currentBlock = 0; // 当前所在的块

    // 块间二分查找
    while (low <= high)
    {
        int mid = low + (high - low) / 2; // 计算中间索引

        if (arr[mid] < target)
            low = mid + 1;
        else if (arr[mid] > target)
            high = mid - 1;
        else
            return mid; // 目标值正好在中间，直接返回
    }

    //low>high跳出循环,但low所指并未查找,需要在块内查找
    // 块内顺序查找
    int start = currentBlock * blockSize;                     // 当前块的起始索引
    int end = min((currentBlock + 1) * blockSize - 1, n - 1); // 当前块的结束索引

    for (int i = start; i <= end; ++i)
        if (arr[i] == target)
            return i; // 找到目标值，返回索引

    return -1; // 目标值不在数组中
}

// int main()
// {
//     vector<int> arr = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
//     int target = 12;

//     int result = blockSearch(arr, target);

//     if (result != -1)
//     {
//         cout << "目标值 " << target << " 在数组中的索引为 " << result << endl;
//     }
//     else
//     {
//         cout << "目标值 " << target << " 不在数组中" << endl;
//     }

//     return 0;
// }