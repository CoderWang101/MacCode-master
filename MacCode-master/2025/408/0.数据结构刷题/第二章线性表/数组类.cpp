#include <iostream>
// using namespace std;
#define MAX_SIZE 10
typedef struct
{
    int length;
    int data[MAX_SIZE];
} sqlist;

// 删除指定元素
void delete_all_element(sqlist &L, int val)
{
    int len = L.length;
    if (len == 0)
        return; // 如果数组为空，直接返回
    int k = 0;
    for (int i = 0; i < len; i++)
    {
        if (L.data[i] != val)
        {
            L.data[k++] = L.data[i]; // 保留不等于val的元素
        }
    }
    L.length = k; // 更新数组长度
}

void delete_range_all_element(sqlist &L, int s, int t) // s<t
{
    int len = L.length;
    if (s >= t || s < 0 || t < 0 || s >= L.length || t >= L.length || len == 0)
        return; // 如果范围不合法，直接返回
    int range = t - s + 1;
    ++t;
    while (t < len) // 从t开始向前移动
    {
        L.data[s++] = L.data[t++];
    }
    L.length -= range; // 更新数组长度
}

void delete_repeat_element(sqlist &L)
{
    int len = L.length;
    if (len == 0)
        return; // 如果数组为空，直接返回

    int left = 0, right = 1;
    while (right < len)
    {
        if (L.data[left] == L.data[right])
            right++;
        else
            L.data[++left] = L.data[right++];
    }
    L.length = left + 1;
}
sqlist combine_list(const sqlist &L1, const sqlist &L2)
{
    sqlist L3;
    L3.length = L1.length + L2.length;

    int i = 0, j = 0, k = 0;
    while (i < L1.length && j < L2.length)
    {
        if (L1.data[i] < L2.data[j])
        {
            L3.data[k++] = L1.data[i++];
        }
        else
        {
            L3.data[k++] = L2.data[j++];
        }
    }
    // if(i+1==L1.length)
    // {
    //     while (j<L2.length)
    //     {
    //         L3.data[k++] = L2.data[j++];
    //     }
    // }
    // 直接用两个while 处理可能存在的剩余元素
    // 处理 L1 中剩余的元素
    while (i < L1.length)
    {
        L3.data[k++] = L1.data[i++];
    }

    // 处理 L2 中剩余的元素
    while (j < L2.length)
    {
        L3.data[k++] = L2.data[j++];
    }

    L3.length = k; // 更新新数组的长度
    return L3;
}

void reverse_1(sqlist &L, int i, int j, int arraysize)
{
    while (i < j && i < arraysize && j < arraysize)
    {
        int temp = L.data[i];
        L.data[i++] = L.data[j];
        L.data[j--] = temp;
    }
}
void exchange(sqlist &L, int i, int j, int arraysize)
{
    if (L.length == 0 || i < 0 || j < 0 || i >= arraysize || j >= arraysize)
        return; // 如果数组为空或索引越界，直接返回

    reverse_1(L, 0, i + j - 1, arraysize);
    reverse_1(L, 0, i - 1, arraysize);
    reverse_1(L, i, j - 1, arraysize);
}

void exchange_find_insert(sqlist &l, int val)
{
    int len = l.length;
    if (len == 0)
        return; // 如果数组为空，直接返回

    int left = 0, right = len - 1;
    int flag = 0;
    while (left <= right)
    {
        // int mid = (right + left) / 2;
        int mid = (right - left) / 2 + left;      // 防止溢出
        if (l.data[mid] == val && mid != len - 1) // 如果找到值且不是最后一个元素
        {
            // 交换
            int temp = l.data[len - 1];
            l.data[len - 1] = l.data[mid];
            l.data[mid] = temp;
            flag = 1; // 标记已找到并交换
        }
        else if (mid > val)
            left = mid + 1;
        else
            right = mid - 1;
    }
    // 如果没有找到值，插入
    if (flag == 0)
    {
        int x = len;
        // 向后移动元素
        while (l.data[x] > val)
        {
            l.data[x] = l.data[x - 1];
            --x;
        }
        l.data[x] = val; // 插入值
        l.length++;      // 更新数组长度
    }
}

