// #include <iostream>
// using namespace std;
// // 环形

// int rob(vector<int> &nums, int left, int right)
// {
//     int n=nums.size();
//     // 两种情况:第一个位置 偷 or 不偷
//     vector<int> f(n); // 偷
//     auto g = f;       // 不偷

//     // 初始化
//     f[0] = nums[0];
//     g[0] = 0;

//     for (int i = left+1; i <= right; i++)
//     {
//         f[i] = nums[i] + g[i - 1];
//         // g[i]分两种,偷i-1,不偷i-1
//         g[i] = max(f[i - 1], g[i - 1]);
//     }
//     return max(g[right],f[right]);
// }

// int main()
// {
//     int n;
//     cin >> n;
//     if (n == 0)
//         return 0;
//     vector<int> nums(n);
//     for (int i = 0; i < n; i++)
//         cin >> nums[i];

//     cout << max(nums[0] + rob(nums, 2, n - 2), rob(nums, 1, n - 1)) << endl;

//     return 0;
// }