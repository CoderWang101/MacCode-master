#include<iostream>
using namespace std;

int main()
{
    int N;
    cin >> N;//总人数
    int arr[N];
    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];//输入每个人的座位号
    }
    int x=0,y=0;
    for (int i = 0; i < N; i++)
    {
        if(arr[i]%2!=0)
            x++;
        else
            y++;
    }
    printf("成年人人数:%d\t,占比:%.2f\t",x,(double)x/N);
    printf("未成年人数:%d\t,占比:%.2f\n",y,(double)y/N);
    return 0;
}