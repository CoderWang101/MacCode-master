
#include <iostream>
#include <iomanip>
using namespace std;
namespace a
{
    int main(void)
    {
        int T;
        cin >> T;

        while (T--)
        {
            int x[2], y[2];
            cin >> x[0] >> y[0] >> x[1] >> y[1];
            // 点乘
            double dot = x[0] * x[1] + y[0] * y[1];

            // 计算模长
            double len1 = sqrt(pow(x[0], 2) + pow(y[0], 2));
            double len2 = sqrt(pow(x[1], 2) + pow(y[1], 2));

            // 计算cos值
            double cos_ = dot / (len1 * len2);
            // 计算角度
            double angle = acos(cos_) * 180.0 / M_PI;
            cout << fixed << setprecision(2) << angle << endl;
        }

        return 0;
    }
}