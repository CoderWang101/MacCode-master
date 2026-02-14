// #include<iostream>
// using namespace std;

// int main()
// {
//     int n;
//     //人民币一共有100元、50元、10元、5元、2元和1元六种。
//     while(cin>>n)
//     {
//         vector<int> teacher(n);
//         for (int i = 0; i < n; i++)
//             cin >> teacher[i];
//         int money[6]={100,50,10,5,2,1};
//         int count=0;
//         for(int i=0;i<n;i++)
//         {
//             int temp=teacher[i];
//             int j=0;
//             while (temp!=0)
//             {
//                 if(temp>=money[j])
//                 {
//                     temp-=money[j];
//                     count++;
//                 }
//                 else
//                     j++;
//             }
//         }
//         cout<<count<<endl;
//     }
//     return 0;
// }