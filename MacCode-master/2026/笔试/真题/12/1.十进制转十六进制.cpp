#include <iostream>
using namespace std;

namespace DecimalToHexadecimal
{
    string change(int n)
    {
        string str;
        char num[] = {'A', 'B', 'C', 'D', 'E', 'F'};
        while (n)
        {
            int temp = n % 16;
            if (temp < 10)
                str += temp + '0';
            else
                str += num[temp - 10];
            n /= 16;
        }
        reverse(str.begin(), str.end());
        return str;
    }

    int main()
    {
        int n;
        cin >> n;
        string number = change(n);
        cout << number << endl;

        return 0;
    }
}