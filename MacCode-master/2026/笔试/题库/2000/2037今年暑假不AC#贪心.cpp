// #include <iostream>
// using namespace std;

// struct schedule
// {
//     int start;
//     int end;
// };

// bool compare(schedule &a, schedule &b)
// {
//     return a.end < b.end;
// }

// int main()
// {
//     int n;
//     cin >> n;
//     cin.ignore();

//     vector<schedule> program(n);
//     for (int i = 0; i < n; i++)
//     {
//         cin >> program[i].start>>program[i].end;
//     }
//     sort(program.begin(), program.end(), compare);//按照结束时间排序

//     int select=0;//选择个数
//     int endtime=0;//最早结束时间
//     for (int i = 0; i < n; i++)
//     {
//         if(program[i].start>=endtime)//开始时间在当前时间之后
//         {
//             select++;
//             endtime=program[i].end;
//         }
//     }
//     cout<<select<<endl;

//     return 0;
// }