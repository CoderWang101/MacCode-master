// //AH,AM,AS,BH,BM,BS
// #include<iostream>
// using namespace std;

// int main()
// {
//     int n;
//     cin>>n;
//     cin.ignore();//忽略换行符
//     while (n--)
//     {
//         int ah,am,as,bh,bm,bs;
//         cin>>ah>>am>>as>>bh>>bm>>bs;
//         int sumh=0,summ=0,sums=0;

//         sums=as+bs;
//         if(sums>=60)
//         {
//             sums-=60;
//             summ++;
//         }
//         summ+=am+bm;
//         if(summ>=60)
//         {
//             summ-=60;
//             sumh++;
//         }
//         sumh+=ah+bh;
//         cout<<sumh<<" "<<summ<<" "<<sums<<endl;
//     }
    

//     return 0;
// }