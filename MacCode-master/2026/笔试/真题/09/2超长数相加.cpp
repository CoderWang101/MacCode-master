// #include<iostream>
// #include<stdio.h>
// using namespace std;

// int main()
// {
//     //数字过长采用string存储
//     string num1, num2;
//     cout << "请输入第一个大整数：" << endl;
//     cin >> num1;
//     cout << "请输入第二个大整数：" << endl;
//     cin >> num2;

//     //反转字符串，方便从低位开始相加
//     reverse(num1.begin(), num1.end());
//     reverse(num2.begin(),num2.end());
//     //进位标志
//     string result = "";
//     int carry = 0;
//     string longer=(num1.length()>num2.length()?num1:num2);
//     string shorter=(num1.length()>num2.length()?num2:num1);
//     int maxLength=longer.length();
//     int minLength=shorter.length();

//     //逐位相加（低位到高位，考虑进位)
//     while (carry<minLength)
//     {
//         longer[carry]=shorter[carry]-'0'+longer[carry]-'0'+'0';
//         //判断是否需要进位  
//         if(longer[carry]>'9')
//         {
//             longer[carry]=longer[carry]-10;
//             carry++;
//             if(carry<minLength)
//                 longer[carry]=longer[carry]+1;
//         }
//         else//不需要进位
//             carry++;
   
//     }
//     if(carry<maxLength)//处理长度不等的情况
//     {
//         while(carry<maxLength)
//         {
//             if(longer[carry]>'9')
//             {
//                 longer[carry]=longer[carry]-10;
//                 carry++;
//                 if(carry<maxLength)
//                     longer[carry]=longer[carry]+1;
//             }
//             else
//                 carry++;
//         }
//     }

//     //最高位有进位
//     if(carry==maxLength && longer[carry]>'9')
//         longer=longer+'1';
//     //反转结果字符串
//     reverse(longer.begin(),longer.end());
//     cout<<"两个大整数之和为："<<longer<<endl;

//     return 0;
// }