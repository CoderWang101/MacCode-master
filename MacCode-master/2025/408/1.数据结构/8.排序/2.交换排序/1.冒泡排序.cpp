#include <iostream>
#include <assert.h>
#include <algorithm>
using namespace std;

//交换
void Swap(int* p1, int* p2)
{
	int tmp = *p1;
	*p1 = *p2;
	*p2 = tmp;
}

//冒泡排序  时间复杂度O(N^2),最坏情况还为O(N^2)
//对比插入排序哪个更好？--接近有序或局部有序时，插入排序能更好适应
void Bubblesort(int* a, int n)
{
	assert(a);
 
	for (int j = 0; j < n; j++)
	{
		int exchange = 0;
		for (int i = 0; i < n - j; i++)
		{
			if (a[i - 1] > a[i])
			{
				// Swap(&a[i - 1], &a[i]);//自实现交换函数
                swap(a[i - 1], a[i]);//使用STL库函数
				exchange = 1;
			}
		}
		if (exchange == 0)
			break;
	}
}