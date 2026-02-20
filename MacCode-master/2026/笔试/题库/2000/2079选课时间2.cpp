#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
/*
Input
输入数据的第一行是一个数据T，表示有T组数据。
每组数据的第一行是两个整数n(1 <= n <= 40)，k(1 <= k <= 8)。
接着有k行，每行有两个整数a(1 <= a <= 8),b(1 <= b <= 10)，表示学分为a的课有b门。
Output
对于每组输入数据，输出一个整数，表示学n个学分的组合数。
*/
void slove()
{
    int T;
    cin>>T;
    while(T--)
    {
        int n,k;
        cin>>n>>k;//n:目标总分数,k:课程种类
        vector<vector<long long>> dp(k + 1, vector<long long>(n + 1, 0));
        dp[0][0] = 1;//目标学分为0仅由1种情况
        
        vector<pair<int,int>> types;
        types.reserve(k);
        for (int i = 1; i <=k; i++)
        {
            int score,course;//学分、课程数
            cin>>score>>course;
            types.emplace_back(score, course);
        }

        for (int i = 1; i <= k; i++)
        {
            int s = types[i-1].first;
            int c = types[i-1].second;
            //所有可能的总学分 j
            for (int j = 0; j <=n; j++)
            {
                for (int t = 0; t <= c; t++)
                {
                    if(j - t * s >= 0)
                        dp[i][j] += dp[i-1][j - t * s];
                }
            }
            
        }
        cout<<dp[k][n]<<endl;
    }
}
//利用滚动数组优化空间复杂度
void slove_better()
{
    int T;
    cin>>T;
    while(T--)
    {
        int n,k;
        cin>>n>>k;//n:目标总分数,k:课程种类
        vector<long long> dp(n + 1, 0);
        dp[0] = 1;//目标学分为0仅由1种情况
        
        vector<pair<int,int>> types;
        types.reserve(k);
        for (int i = 1; i <=k; i++)
        {
            int score,course;//学分、课程数
            cin>>score>>course;
            types.emplace_back(score, course);
        }
        for (int i = 1; i <= k; i++)
        {
            int s = types[i-1].first;
            int c = types[i-1].second;
            vector<long long> ndp(n + 1, 0);
            for (int j = 0; j <= n; j++)
                for (int t = 0; t <= c; t++)
                    if (j - t * s >= 0)
                        ndp[j] += dp[j - t * s];
            dp.swap(ndp);
            
        }
        cout<<dp[n]<<endl;
    }
}

int main()
{
    slove();
    return 0;
}
