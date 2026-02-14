// #include <iostream>
// #include <set>
// using namespace std;

// int main()
// {
//     int n, m;
//     while (cin >> n >> m)
//     {
//         set<int> a;
//         int t;
//         for (int i = 0; i < n; i++)
//         {
//             int x;
//             cin >> x;
//             a.insert(x);
//         }

//         while (m--)
//         {
//             cin >> t;
//             if (a.count(t))
//                 a.erase(t);
//         }
//         if (a.empty())
//             cout << "NULL" << endl;
//         else
//         {
//             set<int>::iterator it;
//             for(it=a.begin();it!=a.end();it++)
//                 cout<<*it<<" ";
//         }
//     }
//     return 0;
// }