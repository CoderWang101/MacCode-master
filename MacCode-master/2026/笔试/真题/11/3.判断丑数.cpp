#include <iostream>
using namespace std;
namespace ugly
{
    // 判断是否是丑数
    bool ugly(int n)
    {
        if (n <= 0)
            return false;
        while (n % 2 == 0)
            n /= 2;
        while (n % 3 == 0)
            n /= 3;
        while (n % 5 == 0)
            n /= 5;
        while (n % 7 == 0)
            n /= 7;
        return n == 1;
    }
    int main()
    {
        int n;
        cin >> n;
        if (ugly(n))
            cout << "是丑数";
        else
            cout << "不是丑数";
        return 0;
    }
}