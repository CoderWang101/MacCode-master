#include <iostream>
using namespace std;

namespace findyourpresent
{
    int main()
    {
        int n;
        while (cin >> n && n)
        {
            int ans = 0;
            while (n--)
            {
                int a;
                cin >> a;
                ans ^= a;
            }
            cout << ans << endl;
        }

        return 0;
    }
}