#include <vector>
void hash_sum(int a[], int b[], int c[], int n)
{
    std::vector<int> hash(n);
    for (int i = 0; i < n; i++)
    {
        hash[a[i]]++;
        hash[b[i]]++;
        hash[c[i]]++;
    }
    for (int i = 0; i < n; i++)
    {
        if (hash[i] == 3)
        {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;
}
#include <iostream>
void find_common_elements(int A[], int B[], int C[], int n)
{
    int i = 0, j = 0, k = 0;
    while (i < n && j < n && k < n)
    {
        if (A[i] == B[j] && B[j] == C[k])
        {
            std::cout << A[i] << std::endl;
            i++;
            j++;
            k++;
        }
        else if (A[i] < B[j])
        {
            i++;
        }
        else if (B[j] < C[k])
        {
            j++;
        }
        else
        {
            k++;
        }
    }
}
// int main() {
//     int A[] = {1, 2, 3};
//     int B[] = {2, 3, 4};
//     int C[] = {-1, 0, 2};
//     int n = 3;
//     find_common_elements(A, B, C, n);
//     return 0;
// }

// 2010真题

void reverse_2(int R[], int l, int r)
{
    while (l < r)
    {
        int temp = R[l];
        R[l++] = R[r];
        R[r--] = temp;
    }
}
void cycle_move_arr(int R[], int n, int p)
{
    reverse_2(R, 0, p - 1);
    reverse_2(R, p, n - 1);
    reverse_2(R, 0, n - 1);
}

// 2011
// 查找两个有序数组的中位数
// 时间复杂度O(n)，空间复杂度O(1)
void find_mid(int a[], int b[], int n)
{
    int ap = 0, bp = 0;
    int mid = (2 * n - 1) / 2; // 中位数位置
    while (ap < n && bp < n)
    {
        if (a[ap] > b[bp])
            ++bp;
        else
            ++ap;
        --mid;
        if (mid <= 0)
        {
            if (a[ap] > b[bp])
                std::cout << b[bp] << std::endl;
            else
                std::cout << a[ap] << std::endl;
        }
    }
    while (ap < n && mid > 0)
    {
        --mid;
        ++ap;
        std::cout << a[ap] << std::endl;
    }
    while (bp < n && mid > 0)
    {
        --mid;
        ++bp;
        std::cout << b[bp] << std::endl;
    }
}
// 二分法
//  时间复杂度O(logn)，空间复杂度O(1)
int findMedianOptimized(int A[], int B[], int n)
{
    int low = 0, high = n;

    while (low <= high)
    {
        int i = (low + high) / 2; // A的分区点
        int j = n - i;            // B的分区点

        // 处理边界情况
        int A_left = (i == 0) ? INT_MIN : A[i - 1];
        int A_right = (i == n) ? INT_MAX : A[i];
        int B_left = (j == 0) ? INT_MIN : B[j - 1];
        int B_right = (j == n) ? INT_MAX : B[j];

        if (A_left <= B_right && B_left <= A_right)
        {
            // 找到正确分区
            return std::max(A_left, B_left);
        }
        // A左部过大，左移分区点
        else if (A_left > B_right)
            high = i - 1;
        // A左部过小，右移分区点
        else
            low = i + 1;
    }
    return -1; // 理论上不会执行
}

// 2013
// O(n)	O(n)
#include <iostream>
#include <vector>
int find_main_element(int a[], int n)
{
    // int mid = n / 2;
    // std::vector<int> hash(n, 0);
    // for (int i = 0; i < n; ++i)
    //     hash[a[i]]++;
    // for (int i = 0; i < n; i++)
    //     if (hash[i] > mid)
    //         return i;
    // return -1; // 如果没有主元素，返回-1

    // 使用数组代替vector
    int mid = n / 2;
    int *hash = new int[n](); // 动态分配内存并初始化为0
    for (int i = 0; i < n; ++i)
        hash[a[i]]++; // 统计每个元素的出现次数

    for (int i = 0; i < n; ++i)
    {
        if (hash[i] > mid)
        {
            delete[] hash; // 释放内存
            return i;
        }
    }
    delete[] hash; // 释放内存
    return -1;     // 没有主元素
}
// 最优算法（摩尔投票法 + 验证）//O(n)	O(1)
int findMainElement(int a[], int n)
{
    // 摩尔投票阶段
    int candidate = -1; // 候选主元素
    int count = 0;      // 计数器

    for (int i = 0; i < n; ++i)
    {
        if (count == 0)
        {
            // 计数器归零时更新候选元素
            candidate = a[i];
            count = 1;
        }
        else
        {
            // 相同元素计数增加，不同元素计数减少
            count += (a[i] == candidate) ? 1 : -1;
        }
    }

    // 验证阶段
    int actualCount = 0;
    for (int i = 0; i < n; ++i)
    {
        if (a[i] == candidate)
            actualCount++;
    }
    // 判断是否满足主元素条件
    return (actualCount > n / 2) ? candidate : -1;
}
int find(int a[], int n)
{
    int candiate = -1;
    int count = 0;

    for (int i = 0; i < n; ++i)
    {
        if (count == 0)
        {
            candiate = a[i];
            count = 1;
        }
        else
        {
            if (candiate == a[i])
                ++count;
            else
                --count;
        }
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        if (candiate == a[i])
            ++sum;
    }
    return (sum > n / 2) ? candiate : -1;
}

// 2018
int find_min_null_val(int a[], int n)
{
    // 找最大元素扩
    int max_val = 0;
    for (int i = 0; i < n; i++)
        max_val = (max_val > a[i]) ? max_val : a[i];

    int *hash = new int[max_val + 1]();
    for (int i = 0; i < n; i++)
    {
        if (a[i] > 0)
            ++hash[a[i]];
    }
    for (int i = 1; i <= max_val; i++)
    {
        if (hash[i] == 0)
            return i;
    }
    return n + 1;
}
// 原地哈希，O(n) O(1)
// 将数组中小于等于0或大于n的元素设为n+1
int findMissingMinPositive(int a[], int n)
{
    // 1. 处理特殊情况：空数组
    if (n == 0)
        return 1;

    // 2. 将无效值设为 n+1
    for (int i = 0; i < n; i++)
        if (a[i] <= 0 || a[i] > n)
            a[i] = n + 1;

    // 3. 使用负号标记出现过的数
    for (int i = 0; i < n; i++)
    {
        int num = abs(a[i]); // 获取绝对值
        if (num <= n)
            // 只处理[1, n]范围内的数
            // 确保标记为负（避免重复标记）
            if (a[num - 1] > 0)
                a[num - 1] = -a[num - 1];
    }

    // 4. 找到第一个正数位置
    for (int i = 0; i < n; i++)
        if (a[i] > 0)
            return i + 1;
    // 5. 所有[1,n]都存在时返回n+1
    return n + 1;
}

// 2020//心得:多数组访问,尽量安排在同一循环中,使得仍然是O(n)
#define INT_MAX 0x7fffffff

int abs_(int a)
{
    if (a >= 0)
        return a;
    else
        return -a;
}
bool min_val(int x, int y, int z)
{
    if (x <= y && x <= z)
        return true;
    else
        return false;
}
int min_distance(int a[], int n, int b[], int m, int c[], int p)
{
    int d_min = INT_MAX;
    int i = 0, j = 0, k = 0, D;

    while (i < n && j < m && k < p)
    {
        D=abs_(a[i]-b[i])+abs_(b[i]-c[i])+abs_(c[i]-a[i]);
        if(D<d_min)
            d_min=D;

        if(min_val(a[i],b[i],c[i]))
            ++i;
        else if(min_val(b[i],a[i],c[i]))
            ++j;
        else
            ++k;
    }
    return d_min;
}