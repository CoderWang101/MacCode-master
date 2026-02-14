#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "请输入一个正整数：" << endl;
    cin >> n;
    int num=0;
    for(int i=1;i<= n;i++)
    {
        if(n%i==0 && i!=n)
            num+=i;
            // cout<<num<<endl;
    }   
    if(num==n)
        cout<<n<<"是完数"<<endl;
    else
        cout<<n<<"不是完数"<<endl;


    return 0;
}