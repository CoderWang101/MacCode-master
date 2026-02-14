// #include <iostream>
// #include <iomanip>
// #include <cmath>
// using namespace std;

// const int MAX_S = 205;    // 因为x,y ≤ 100，所以x+y ≤ 200
// double D[MAX_S];          // D[s] 表示从原点到点(0,s)的折线距离
// double sqrt2 = sqrt(2.0); // 根号2的近似值

// // 预处理D数组
// void init()
// {
//     D[0] = 0.0; // 原点到自己的距离为0
//     // 递推计算D[s]
//     for (int s = 1; s < MAX_S; s++)
//     {
//         // D[s] = D[s-1] + (s-1)*√2 + √((s-1)^2 + s^2)
//         D[s] = D[s - 1] + (s - 1) * sqrt2 + sqrt((s - 1) * (s - 1) + s * s);
//     }
// }

// // 计算点(x,y)到原点的折线距离
// double dist(int x, int y)
// {
//     int s = x + y; // 点所在的斜线层级
//     // 距离 = D[s] + x * √2
//     return D[s] + x * sqrt2;
// }

// int main()
// {
//     init(); // 预处理
//     int N;
//     cin >> N;
//     cout << fixed << setprecision(3); // 输出保留三位小数

//     while (N--)
//     {
//         int x1, y1, x2, y2;
//         cin >> x1 >> y1 >> x2 >> y2;

//         double d1 = dist(x1, y1);
//         double d2 = dist(x2, y2);

//         double ans = fabs(d1 - d2); // 两点间折线距离
//         cout << ans << endl;
//     }

//     return 0;
// }
// // #include <iostream>
// // using namespace std;
// // double d[101][101];
// // void slove()
// // {
// //     d[0][0]=0,d[0][1]=1;d[1][0]=pow(2,0.5)+1;
// //     // d[0][2]=d[1][0]+pow(5,0.5);
// //     for (int i = 2; i <=100; i++)
// //     {
// //         int x=0,y=i;
// //         do
// //         {
// //             if(x==0)
// //             {
// //                 d[x][y]=d[y-1][x]+pow(pow(y,2)+pow(y-1,2),0.5);
// //                 x+=1,y-=1;
// //             }
// //             else
// //             {
// //                 double len=pow(2.0*pow(y+1,2),0.5)/(y+1);
// //                 d[x][y]=d[x-1][y+1]+len;
// //             }

// //         } while (y!=0);

// //         int n,x1,y1,x2,y2;
// //         cin>>n;
// //         while (n--)
// //         {
// //             cin>>x1>>y1>>x2>>y2;
// //             cout<<d[x2][y2]-d[x1][y2]<<endl;
// //         }
// //     }
// // }

// // int main()
// // {
// //     slove();

// //     return 0;
// // }