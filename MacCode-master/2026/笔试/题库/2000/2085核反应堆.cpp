// #include <iostream>
// using ll = long long;
// using namespace std;
// namespace z
// {
//     int main()
//     {
//         int n;
//         while (cin >> n)
//         {
//             if (n == -1)
//                 break;
//             ll a[2] = {1, 0}; // a[0] 高能，a[1] 低能
//             ll h = 0, l = 0;  // 临时记录本微秒将要产生的新粒子

//             for (int t = 0; t < n; ++t)
//             {
//                 h = 0;
//                 l = 0;

//                 // 所有高能质点撞击
//                 ll cnt_h = a[0];
//                 h += cnt_h * 3;
//                 l += cnt_h * 1;

//                 // 所有低能质点撞击
//                 ll cnt_l = a[1];
//                 h += cnt_l * 2;
//                 l += cnt_l * 1;

//                 // 更新下一秒的状态
//                 a[0] = h;
//                 a[1] = l;
//             }

//             cout << a[0] << ", " << a[1] << endl;
//         }
//         return 0;
//     }
// }