// // 鞋带公式
// // S三角形=0.5∗((x1∗y2+x2∗y3+x3∗y1)−(y1∗x2+y2∗x3+y3∗x1))
// #include <iostream>
// #include <iomanip>
// #include <cmath>
// using namespace std;

// int main()
// {
//     int n;

//     while (cin >> n && n != 0)
//     {
//         int x[100], y[100];

//         // 读取顶点坐标
//         for (int i = 0; i < n; i++)
//             cin >> x[i] >> y[i];

//         // 使用鞋带公式计算面积
//         long long sum = 0;
//         for (int i = 0; i < n; i++)
//         {
//             int j = (i + 1) % n; // 下一个顶点，循环处理
//             sum += (long long)x[i] * y[j] - (long long)x[j] * y[i];
//         }

//         // 计算面积并取绝对值
//         double area = 0.5 * fabs((double)sum);

//         // 输出结果，保留一位小数
//         cout << fixed << setprecision(1) << area << endl;
//     }

//     return 0;
// }