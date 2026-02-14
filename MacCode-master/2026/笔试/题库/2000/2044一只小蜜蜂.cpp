// #include<iostream>
// using namespace std;
// //只能爬向右侧相邻的蜂房，不能反向爬行
// //是能向+1或+2方向,实际上是斐波那契
// int main()
// {
//     long febi[51]={1,1,2};
//     for (int i = 3; i < 51; i++)
//         febi[i]=febi[i-1]+febi[i-2];
//     int n;
//     cin>>n;
//     cin.ignore();
//     while (n--)
//     {
//         pair<int,int> road;
//         cin>>road.first>>road.second;
//         if(road.first>road.second)
//         {
//             cout<<"error"<<endl;
//             continue;
//         }
//         cout<<febi[road.second-road.first]<<endl;
//     }
//     return 0;
// }