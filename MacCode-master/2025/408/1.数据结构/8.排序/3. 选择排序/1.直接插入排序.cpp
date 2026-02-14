#include <iostream>
#include <assert.h>
//交换
void Swap(int* p1, int* p2)
{
	int tmp = *p1;
	*p1 = *p2;
	*p2 = tmp;
}

//教材上的选择排序
void SelectSort(int* a, int n)
{
	for (int i = 0; i < n - 1; i++)//一共进行n-1轮趟
	{
		int min = i;//每一轮的最小值
		for (int j = i + 1; j < n; j++)//找到最小值的下标
		{
			if (a[j] < a[min])		   //找到最小值
				min = j;
		}
		if (min != i)//交换
			Swap(&a[i], &a[min]);
	}
}


// //对比插入排序，还是插入排序更优
// void SelectSort(int* a, int n)
// {
// 	//遍历一遍选出最小and最大的，分别放在左右边
// 	int begin = 0, end = n - 1;
// 	int mini = begin, maxi = begin;
// 	while (begin<end)
// 	{
// 		for (int i = 0; i <= end; i++)
// 		{
// 			//选最小
// 			if (a[i] < a[mini])
// 				mini = i;
			
// 			//选最大
// 			if (a[i] > a[maxi])
// 				maxi = i;
// 		}
 
// 		Swap(&a[begin], &a[mini]);//交换元素
 
// 		if (begin == maxi)//如果begin和maxi重叠，那么需要修正位置
// 			maxi = mini;
 
// 		Swap(&a[end], &a[maxi]);//交换元素
// 		++begin;
// 		--end;
// 	}
// } 

