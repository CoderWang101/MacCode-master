// #include<iostream>
// using namespace std;

// void qsort(int arr[],int l,int r)
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
//     int n;
//     cout<<"=====请输入数字个数：======"<<endl;
//     cin>>n;
//     int arr[n];

//     cout<<"====请输入数字：======="<<endl;
//     for(int i=0;i<n;i++)
//         cin>>arr[i];

//     qsort(arr,0,n-1);

//     cout<<"排序后的数字为："<<endl;
//     for(int i=0;i<n;i++)
//         cout<<arr[i]<<" ";
//     cout<<endl;


//     return 0;
// }