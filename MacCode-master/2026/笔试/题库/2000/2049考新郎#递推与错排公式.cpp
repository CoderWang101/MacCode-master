// #include <stdio.h>

// int main(void)
// {
//     int i, m, n;
//     long long a[21][2] = {{1, 0}, {1, 0}, {2, 1}, {6, 2}};

//     // 预处理：计算阶乘和错排数
//     for (i = 4; i < 21; i++)
//     {
//         a[i][0] = i * a[i - 1][0]; // i! = i × (i-1)!
//         // 错排数递推 D(n) = (n-1) × [D(n-1) + D(n-2)]
//         a[i][1] = (i - 1) * (a[i - 1][1] + a[i - 2][1]);
//     }

//     scanf("%d", &i);
//     while (i-- && scanf("%d%d", &n, &m))
//     {
//         // 计算 C(n, m) × D(m)
//         // C(n, m) = n! / (m! × (n-m)!)
//         // 注意：先计算组合数再乘错排数
//         long long result = a[n][0] / a[m][0] / a[n - m][0] * a[m][1];
//         printf("%lld\n", result); // 改为十进制输出
//     }

//     return 0;
// }