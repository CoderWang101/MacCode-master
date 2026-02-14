// #include <iostream>
// using namespace std;

// int main()
// {
//     int n;
//     while (cin >> n)
//     {
//         vector<int>delta(32,0);
//         delta[0]=1;

//         for (int i = 0; i < n; i++)
//         {
//             cout<<1<<" ";
//             // 每次更新时，从后往前更新，避免重复使用同一元素
//             for(int j=i;j;j--)
//                 delta[j]+=delta[j-1];// 组合数公式C(n,k)=C(n-1,k-1)+C(n-1,k)
            
//             // 输出当前行的组合数
//             for(int k=1;k<=i;k++)
//                 cout<<delta[k]<<" ";
//             cout<<endl;
//         }
//         cout<<endl;
        
//     }
//     return 0;
// }