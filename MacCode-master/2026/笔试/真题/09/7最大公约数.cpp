// #include <iostream>
// using namespace std;
// //最大公约数:两个或多个整数共有约数中最大的一个数。
// //最小公倍数:两个或多个整数共有倍数中最小的一个数。

// //求最大公约数的方法：欧几里得算法
// int gcd(int a,int b)
// {
//     if (b==0)
//         return a;
//     else
//         return gcd(b,a%b);
// }
// //求最小公倍数的方法：两个数的乘积除以它们的最大公约数
// int lcm(int a,int b)
// {
//     return a*b/gcd(a,b);
// }

// int main()
// {
//     int a,b;
//     cout<<"请输入两个正整数："<<endl;
//     cin>>a>>b;
//     int greatest_common_divisor=gcd(a,b);
//     int least_common_multiple=lcm(a,b);

//     cout<<"最大公约数为："<<greatest_common_divisor<<endl;
//     cout<<"最小公倍数为："<<least_common_multiple<<endl;


//     return 0;
// }