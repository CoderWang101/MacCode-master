// #include <iostream>
// using namespace std;
// int graph[1001][1001];
// const int inf = 0x7fffff;
// int n, s, d;           // 路径个数 出发点个数 终点个数
// int MinDistance[1001]; // 记录最小距离
// int cheak[1001];       // 标记数组(是否访问过)
// int top = 0;           // 找到最大值城市
// int dij(int start, int destination[])
// {
//     MinDistance[start] = 0;
//     for (int i = 1; i <= top; i++)
//     {
//         int min_n, min_v = inf; // 最小值节点、最小值
//         // 寻找当前未访问节点中距离起点最近的那个节点
//         for (int j = 1; j <= top; j++)
//         {
//             if (MinDistance[j] < min_v && cheak[j] == 0)
//             {
//                 // 选中新节点(不一定)
//                 min_v = MinDistance[j];
//                 min_n = j;
//             }
//         }
//         if (min_v == inf) // 节点均不可达
//             continue;

//         cheak[min_n] = 1; // 标记新节点(确定)

//         // 更新最小节点
//         for (int j = 1; j <= top; j++)
//         {
//             // 访问新节点距离
//             if (graph[min_n][j] > 0 &&
//                 graph[min_n][j] + min_v < MinDistance[j])
//                 MinDistance[j] = graph[min_n][j] + min_v;
//         }
//     }
//     int FindMinDistance = inf;
//     for (int i = 1; i <= d; i++)
//     {
//         if (FindMinDistance > MinDistance[destination[i]])
//         {
//             FindMinDistance = MinDistance[destination[i]];
//         }
//     }
//     return FindMinDistance;
// }

// void slove()
// {
//     cin >> n >> s >> d;
//     int t = n;
//     // 初始化
//     for (auto &val : MinDistance)
//         val = inf;
//     // 创建图
//     while (t--)
//     {
//         int start, end, time;
//         cin >> start >> end >> time;
//         graph[start][end] = time;
//         graph[end][start] = time;
//         if (top < max(start, end))
//             top = max(start, end);
//     }
//     // 从1开始
//     int start[s + 1], destination[d + 1]; // 出发点、目的地
//     for (int i = 1; i <= s; i++)
//         cin >> start[i];
//     for (int i = 1; i <= d; i++)
//         cin >> destination[i];
//     // 出发点
//     vector<int> record; // 记录到达目的地的距离
//     for (int i = 1; i <= s; i++)
//     {
//         if (i != 1)
//         {
//             for (int j = 0; j <= 1000; j++)
//             {
//                 MinDistance[j] = inf;
//                 cheak[j] = 0;
//             }
//         }
//         int origin = start[i];
//         record.push_back(dij(origin, destination));
//         MinDistance[origin] = inf;
//     }
//     int min_road = inf;
//     for (auto val : record)
//         if (min_road > val)
//             min_road = val;
//     cout << min_road << endl;
// }

// int main()
// {
//     slove();
//     return 0;
// }