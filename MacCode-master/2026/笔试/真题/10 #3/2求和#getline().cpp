// #include <iostream>
// #include<stdio.h>
// using namespace std;

// string FindAndSum(string& str)
// {
//     int sum=0;
//     int i=0;
//     while(i<str.length())
//     {
//         string temp="";

//         //判断是否为数字字符
//         while(i<str.length() &&str[i]>='0' && str[i]<='9')//获取字符串中的数字
//         {
//             temp+=str[i];
//             i++;
//         }
//         if(temp!="")
//         {
//             sum+=stoi(temp);//字符串转换为整数并累加
//             temp="";
//         }
//         i++;
//     }
//     return to_string(sum);//整数转换为字符串返回
// }

// int main()
// {
//     string a;
//     cout << "请输入字符串：" << endl;
//     //输入字符串,并忽略空格
//     getline(cin,a);
//     // cout<<"输入的字符串为："<<a<<endl;

//     FindAndSum(a);
//     cout<<"字符串中数字之和为："<<FindAndSum(a)<<endl;

//     return 0;
// }