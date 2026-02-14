// #include <math.h>
// #include <stdio.h>

// #define lev(n) (n % 4 == 0 && (n % 100 != 0 || n % 400 == 0))

// int main(void)
// {
//     int y, m, d, i, s;
//     int month[2][13] = {
//         {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},
//         {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
//     };

//     while (scanf("%d/%d/%d", &y, &m, &d) != EOF)
//     {
//         for (s = 0, i = 1 ; i < m ; i++)
//             s += month[lev(y)][i];
//         s += d;
//         printf("%d\n", s);
//     }

//     return 0;
// }
			
// #include<iostream>
// using namespace std;

// int compute(string& date,vector<int>& mounths)
// {

//     string year,mounth,day;
//     int num=0;
//     int flag=0;//闰年标志
//     int i=0;


//     while(date[i]!='/')
//     {
//         year+=date[i];
//         i++;
//     }
//     int yearint=stoi(year);
//     i++;//跳过'/'

//     while(date[i]!='/')
//     {
//         mounth+=date[i];
//         i++;
//     }
//     int mounthint=int(stoi(mounth));
//     i++;//跳过'/'

//     while(i<date.length())  
//     {
//         day+=date[i];
//         i++;
//     }
//     int dayint=stoi(day);

//     //判断闰年
//     if((yearint%400==0 ||(yearint%4==0 && yearint%100!=0)))
//         flag=1;
    
//     //计算天数
//     for(int j=0;j<mounthint-1;j++)
//         num+=mounths[j];
//     if(mounthint>2 && flag==1)
//         num+=1;

//     num+=dayint;
//     return num;
// }

// int main()
// {
//     vector<int> mounths(12);
//     mounths = {31,28,31,30,31,30,31,31,30,31,30,31};

//     string date;
//     while(cin>>date)
//     {
//         cout<<compute(date,mounths)<<endl;
//     }


//     return 0;
// }