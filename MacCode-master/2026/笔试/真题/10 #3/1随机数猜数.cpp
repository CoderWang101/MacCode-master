// #include <iostream>
// using namespace std;

// int main()
// {
//     int r = rand() % 900 + 100; // 生成100-999的随机数
//     int flag = 10;

//     while (flag)
//     {
//         int a;
//         cout << "请输入你猜的三位数：" << endl;
//         cin >> a;

//         if (a == r)
//         {
//             cout << "恭喜你，猜对了！" << endl;
//             break;
//         }
//         else if (a > r)
//             cout << "你猜的数字大了，请重新输入！" << endl;
//         else
//             cout << "你猜的数字小了，请重新输入！" << endl;
//         flag--;
//     }
//     cout << "Bye Bye!" << endl;

//     return 0;
// }