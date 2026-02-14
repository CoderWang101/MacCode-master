#include<iostream>
#include<assert.h>
using namespace std;

#define n 100

void Merge(int* a, int* tmp, int left, int mid, int right)
{
    int i = left, j = mid + 1, k = left;
    //
    while (i <= mid && j <= right)
    {
        if (a[i] < a[j])
            tmp[k++] = a[i++];
        else
            tmp[k++] = a[j++];
    }
    while (i <= mid)
        tmp[k++] = a[i++];
    while (j <= right)
        tmp[k++] = a[j++];
    for (int i = left; i <= right; i++)
        a[i] = tmp[i];
}

void MergeSort(int* a, int* tmp, int left, int right)
{
    if (left < right)
    {
        int mid = (left + right) / 2;
        MergeSort(a, tmp, left, mid);
        MergeSort(a, tmp, mid + 1, right);
        Merge(a, tmp, left, mid, right);
    }
}

int main()
{
    int a[n] = { 0 };
    int tmp[n] = { 0 };//辅助数组
    for (int i = 0; i < n; i++)
        a[i] = n - i;
    MergeSort(a, tmp, 0, n - 1);
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    cout << endl;
    return 0;
}
