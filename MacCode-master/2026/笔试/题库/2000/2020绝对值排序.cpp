// #include<iostream>
// using namespace std;

// bool compare(const int& a,const int& b)
// {
//     return abs(a)>abs(b);
// }


// int main()
// {
//     int n;
//     while(cin>>n)
//     {
//         vector<int> a(n);
//         for (int i = 0; i < n; i++)
//             cin >> a[i];
//         sort(a.begin(), a.end(),compare);        
//         for (int i = 0; i < n; i++)
//             cout << a[i] << " ";
//         cout << endl;
//     }


//     return 0;
// }

// #include <math.h>
// #include <stdio.h>
// #include <stdlib.h>

// int cmp(const int *a, const int *b)
// {
//     return abs(*b) - abs(*a);
// }

// int main(void)
// {
//     int n, i, x[101];
    
//     while (scanf("%d", &n), n)
//     {
//         for (i = 0 ; i < n ; i++)
//             scanf("%d", x + i);
//         qsort(x, n, sizeof(int), cmp);
//         for (i = 0 ; i < n ; i++)
//             printf("%d%c", x[i], (i != n - 1 ? ' ' : '\n'));
//     }

//     return 0;
// }