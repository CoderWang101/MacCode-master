// #include <iostream>
// using namespace std;

// // 计算真约数之和的函数
// int sum_of_proper_divisors(int n) {
//     if (n <= 1) return 0;  // 0和1没有真约数（除了0和1本身，但真约数不包括自身）
    
//     int sum = 1;  // 对于大于1的数，1总是真约数
    
//     // 遍历可能的约数，直到i的平方超过n
//     for (int i = 2; i * i <= n; i++) {
//         if (n % i == 0) {
//             if (i * i == n) {
//                 // 如果是平方数，只加一次
//                 sum += i;
//             } else {
//                 // 否则加i和n/i两个约数
//                 sum += i + n / i;
//             }
//         }
//     }
//     return sum;
// }

// int main() {
//     int M;
//     cin >> M;
    
//     while (M--) {
//         int A, B;
//         cin >> A >> B;
        
//         // 亲和数要求两个数不同
//         if (A == B) {
//             cout << "NO" << endl;
//             continue;
//         }
        
//         int sumA = sum_of_proper_divisors(A);
//         int sumB = sum_of_proper_divisors(B);
        
//         // 检查亲和数条件：A的真约数之和等于B，且B的真约数之和等于A
//         if (sumA == B && sumB == A) {
//             cout << "YES" << endl;
//         } else {
//             cout << "NO" << endl;
//         }
//     }
    
//     return 0;
// }