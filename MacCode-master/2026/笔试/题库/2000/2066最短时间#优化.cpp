// // 超级源点方法
// // 添加虚拟节点0，添加边 (0, sᵢ) 权重为0
// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// // 定义常量
// const int INF = 0x7fffff; // 定义无穷大值，表示不可达
// const int MAXN = 1001;    // 最大城市数，题目中城市编号不超过1000

// // 全局变量声明
// int graph[MAXN][MAXN]; // 邻接矩阵存储图，graph[i][j]表示城市i到城市j的时间
// int dis[MAXN];         // 存储从起点到每个城市的最短距离
// bool visited[MAXN];    // 标记数组，记录节点是否已确定最短路径
// int maxCity = 0;       // 记录图中最大的城市编号

// /**
//  * 初始化图的邻接矩阵
//  * 将所有权重初始化为无穷大（INF）
//  * 将对角线（自己到自己的距离）初始化为0
//  */
// void initGraph()
// {
//     for (int i = 0; i < MAXN; i++)
//     {
//         for (int j = 0; j < MAXN; j++)
//             graph[i][j] = INF; // 初始认为所有城市之间都不可达
//         graph[i][i] = 0;       // 自己到自己的距离为0
//     }
// }

// /**
//  * Dijkstra最短路径算法
//  * @param start 起点城市编号
//  * @param n 图中最大城市编号
//  *
//  * 算法步骤：
//  * 1. 初始化距离数组和访问标记
//  * 2. 设置起点距离为0
//  * 3. 重复n+1次（因为有0号超级源点）：
//  *    a. 从未访问节点中找到距离最小的节点
//  *    b. 标记该节点已访问
//  *    c. 通过该节点更新其相邻节点的最短距离
//  */
// void dijkstra(int start, int n)
// {
//     // 1. 初始化阶段
//     for (int i = 0; i <= n; i++)
//     {
//         dis[i] = INF;       // 初始距离设为无穷大
//         visited[i] = false; // 所有节点都未访问
//     }
//     dis[start] = 0; // 起点到自身的距离为0

//     // 2. 主循环，处理每个节点
//     for (int i = 0; i <= n; i++)
//     {
//         int minDist = INF; // 当前找到的最小距离
//         int u = -1;        // 对应的节点编号

//         // 3. 寻找当前未访问节点中距离最小的节点
//         for (int j = 0; j <= n; j++)
//         {
//             // 如果节点j未访问且距离更小，则更新
//             if (!visited[j] && dis[j] < minDist)
//             {
//                 minDist = dis[j];
//                 u = j; // 记录最小距离的节点
//             }
//         }

//         // 如果找不到这样的节点，说明所有可达节点都已处理
//         if (u == -1)
//             break;

//         visited[u] = true; // 标记节点u为已访问，最短路径已确定

//         // 4. 松弛操作：通过节点u更新其相邻节点的最短距离
//         for (int v = 0; v <= n; v++)
//         {
//             // 条件1：节点u到v有边（距离小于INF）
//             // 条件2：节点v未被访问
//             if (graph[u][v] < INF && !visited[v])
//                 // 如果通过u到v的距离比当前记录的距离更短，则更新
//                 if (dis[u] + graph[u][v] < dis[v])
//                     dis[v] = dis[u] + graph[u][v];
//         }
//     }
// }

// /**
//  * 主解题函数
//  * 处理多组输入数据，直到输入结束
//  */
// void solve()
// {
//     int T, S, D; // T: 道路数, S: 相邻城市数, D: 目的地数

//     // 循环读取每组测试数据
//     while (cin >> T >> S >> D)
//     {
//         // 1. 初始化图
//         initGraph();
//         maxCity = 0; // 重置最大城市编号

//         // 2. 读取道路信息
//         for (int i = 0; i < T; i++)
//         {
//             int a, b, time;
//             cin >> a >> b >> time;

//             // 处理重边：取最短的时间
//             // 因为可能有多个a到b的道路，我们只保留最短的那个
//             if (time < graph[a][b])
//             {
//                 graph[a][b] = time; // a到b的时间
//                 graph[b][a] = time; // b到a的时间（无向图）
//             }

//             // 更新最大城市编号
//             maxCity = max(maxCity, max(a, b));
//         }

//         // 3. 读取草儿家相邻的城市（起点城市）
//         vector<int> startCities(S);
//         for (int i = 0; i < S; i++)
//         {
//             cin >> startCities[i];
//             maxCity = max(maxCity, startCities[i]); // 更新最大城市编号
//         }

//         // 4. 读取草儿想去的目的地
//         vector<int> destCities(D);
//         for (int i = 0; i < D; i++)
//         {
//             cin >> destCities[i];
//             maxCity = max(maxCity, destCities[i]); // 更新最大城市编号
//         }

//         // 5. 关键优化：添加超级源点
//         // 添加虚拟节点0表示草儿的家，连接到所有起点城市，权重为0
//         for (int i = 0; i < S; i++)
//         {
//             graph[0][startCities[i]] = 0; // 从家到相邻城市的时间为0
//             graph[startCities[i]][0] = 0; // 无向图，所以反向也要设置
//         }

//         // 6. 运行Dijkstra算法，从超级源点0开始
//         // 只需运行一次，而不是为每个起点运行S次
//         dijkstra(0, maxCity);

//         // 7. 计算答案：从所有目的地中找到最短的距离
//         int minTime = INF;
//         for (int i = 0; i < D; i++)
//         {
//             // 注意：这里可能会访问到INF，表示不可达
//             if (dis[destCities[i]] < minTime)
//                 minTime = dis[destCities[i]];
//         }

//         // 8. 输出结果
//         cout << minTime << endl;
//     }
// }

// /**
//  * 主函数
//  * 程序入口点
//  */
// int main()
// {
//     // 调用解题函数
//     solve();
//     return 0;
// }