// #include <iostream>
// #include <vector>
// using namespace std;

// void compute2(int n)
// {
//     while (n--)
//     {
//         int m, n;
//         cin >> n >> m;

//         auto i = n;
//         while (i--) // wide
//         {
//             int j = m;
//             if (i == n - 1 || i == 0)
//             {
//                 cout << '+';
//                 while (j--)
//                     cout << '-';
//                 cout << '+' << endl;

//                 if(i==0)
//                     break;
//             }
//             j = m+1;
//             cout << '|';
//             while (j--)
//                 cout << ' ';
//             cout << '|' << endl;
//         }
//     }
// }

// int main()
// {
//     int n;
//     cin >> n;
//     compute2(n);
//     return 0;
// }