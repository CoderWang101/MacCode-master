#include <iostream>
using namespace std;

namespace w
{
    void slove_baggage()
    {
        int n, V;
        cin >> n >> V;
        int w[n + 1], v[n + 1];
        for (int i = 1; i <= n; i++)
            cin >> w[i] >> v[i]; // w:价值,v:体积

        int dp[n + 1][n + 1];
        // 1.求背包至多装多少物品
        for (int i = 1; i <= n; i++)
            dp[i][0] = -1;

        // 从i个物品中挑选,体积不超过j
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= V; j++)
            {
                // 两种情况,选物品i或不选i
                dp[i][j] = dp[i - 1][j]; // 不选物品i
                // 1.总体积不超过j
                if (j - v[i] >= 0)                                        // 背包容量足够选物品i
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + v[i]); // 选物品i
            }
        }
        cout << dp[n][V] << endl;

        memset(dp, 0, sizeof(dp));
        for (int j = 1; j <= V; j++)
            dp[j][0] = -1;

        // 2.dp[i][i]=-1表示没有该情况
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= V; j++)
            {
                // 两种情况,选物品i或不选i
                dp[i][j] = dp[i - 1][j]; // 不选物品i
                // 2.总体积等于j
                if (j - v[i] >= 0 && dp[i - 1][j - v[i]] != -1)           //=-1表示无法满足装到j
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + v[i]); // 选物品i
            }
        }
        cout << (dp[n][V] == -1 ? 0 : dp[n][V]) << endl;
    }
    // 利用滚动数组进行优化(单行数组,从右往左更新)
    // 状态转移只依赖上一行，因此可将二维dp压缩为一维，倒序更新避免覆盖
    void slove_baggage_better()
    {
        int n, V;
        cin >> n >> V;
        int w[n + 1], v[n + 1];
        for (int i = 1; i <= n; i++)
            cin >> w[i] >> v[i]; // w:价值,v:体积

        int dp[V + 1]; // 滚动数组，仅一行

        // 1.求背包至多装多少物品
        memset(dp, 0, sizeof(dp));
        dp[0] = 0; // 体积为0时价值为0

        for (int i = 1; i <= n; i++)
            // 从右往左更新，避免覆盖
            for (int j = V; j >= v[i]; j--)
                if (dp[j - v[i]] != -1)
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i]);
        cout << dp[V] << endl;

        // 2.总体积恰好等于V
        memset(dp, 0, sizeof(dp));
        for (int j = 1; j <= V; j++)
            dp[j] = -1;

        for (int i = 1; i <= n; i++)
            for (int j = V; j >= v[i]; j--)
                if (dp[j - v[i]] != -1)
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i]);
        cout << (dp[V] == -1 ? 0 : dp[V]) << endl;
    }

    int main()
    {

        while (true)
        {
            slove_baggage();
        }
        return 0;
    }
}
