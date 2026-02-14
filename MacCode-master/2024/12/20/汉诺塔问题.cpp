// 汉诺塔问题
#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void hanota(vector<int> &a, vector<int> &b, vector<int> &c)
    {
        dfs(a, b, c, a.size());
    }

    void dfs(vector<int> &a, vector<int> &b, vector<int> &c, int n)
    {
        if (n == 1) // 只有一个或剩下最后一个
        {
            c.push_back(a.back());
            a.pop_back();
            return;
        }

        dfs(a, c, b, n - 1); // 将上面转移
        c.push_back(a.back());
        a.pop_back();        // 最底下的转移到目标柱
        dfs(b, a, c, n - 1); // 将上面转移
    }
};