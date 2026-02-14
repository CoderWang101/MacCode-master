//直接插入排序
// 一个数依次向前比较一个元素，被比较的元素后移，直到找到合适的位置插入
void InsertSort(int* a, int n)
{
	for (int i = 0; i < n - 1; i++)
	{
		// [0,end]有序，吧end+1 位置的值插入，保持有序
		int end = i;
		int tmp = a[end + 1];
		while (end >= 0)
		{
			if (tmp < a[end])//要交换的数字更大
			{
				//指针指向元素后移，end指针前移
				a[end + 1] = a[end];
				--end;
			}
			else
				//要交换的数字更小,退出循环
				break;
		}
		//开始交换
		a[end + 1] = tmp;
	}
}



