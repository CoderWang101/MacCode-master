// #include <iostream>
// #include <cstdio>
// using namespace std;

// typedef unsigned long long ull;

// // 快速幂取模：计算 (a^b) % mod
// int pow_mod(int a, ull b, int mod)
// {
//     int res = 1 % mod;
//     while (b)
//     {
//         if (b & 1)
//             res = (res * a) % mod;
//         a = (a * a) % mod;
//         b >>= 1;
//     }
//     return res;
// }

// int main()
// {
//     int T;
//     while (scanf("%d", &T) == 1 && T != 0)
//     {
//         ull N;
//         for (int i = 0; i < T; ++i)
//         {
//             scanf("%llu", &N);
//             // 公式：ans = 4^(N-1) + 2^(N-1) (mod 100)
//             int ans = (pow_mod(4, N - 1, 100) + pow_mod(2, N - 1, 100)) % 100;
//             printf("%02d\n", ans);
//         }
//         // 每组输出后跟一个空行
//         printf("\n");
//     }
//     return 0;
// }