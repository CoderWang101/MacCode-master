#include <iostream>
#include <iomanip>
using namespace std;

namespace z
{
    int main()
    {
        int n;
        while (cin >> n)
        {
            double a0, an1;
            cin >> a0 >> an1;
            long double sumw = 0.0L;
            for (int i = 1; i <= n; ++i)
            {
                long double ci;
                cin >> ci;
                sumw += (long double)(n + 1 - i) * ci;
            }
            long double a1 = ((long double)an1 - 2.0L * sumw + (long double)n * a0) / (long double)(n + 1);
            cout << fixed << setprecision(2) << (double)a1 << "\n";
        }
        return 0;
    }
}
