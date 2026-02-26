#include <iostream>
#include <string>
#include <cstdio>
#include <iomanip>
using namespace std;

static int to_seconds(const string &t)
{
    int h = 0, m = 0, s = 0;
    //当需要将C++中的string对象传递给只接受C风格字符串的C语言函数时，就需要使用c_str()函数。
    sscanf(t.c_str(), "%d:%d:%d", &h, &m, &s);
    return h * 3600 + m * 60 + s;
}

int main()
{
    string t1, t2;
    cin >> t1 >> t2;
    int d = to_seconds(t2) - to_seconds(t1);
    int sign = d < 0 ? -1 : 1;
    d = sign < 0 ? -d : d;
    int h = d / 3600;
    int m = (d % 3600) / 60;
    int s = d % 60;
    if (sign < 0)
        cout << "-";
    cout << setw(2) << setfill('0') << h << ":"
         << setw(2) << setfill('0') << m << ":"
         << setw(2) << setfill('0') << s << endl;
    return 0;
}
