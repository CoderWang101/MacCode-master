// #include <iostream>
// #include <string>
// using namespace std;

// bool isalpha_(char c)
// {
//     if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
//         return true;
//     return false;
// }


// int main()
// {
//     int n;
//     cin >> n;
//     cin.ignore(); // 忽略换行符

//     while (n--)
//     {
//         string str;
//         getline(cin,str);
        
//         if (str[0] != '_' && !isalpha_(str[0]))
//         {
//             cout << "No" << endl;
//             continue;
//         }
//         for (int i = 1; i < str.size(); i++)
//         {
//             if(!isalpha_(str[i]) && !(str[i]>='0' && str[i]<='9') && str[i]!='_')
//             {
//                 cout<<"No"<<endl;
//                 break;
//             }
//             else if(i==str.size()-1)
//                 cout<<"Yes"<<endl;
//         }
        
//     }

//     return 0;
// }