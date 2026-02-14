#include <iostream>
using namespace std;
int n, e, s;// n个顶点，e条边，s是起点
const int inf = 0x7fffff;
int dis[101];        // 最短距离表
int cheak[101];      // 标记访问到的最小点
int graph[101][101]; // 记录路径i->j有路径

void dij()
{
    // 1.初始化
    for (auto &val : dis)
        val = inf; // 初始无穷大

    // 2.输入 领接表
    for (int i = 1; i <= e; i++)
    {
        int head, tail, val;
        cin >> head >> tail >> val;
        graph[head][tail] = val;
    }
    // 输入起点
    cin >> s;
    dis[s] = 0;
    for (int i = 1; i <= n; i++)
    {
        int min_d = inf; // 到节点最小距离
        int min_n;       //(最小)该节点
        // 1.检查,寻找当前未访问的距离最近的节点
        for (int j = 1; j <= n; j++)
        {
            // 于寻找当前未访问节点中距离起点最近的那个节点。
            if (dis[j] < min_d && cheak[i] == 0)
            {
                min_d = dis[j];
                min_n = j;
            }
        }

        cheak[min_d] = 1; // 已访问

        // 2.计算值,用该节点更新邻居节点的距离
        for (int j = 1; j <= n; j++)
            // 存在该路径 且 当前距离小于记录距离
            if (graph[min_n][j] > 0 &&
                graph[min_n][j] + min_d < dis[j])
                dis[j] = graph[min_n][j] + min_d; // 更新最小距离
    }
    for (auto val : dis)
        cout << val << endl;
}

int main()
{
    dij();

    return 0;
}