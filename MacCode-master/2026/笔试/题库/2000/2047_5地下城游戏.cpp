// #include <iostream>
// #include <vector>
// using namespace std;
// // 最低生命值‘0<boold<min'
// // 更优:底往上

// int better_calulateMinimumHP(vector<vector<int>> &d)
// {
//     int m = d.size(), n = d[0].size();
//     vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));
//     dp[m][n - 1] = dp[m - 1][n] = 1;
//     for (int i = m - 1; i >= 0; i++)
//     {
//         for (int j = n - 1; j >= 0; j++)
//         {
//             dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) - d[i][j];
//             dp[i][j] = max(1, dp[i][j]);
//         }
//         return dp[0][0];
//     }
// }

// long long min_(int &a, int &b)
// {
//     if (a > 0 && b > 0)
//         return min(a, b);
//     else if (a < 0 && b < 0)
//     {
//         if (abs(a) > abs(b))
//             return b;
//         else
//             return a;
//     }
//     else
//     {
//         if (a == 0)
//             return b;
//         else
//             return a;
//     }
// }

// int main()
// {
//     while (true)
//     {
//         int m, n;
//         cin >> m >> n;

//         vector<vector<int>> graph(m + 1, vector<int>(n + 1));
//         for (int i = 1; i <= m; i++)
//             for (int j = 1; j <= n; j++)
//                 cin >> graph[i][j];

//         vector<vector<int>> dp(m + 1, vector<int>(n + 1));
//         dp[1][1] = graph[1][1];

//         for (int i = 1; i <= m; i++)
//         {
//             for (int j = 1; j <= n; j++)
//             {
//                 dp[i][j] = graph[i][j] + min_(dp[i - 1][j], dp[i][j - 1]);
//             }
//         }
//         cout << "数组内容:" << endl;
//         for (int i = 1; i <= m; i++)
//         {
//             for (int j = 1; j <= n; j++)
//             {
//                 cout << dp[i][j] << "\t";
//             }
//             cout << endl;
//         }
//         cout << "最低所需血量为:" << endl;
//         cout << abs(dp[m][n]) + 1 << endl;
//     }

//     return 0;
// }