// #include <iostream>
// #include <algorithm>
// using namespace std;

// int main()
// {
//     pair<int, int> p[2];
//     for (int i = 0; i < 2; i++)
//         cin >> p[i].first >> p[i].second;
//     double d = abs(
//                     pow(
//                         abs(pow(p[0].first, 2) - pow(p[1].first, 2)), 0.5) 
//                 + pow(
//                     abs(pow(p[0].second, 2) - pow(p[1].second, 2)), 0.5));

//     cout << d << endl;
//     return 0;
// }
// #include <iostream>
// #include <algorithm>
// using namespace std;

// int main()
// {
//     int a[5] = {5, 4, 2, 5, 7};
//     int b[5] = {6, 2, 5, 8, 2};
//     pair<int, int> d[5];
//     for (int i = 0; i < 5; i++)
//     {
//         d[i] = make_pair(a[i], b[i]);
//     }
//     cout << "原始数据:" << endl;
//     for (int i = 0; i < 5; i++)
//         cout << d[i].first << " " << d[i].second << endl;

//     // 使用sort排序
//     //数据按first的大小进行排序，如果first相同，则再进一步按second排序
//     sort(d, d + 5);

//     cout << "使用sort排序后:" << endl;
//     for (int i = 0; i < 5; i++)
//         cout << d[i].first << " " << d[i].second << endl;

//     return 0;
// }