#include <iostream>
#include <vector>
using namespace std;
namespace w
{
    int main()
    {
        int T;
        cin >> T;
        while (T--)
        {
            int N;
            cin >> N;
            vector<vector<int>> a(N, vector<int>(N, 0)); // 存储三角形，只用到下三角
            for (int i = 0; i < N; ++i)
                for (int j = 0; j <= i; ++j)
                    cin >> a[i][j];

            // 从下到上
            auto dp = a; // dp[i][j]表示从(i,j)到上一层的最大路径和
            for (int i = N - 2; i >= 0; i--)
            {
                for (int j = 0; j <= i; j++)
                {
                    dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + a[i][j];
                }
            }
            cout << dp[0][0] << endl;
        }
        return 0;
    }
}