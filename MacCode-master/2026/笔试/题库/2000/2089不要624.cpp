#include <iostream>
using namespace std;
namespace n624
{
    bool isValue(int x)
    {
        while (x > 0)
        {
            if (x % 10 == 4)
                return false;
            if (x % 100 == 62)
                return false;
            x /= 10;
        }
        return true;
    }

    int main()
    {
        int a, b;
        while (cin >> a >> b)
        {
            if (a == 0 && b == 0)
                break;
            int cnt = 0;
            for (int i = a; i <= b; ++i)
            {
                if (isValue(i))
                    cnt++;
            }
            cout << cnt << endl;
        }

        return 0;
    }
}