// #include <iostream>
// using namespace std;

// void slove(int n)
// {
//     int caseNum = 1; // 序号从1开始
//     // 使用递推公式计算卡特兰数: C_0 = 1, C_n = C_{n-1} * (4*n-2) / (n+1)
//     long long catalan = 1; // C_0

//     // 计算 C_n
//     for (int i = 1; i <= n; i++)
//         catalan = catalan * (4 * i - 2) / (i + 1);

//     // 输出结果：序号, n, 2 * 卡特兰数
//     cout << caseNum << " " << n << " " << catalan * 2 << endl;
//     caseNum++;
// }

// int main()
// {
//     int n, count = 0;
//     while (cin >> n && n != -1)
//         slove(n);

//     return 0;
// }