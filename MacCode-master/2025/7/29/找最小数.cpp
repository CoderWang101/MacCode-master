#include <iostream>
using namespace std;

struct Array {
    int length;
    int data[10];
};

int find_min_num(Array &a)
{
    if(a.length == 0) 
    {
        return -1; // 返回一个特殊值表示数组为空
    }

    int min_num = 0; // 初始化为第一个元素的索引
    for (int i = 0; i < a.length; i++)
    {
        if(a.data[i] < a.data[min_num])
        {
            min_num = i;
        }
    }
    // 交换最小值和最后一个元素
    int temp = a.data[min_num];
    a.data[min_num] = a.data[a.length - 1];
    a.data[a.length - 1] = temp;
    a.length--; // 减少数组长度

    return temp;
}

int main() {
    // 测试用例1: 正常情况
    Array arr1;
    arr1.length = 5;
    arr1.data[0] = 5; arr1.data[1] = 3; arr1.data[2] = 8; arr1.data[3] = 1; arr1.data[4] = 2;
    cout << "测试用例1: 原数组: ";
    for(int i=0; i<arr1.length; i++) cout << arr1.data[i] << " ";
    cout << endl;
    int min1 = find_min_num(arr1);
    cout << "最小值: " << min1 << endl;
    cout << "数组变为: ";
    for(int i=0; i<arr1.length; i++) cout << arr1.data[i] << " ";
    cout << endl << endl;

    // 测试用例2: 数组为空
    Array arr2;
    arr2.length = 0;
    cout << "测试用例2: 原数组为空" << endl;
    int min2 = find_min_num(arr2);
    cout << "返回值: " << min2 << endl << endl;

    // 测试用例3: 数组只有一个元素
    Array arr3;
    arr3.length = 1;
    arr3.data[0] = 1;
    cout << "测试用例3: 原数组: ";
    for(int i=0; i<arr3.length; i++) cout << arr3.data[i] << " ";
    cout << endl;
    int min3 = find_min_num(arr3);
    cout << "最小值: " << min3 << endl;
    cout << "数组变为: ";
    for(int i=0; i<arr3.length; i++) cout << arr3.data[i] << " ";
    cout << endl << endl;

    // 测试用例4: 最小值在中间
    Array arr4;
    arr4.length = 5;
    arr4.data[0] = 4; arr4.data[1] = 2; arr4.data[2] = 5; arr4.data[3] = 1; arr4.data[4] = 3;
    cout << "测试用例4: 原数组: ";
    for(int i=0; i<arr4.length; i++) cout << arr4.data[i] << " ";
    cout << endl;
    int min4 = find_min_num(arr4);
    cout << "最小值: " << min4 << endl;
    cout << "数组变为: ";
    for(int i=0; i<arr4.length; i++) cout << arr4.data[i] << " ";
    cout << endl << endl;

    // 测试用例5: 最小值在末尾
    Array arr5;
    arr5.length = 5;
    arr5.data[0] = 3; arr5.data[1] = 5; arr5.data[2] = 2; arr5.data[3] = 4; arr5.data[4] = 1;
    cout << "测试用例5: 原数组: ";
    for(int i=0; i<arr5.length; i++) cout << arr5.data[i] << " ";
    cout << endl;
    int min5 = find_min_num(arr5);
    cout << "最小值: " << min5 << endl;
    cout << "数组变为: ";
    for(int i=0; i<arr5.length; i++) cout << arr5.data[i] << " ";
    cout << endl << endl;

    return 0;
}