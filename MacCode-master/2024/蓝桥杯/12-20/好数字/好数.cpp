// P10424 [蓝桥杯 2024 省 B] 好数
// 一个整数如果按从低位到高位的顺序，奇数位（个位、百位、万位……）上的数字是奇数，偶数位（十位、千位、十万位……）上的数字是偶数，我们就称之为“好数”。
#include <iostream>
using namespace std;

bool cla(int x)
{
    int i=1;
    while(x>0)
    {
        if (i%2==1)
        {
            if ((x%10)%2==0)return 0;
        }
        else 
        {
            if ((x%10)%2==1)return 0;
        }
        x/=10,i++;
    }
    return 1;
}

// 枚举
int main()
{
    int N = 24;
    int ans=0; // 好数的个数
    cin>>N;
    for (int i = 1; i <=N; i++)
    {
        if (cla(i) == 1)
            ans++;
    }
    cout << ans;
    return 0;
}


// 思路:单独计算最高为的好数
//  int main()
//  {
//      int n=24;
//      int odd[]={1,3,5,7,9};
//      int even[]={0,2,4,6,8};

//     //计算最高位的好数
//     int count=0;
//     for(int i=0;i<5;++i)
//     {
//         if(n%10==odd[i])
//         {
//             count++;
//             break;
//         }
//     }
//     for(int i=0;i<5;++i)
//     {
//         if(n%10==even[i])
//         {
//             count++;
//             break;
//         }
//     }

//     return 0;
// }
