// #include <iostream>
// #include <vector>
// #include <cstring>
// using namespace std;

// const int MAXN = 505; // 最大人数

// vector<int> graph[MAXN]; // 邻接表：graph[女生] = {男生列表}
// int match[MAXN];         // match[男生] = 匹配的女生，0表示未匹配
// bool visited[MAXN];      // 访问标记

// // 深度优先搜索寻找增广路
// bool dfs(int girl)
// {
//     // 遍历该女生所有心仪的男生
//     for (int i = 0; i < graph[girl].size(); i++)
//     {
//         int boy = graph[girl][i];
//         if (!visited[boy])
//         {
//             visited[boy] = true;
//             // 如果男生未匹配，或者 可以为已匹配的女生找到新的匹配
//             if (match[boy] == 0 || dfs(match[boy]))
//             {
//                 match[boy] = girl; // 建立匹配
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// int main()
// {
//     int K, M, N;

//     while (cin >> K && K != 0)
//     {
//         cin >> M >> N;

//         // 清空图
//         for (int i = 1; i <= M; i++)
//             graph[i].clear();

//         // 读取边
//         for (int i = 0; i < K; i++)
//         {
//             int girl, boy;
//             cin >> girl >> boy;
//             graph[girl].push_back(boy);
//         }

//         // 匈牙利算法
//         memset(match, 0, sizeof(match));//将match初始化
//         int matching = 0;

//         for (int girl = 1; girl <= M; girl++)
//         {
//             memset(visited, false, sizeof(visited));//将visited初始化
//             if (dfs(girl))
//                 matching++; // 找到新的匹配
//         }

//         cout << matching << endl;
//     }

//     return 0;
// }