// 2022 省 B] 
#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int cost_day=0;
    int day=0;

    // int a=10;
    // int b=20;
    // int n=99;
    int a,b,n;
    cin>>a>>b>>n;

    // vector<int> day_num(7);
    // for(int i=0;i<5;++i)
    // {
    //     day_num[i]=a;
    // }
    // day_num[6]=day_num[5]=b;

    //优化直接计算一周要做的题目
    int week=5*a+b*2;
    int week_num=n/week;
    int week_loss=n%week;

    if (week_num<=5*a)//在工作日完成
        cout<<week_num*7+(week_loss+a-1)/a;
    else//周末完成
        cout<<week_num*7+5+(week_loss-5*a+b-1)/b;



    // while (true)
    // {
    //     day=day%6;
    //     if(day_num[day]<n)
    //     {
    //         n-=day_num[day];
    //     }
    //     else
    //         break;

    //     day++;
    //     cost_day++;
    // }
    // cout<<cost_day<<endl;

    return 0;
}