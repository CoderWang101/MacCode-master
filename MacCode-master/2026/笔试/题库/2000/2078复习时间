#include <iostream>
using namespace std;

void slove()
{
    int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];
        sort(a.begin(), a.end());
        // 去重
        a.erase(unique(a.begin(), a.end()), a.end());

        int M = a.size();
        int cap = min(M, m);
        // dp[i][k] 表示以第i门课结尾，选了k门课的最大效率
        vector<vector<int>> dp(M, vector<int>(cap + 1, 0));
        // 选第一门课
        for (int i = 0; i < M; i++)
            dp[i][1] = (100 - a[i]) * (100 - a[i]);

        for (int k = 2; k <= cap; k++)
        {
            for (int i = 0; i < M; i++)
            {
                int max_val = 0;
                for (int j = 0; j < i; j++)
                {
                    if (a[i] < a[j])
                    {
                        int val = dp[j][k - 1] + (a[j] - a[i]) * (a[j] - a[i]);
                        if (val > max_val)
                            max_val = val;
                    }
                }
                dp[i][k] = max_val;
            }
        }
        // 找出所有k中的最大值
        int ans = 0;
        for (int k = 1; k <= cap; k++)
            for (int i = 0; i < M; i++)
                if (dp[i][k] > ans)
                    ans = dp[i][k];
                    
        cout << ans << endl;
    }
}

int main()
{
    slove();
    return 0;
}