#include<iostream>
#include<vector>
using namespace std;

int compute1(int n)
{
    if (n == 1) return 3;
    
    // dp[i][0]：长度为i，最后一个字符不是'O'
    // dp[i][1]：长度为i，最后一个字符是'O'
    vector<vector<long long>> dp(n + 1, vector<long long>(2, 0));
    
    // 初始化：长度为1
    dp[1][0] = 2;  // E或F
    dp[1][1] = 1;  // O
    
    // 动态规划
    for (int i = 2; i <= n; i++)
    {
        // 当前不是'O'，可以由前一个不是'O'或前一个是'O'转移过来，并且有2种选择(E或F)
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * 2;
        // 当前是'O'，只能由前一个不是'O'转移过来
        dp[i][1] = dp[i-1][0];
    }
    
    return dp[n][0] + dp[n][1];
}

// int main()
// {
//     int n;
//     while (cin >> n)
//         cout << compute(n) << endl;
//     return 0;
// }