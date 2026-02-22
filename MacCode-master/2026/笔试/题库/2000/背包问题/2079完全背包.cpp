#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
namespace z
{
    int V, N; // 体积,物品数
    // 完全背包问题-每个物品可以选无限次
    void slove()
    {
        while (true)
        {
            cin >> V >> N;
            vector<pair<int, int>> goods;
            int v, w; // 体积,价值
            for (int i = 0; i < N; i++)
            {
                cin >> v >> w;
                goods.push_back({v, w});
            }
            // 1.无需装满
            vector<int> dp(V + 1, 0);
            // 状态转移
            for (int i = 0; i < N; i++)
                for (int j = goods[i].first; j <= V; j++)
                    dp[j] = max(dp[j], dp[j - goods[i].first] + goods[i].second);

            cout << dp[V] << endl;

            // 2.装满背包的最小物品数
            dp.clear();
            for (int j = 1; j <= V; j++)
                dp[j] = -1;

            for (int i = 1; i <= N; i++)
                for (int j = goods[i].first; j <= V; j++)
                    if (dp[j - goods[i].first] != -1)
                        dp[j] = min(dp[j], dp[j - goods[i].first] + 1);
        }
    }

    int main()
    {
        slove();
        return 0;
    }
}