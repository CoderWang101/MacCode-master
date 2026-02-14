#include <iostream>
#include <vector>
#include <climits> // 用于 INT_MIN

using namespace std;

// 下沉调整（小根堆）
void sift_down(vector<int> &heap, size_t root, size_t end)
{
    size_t parent = root;
    while (true)
    {
        size_t child = 2 * parent + 1; // 左子节点索引
        if (child > end)
            break;

        // 选择较小的子节点（小根堆）
        if (child + 1 <= end && heap[child + 1] < heap[child])
            child++;

        // 若父节点 > 子节点，交换并继续下沉
        if (heap[parent] > heap[child])
        {
            swap(heap[parent], heap[child]);
            parent = child;
        }
        else
            break;
    }
}

// 删除堆顶元素
int delete_top(vector<int> &heap)
{
    if (heap.empty())
        return INT_MIN; // 堆为空时返回最小值（或抛出异常）

    // 交换堆顶与堆尾
    swap(heap[0], heap[heap.size() - 1]);

    // 删除堆尾元素（原堆顶）
    int top = heap.back();
    heap.pop_back();

    // 调整堆顶元素
    if (!heap.empty())
        sift_down(heap, 0, heap.size() - 1);

    return top;
}

int main()
{
    int n = 7; // 堆的大小
    vector<int> heap(7); // 初始小根堆
    int arr[] = {1, 3, 5, 7, 9, 11, 13};
    for (int i = 0; i < n; i++)
        heap[i] = arr[i];

    cout << "原始堆: ";
    for (int num : heap)
        cout << num << " ";
    cout << endl;

    int top = delete_top(heap);
    cout << "删除的堆顶元素: " << top << endl;

    cout << "调整后的堆: ";
    for (int num : heap)
        cout << num << " ";
    cout << endl;

    return 0;
}