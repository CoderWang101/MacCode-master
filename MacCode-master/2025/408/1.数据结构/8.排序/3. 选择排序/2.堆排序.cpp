#include <iostream>
using namespace std;

void HeadAdjust(int *a, int s, int n)//向下调整
{
    int temp = a[s]; // 用temp保存当前父节点的值
    for (int i = 2*s + 1; i<n; i=2*i+1)
    {
        if (i+1<n && a[i]<a[i + 1])
            i++;//指向左右孩子中最大的
        if (temp >= a[i])
            break;
        a[s] = a[i]; // 将较大的子节点上移
        s = i;       // 将s指向当前子节点的位置
    }
    a[s] = temp; // 将temp放回正确的位置
}

void BuildMaxHeap(int *a, int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        HeadAdjust(a, i, n); // 从后往前调整所有非终端节点
}

// int main()
// {
//     int a[] = {1, 3, 2, 4, 5, 6};
//     int n = sizeof(a) / sizeof(a[0]);
//     BuildMaxHeap(a, n);
//     for(int i=0; i<n; i++)
//         cout << a[i] << " ";
//     cout << endl;
//     return 0;
// }

