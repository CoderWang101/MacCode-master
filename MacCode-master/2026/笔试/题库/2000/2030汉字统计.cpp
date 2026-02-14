// #include <iostream>
// #include <string>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     cin.ignore(); // 忽略第一行末尾的换行符

//     while (n--)
//     {
//         string line;
//         getline(cin, line); // 读取一行文本

//         int count = 0;
//         // 遍历字符串中的每个字符
//         for (int i = 0; i < line.length(); i++)
//         {
//             // 如果字符的ASCII码值小于0（有符号char）或大于127（无符号char），说明是汉字的一部分
//             if (line[i] < 0 || line[i] > 127)
//                 count++;
//         }
//         // 每个汉字占2个字节，所以除以2
//         cout << count / 2 << endl;
//     }
//     return 0;
// }