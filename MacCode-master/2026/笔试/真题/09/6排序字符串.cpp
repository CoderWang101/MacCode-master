// #include <iostream>
// using namespace std;

// void qsort(string& arr,int l,int r)
// {
//     if(l>=r)
//         return ;

//     int i=l;
//     int j=r;
//     int privot=arr[l];

//     while(i<j)
//     {
//         while(i<j && arr[j]>=privot)
//             j--;
//         while(i<j && arr[i]<=privot)
//             i++;
//         if(i<j)
//             swap(arr[i],arr[j]);
//     }
//     swap(arr[l],arr[i]);
//     qsort(arr,l,i-1);
//     qsort(arr,i+1,r);
// }
// int main()
// {
//     int num;
//     cout<<"=====请输入数字个数：======"<<endl;
//     cin>>num;

//     //输入字符串
    
//     for(int i=0;i<num;i++)
//     {
//         string arr;
//         cout<<"====请输入字符串：======="<<endl;
//         cin>>arr;
//         qsort(arr,0,arr.length()-1);
//         cout<<"排序后的字符串为："<<endl;
//         cout<<arr<<endl<<endl;    
//     }
    

//     return 0;
// }