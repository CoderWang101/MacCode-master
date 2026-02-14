// #include <iostream>
// #include <vector>
// using namespace std;

// int main()
// {
//     while (true)
//     {
//         int m, n;
//         cin >> m >> n;
//         vector<vector<long long>> dp(m + 1, vector<long long>(n + 1));
//         dp[0][1] = 1;

//         for (int i = 1; i <= m; i++)
//         {
//             for (int j = 1; j <= n; j++)
//             {
//                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
//             }
//         }
//         cout<<"数组内容:"<<endl;
//         for (int i = 1; i <=m; i++)
//         {
//             for (int j = 1; j <= n; j++)
//             {
//                 cout<<dp[i][j]<<"\t";
//             }
//             cout<<endl;
//         }
//         cout<<"路径个数:"<<endl;
//         cout << dp[m][n] << endl;
//     }

//     return 0;
// }