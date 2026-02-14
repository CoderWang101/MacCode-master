// #include <iostream>
// #include <vector>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     if (n == 0)
//         return 0;
//     vector<int> nums(n);
//     for (int i = 0; i < n; i++)
//         cin >> nums[i];

//     // 创建两个表
//     vector<int> f(n);
//     auto g = f;

//     f[0] = nums[0];
//     g[0] = 0;

//     for (int i = 0; i < n; i++)
//     {
//         // f[i]表示选i
//         // g[i]表示不选i
//         f[i] = g[i - 1] + nums[i];
//         g[i] = max(g[i - 1], f[i - 1]);
//     }
//     cout << max(f[n - 1], g[n - 1]) << endl; // 输出最大值

//     return 0;
// }