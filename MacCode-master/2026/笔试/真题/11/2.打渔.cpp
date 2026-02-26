#include <iostream>
using namespace std;
namespace years
{
    // 判断是否是闰年
    bool years(int y)
    {
        if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0)
            return true;
        else
            return false;
    }

    int main()
    {
        int mounth, day;
        cin >> mounth >> day;

        int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}; // 每个月的天数
        // if(years(2023))//如果是闰年
        //     days[1]=29;//2月有29天
        int total = 0;
        for (int i = 0; i < mounth - 1; i++)
            total += days[i];
        total += day;

        if ((total %= 5) <= 3)
            cout << "打鱼";
        else
            cout << "晒网";

        return 0;
    }
}