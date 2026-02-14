// #include <iostream>
// #include <vector>
// using namespace std;
// //有障碍物
// int main()
// {
//     while (true)
//     {
//         int m, n;
//         cin >> m >> n;
//         vector<vector<long long>> graph(m + 1, vector<long long>(n + 1));
//         for (int i = 1; i < m+1; i++)
//             for (int j = 1; j < n+1; j++)
//                 cin>>graph[i][j];//1为障碍物       
        

//         vector<vector<long long>> dp(m + 1, vector<long long>(n + 1));
//         dp[0][1] = 1;

//         for (int i = 1; i <= m; i++)
//         {
//             for (int j = 1; j <= n; j++)
//             {
//                 if(graph[i][j]==1)
//                 {
//                     dp[i][j]=0;
//                     continue;
//                 }
//                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
//             }
//         }
//         // cout<<"数组内容:"<<endl;
//         // for (int i = 1; i <=m; i++)
//         // {
//         //     for (int j = 1; j <= n; j++)
//         //     {
//         //         cout<<dp[i][j]<<"\t";
//         //     }
//         //     cout<<endl;
//         // }
//         cout<<"路径个数:"<<endl;
//         cout << dp[m][n] << endl;
//     }

//     return 0;
// }