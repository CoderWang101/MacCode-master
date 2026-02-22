#include <iostream>
#include <vector>
using namespace std;
namespace better_box
{
    int main()
    {
        int n;
        while (cin >> n)
        {
            if (n == 0)
                break;
            vector<int> bricks(n);
            int sum = 0;
            for (int i = 0; i < n; ++i)
            {
                cin >> bricks[i];
                sum += bricks[i];
            }
            int avg = sum / n;
            int moves = 0;

            for (int h : bricks)
                if (h > avg)
                    moves += h - avg;

            cout << moves << "\n";
        }
        return 0;
    }
}

namespace box
{
    int main()
    {
        int n;
        while (cin >> n)
        {
            if (n == 0)
                break;

            vector<int> bricks(n);
            int sum = 0;
            for (int i = 0; i < n; i++)
            {
                cin >> bricks[i];
                sum += bricks[i];
            }
            sort(bricks.begin(), bricks.end());
            int avg = sum / n;
            int step = 0;
            int min = 0, max = n - 1;
            while (bricks[max] != avg && bricks[min] != avg)
            {
                int max_surplus = bricks[max] - avg;
                int min_need = avg - bricks[min];
                // 最大 surplus 小于 最小 need，说明最大的数需要移动
                if (max_surplus < min_need)
                {
                    step += max_surplus;
                    min_need -= max_surplus;
                    max -= 1;
                }
                else if (max_surplus > min_need)
                {
                    step += min_need;
                    max_surplus -= min_need;
                    min += 1;
                }
                else
                {
                    step += max_surplus;
                    max_surplus -= max_surplus;
                    min_need -= max_surplus;
                    max -= 1;
                    min += 1;
                }
            }
            cout << step << endl;
        }

        return 0;
    }

}