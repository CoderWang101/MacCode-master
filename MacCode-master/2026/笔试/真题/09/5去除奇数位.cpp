// #include<iostream>
// using namespace std;

// void delete_odd_number(string& num)
// {
//     // reverse(num.begin(),num.end());
//     int i=0;
//     while(i<num.length() )
//     {
//         if((num[i]-'0')%(2)!=0)
//             num.erase(i,1);//删除奇数位数字
//         else
//             i++;
//     }
// }

// int main()
// {
//     //输入整型数
//     int val;
//     cout << "请输入一个整数：" << endl;
//     cin >> val;
//     //转化为字符串
//     string num=to_string(val);
//     delete_odd_number(num);

//     //string转换为整型数
//     int result=stoi(num);

//     cout<<"删除奇数位后的数字为："<<result<<endl;
//     return 0;
// }