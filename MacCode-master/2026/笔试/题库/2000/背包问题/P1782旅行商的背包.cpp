// 题目：多重背包 + 奇货二次函数体积分配 的组合优化
// 思路总览：
// 1) 普通物品：每类体积 v、价值 w、数量 d，做“多重背包”。用按余数分组 + 单调队列优化，近似 O(n*C)。
// 2) 奇货：每件 j 的价值是 Y = a_j * X^2 + b_j * X + c_j。将容量按单位分配；
//    每增加 1 单位在同一件上，边际增益为 a_j*(2*t+1)+b_j（t 为已分配体积）。
//    用最大堆逐单位选择当前边际增益最大的货，得到前缀最优收益 spec_best[k]。
// 3) 组合：把容量 C 分成普通 used 与奇货 C-used，两者最优相加，再加常数 ∑c_j，取最大。
#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <limits>
#include <utility>
#include <algorithm>
using namespace std;
namespace a
{
    int main()
    {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n, m, C;
        if (!(cin >> n >> m >> C))
            return 0; // 读取失败直接退出
        // input
        vector<int> V(n), W(n), D(n);
        for (int i = 0; i < n; ++i)
            cin >> V[i] >> W[i] >> D[i]; // 普通物品：体积、价值、数量
        vector<long long> a(m), b(m), c(m);
        for (int i = 0; i < m; ++i)
            cin >> a[i] >> b[i] >> c[i]; // 奇货参数：a、b、c

        vector<long long> dp(C + 1, 0); // dp[c]：普通物品在容量 c 下的最优价值
        // 多重背包（单调队列优化，按体积 v 的余数分组）
        for (int i = 0; i < n; ++i)
        {
            int v = V[i], w = W[i], d = D[i];
            if (v == 0)
                continue; // 体积为 0 的物品跳过（避免除以 0）
            // 将容量 c 按 c ≡ r (mod v) 分组；每组做一条“线性”DP
            for (int r = 0; r < v; ++r)
            {
                int max_k = (C - r) / v; // 该组里可容纳的最大件数（步数）
                vector<long long> f(max_k + 1), g(max_k + 1);
                // f[j] 是旧 dp 在容量 r + j*v 的值
                for (int j = 0; j <= max_k; ++j)
                    f[j] = dp[r + j * v];
                deque<int> q; // 维护窗口内的最优下标，单调队列
                // 目标转移：g[j] = max_{t∈[j-d, j]} f[t] + (j-t)*w
                // 等价于维护 f[t] - t*w 的窗口最大值，再加上 j*w
                for (int j = 0; j <= max_k; ++j)
                {
                    // 保持窗口大小：t >= j - d
                    while (!q.empty() && q.front() < j - d)
                        q.pop_front();
                    long long val = f[j] - 1LL * j * w;
                    // 维护队尾单调不增，使得队首为最大值
                    while (!q.empty() && f[q.back()] - 1LL * q.back() * w <= val)
                        q.pop_back();
                    q.push_back(j);
                    // 当前最优 t = q.front()
                    g[j] = f[q.front()] + 1LL * (j - q.front()) * w;
                }
                // 写回 dp（该组的所有点）
                for (int j = 0; j <= max_k; ++j)
                    dp[r + j * v] = g[j];
            }
        }
        long long sum_ci = 0;
        for (int i = 0; i < m; ++i)
            sum_ci += c[i]; // ∑c_i 是常数，加在最终答案上
        // 奇货体积分配：优先给“当前边际增益”最大的货
        vector<int> t(m, 0);                     // t[i] 表示第 i 件奇货当前已分配体积
        priority_queue<pair<long long, int>> pq; // (边际增益, 货物编号)
        for (int i = 0; i < m; ++i)
        {
            long long gain = a[i] * (2LL * t[i] + 1) + b[i]; // 授予下一单位的增益
            pq.push({gain, i});
        }
        vector<long long> spec_best(C + 1, 0); // spec_best[s]：给奇货 s 单位体积的最优总增益（不含 ∑c_i）
        long long acc = 0;                     // 已累计的奇货增益（不含 ∑c_i）
        for (int s = 1; s <= C; ++s)
        {
            if (pq.empty())
            { // 没有可分配（理论上很少发生）
                for (int k = s; k <= C; ++k)
                    spec_best[k] = acc;
                break;
            }
            auto top = pq.top();
            pq.pop();
            long long gain = top.first;
            int idx = top.second;
            if (gain <= 0)
            { // 所有下一单位的边际增益都非正，继续分配只会变差，停止
                for (int k = s; k <= C; ++k)
                    spec_best[k] = acc;
                break;
            }
            acc += gain;                                                // 分配 1 单位给 idx
            spec_best[s] = acc;                                         // 记录前缀 s 的最优增益
            ++t[idx];                                                   // 更新该货已分配体积
            long long next_gain = a[idx] * (2LL * t[idx] + 1) + b[idx]; // 下一单位的边际增益
            pq.push({next_gain, idx});
            if (s == C)
            { // 最后一次，填充剩余（与 acc 相同）
                for (int k = s; k <= C; ++k)
                    spec_best[k] = acc;
            }
        }
        long long ans = LLONG_MIN;
        for (int used = 0; used <= C; ++used)
        {                                                            // 枚举普通物品使用的容量 used
            long long cur = dp[used] + spec_best[C - used] + sum_ci; // 剩余给奇货的收益 + 常数项
            if (cur > ans)
                ans = cur;
        }
        cout << ans << "\n";
        return 0;
    }
}