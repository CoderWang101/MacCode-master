// #include <iostream>
// #include <vector>
// using namespace std;
// // 下降相邻左中右,走到底算结束;
// long long min_(long long& a,long long& b,long long& c)
// {
//     int select=a;
//     if(b<select)
//         select=b;
//     if(c<select)
//         select=c;
//     return select;
// }

// int main()
// {
//     while (true)
//     {
//         int m, n;
//         cin >> m >> n;
//         vector<vector<long long>> graph(m + 2, vector<long long>(n + 2));
//         for (int i = 1; i < m + 1; i++)
//             for (int j = 1; j < n + 1; j++)
//                 cin >> graph[i][j];

//         vector<vector<long long>> dp(m + 2, vector<long long>(n + 2));
//         for (int j = 0; j <= n; j++)
//             dp[0][j] = 0;
//         for (int j = 0; j <= m; j++)
//         {
//             dp[j][0] = 0x3f3f3f3f;
//             dp[j][n+1] = 0x3f3f3f3f;
//         }
//         //dp
//         for (int i = 1; i <= m; i++)
//             for (int j = 1; j <= n; j++)
//                 dp[i][j]=graph[i][j]+min_(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]);

//         //找到最后一行最小值
//         long long min = 0x3f3f3f3f;
//         for (int i = 1; i < n+1; i++)
//             if (dp[m][i] < min)
//                 min = dp[m][i];
//         cout << "路径最小值:" << endl;
//         cout << min << endl;
//     }

//     return 0;
// }
//         // //遍历dp
//         // for (int i =1; i < m+1; i++)
//         // {
//         //     for (int j = 1; j < n+1; j++)
//         //         cout << dp[i][j] << "\t";
//         //     cout << endl;
//         // }