#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int N;
    cin >> N;
    while (N--)
    {
        int words[27];
        for (int i = 1; i <= 26; i++)
            cin >> words[i];

        // 总价值<=50的单词数
        int dp[51] = {0};
        dp[0] = 1;

        for (int i = 1; i <= 26; i++) // 遍历每个单词
        {
            int number = i;              // 当前单词价值
            int count = words[i];        // 当前单词数量
            
            for (int j = 50; j > 0; --j) // 遍历每个价值
                for (int k = 1; k <= count; k++)//遍历每个单词数量
                    if (j >= k * number)//可以选k个当前单词
                        dp[j] += dp[j - k * number];
        }
        // 计算总方案数字
        int ans = 0;
        for (auto v : dp)
            ans += v;
        cout << ans - 1 << endl;
    }
    return 0;
}