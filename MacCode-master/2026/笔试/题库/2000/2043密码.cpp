// #include<iostream>
// using namespace std;

// int isalpha_A(char c ,int& sum)
// {
//     if (c >= 'A' && c <= 'Z')
//         return ++sum;
//     return sum;
// }
// int isalpha_a(char c ,int& sum)
// {
//     if (c >= 'a' && c <= 'z')
//         return ++sum;
//     return sum;
// }
// int isalpha_n(char c ,int& sum)
// {
//     if (c >= '0' && c <= '9')
//         return ++sum;
//     return sum;
// }
// int isalpha_s(char c ,int& sum)
// {
//     if (c=='~'||c=='!' ||c=='@' ||c=='#' ||c=='$' ||c=='%' ||c=='^')
//         return ++sum;
//     return sum;
// }

// int main()
// {
//     int n;
//     cin>>n;
//     cin.ignore();
    
//     while (n--)
//     {
//         string s;
//         cin>>s;
//         if(s.length()<8 ||s.length()>=16)
//         {
//             cout<<"NO"<<endl;
//             continue;
//         }

//         vector<int> count(5);
//         for (int i = 0; i < s.length(); i++)
//         {
//             isalpha_A(s[i],count[0]);
//             isalpha_a(s[i],count[1]);
//             isalpha_n(s[i],count[2]);
//             isalpha_s(s[i],count[3]);
//         }
//         for (int i = 0; i < 4; i++)
//             if(count[i]!=0)
//                 ++count[4];
//         // for (int i = 0; i < count.size(); i++)
//         //     cout<<count[i]<<" ";
//         // cout<<endl;
        
//         if(count[4]>=3)
//             cout<<"YES"<<endl;
//         else    
//             cout<<"NO"<<endl;
//     }
//     return 0;
// }