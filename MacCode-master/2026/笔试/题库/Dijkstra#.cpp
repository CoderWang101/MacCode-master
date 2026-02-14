#include <iostream>
using namespace std;
int n, e, s; // n个顶点，e条边，s是起点
const int inf = 0x7fffff;
int dis[101];        // dis[i]起点到i的最短距离
int cheak[101];      // 标记是否找到
int graph[101][101]; // 记录路径i->j有路径

int main()
{
    for (int i = 1; i <= 100; i++)
        dis[i] = inf; // 初始无穷大

    cin >> n >> e;
    for (int i = 1; i <= e; i++)
    { // 邻接矩阵存储
        int a, b, c;
        cin >> a >> b >> c; // a->b distance=c
        graph[a][b] = c;
    }

    cin >> s;   // 起点
    dis[s] = 0; // 起点到起点不需要带价

    for (int i = 1; i <= n; i++) // n个节点
    {
        // 1.检查,找到当前节点相连路径最小值
        // 寻找当前未访问的距离最近的节点
        int minn = inf, minx; // minn:最小距离, minx记录该节点
        for (int j = 1; j <= n; j++)
        {
            if (dis[j] < minn && cheak[j] == 0)
            { // 寻找当前未访问节点中距离起点最近的那个节点
                minn = dis[j];
                minx = j; // 记录当前节点
            }
        }
        cheak[minx] = 1; // 标记到达的最小点
        // 2.更新值
        // 用该节点更新邻居节点的距离
        for (int j = 1; j <= n; j++)
            // 更新以最小距离点最为中转点的最小距离
            if (graph[minx][j] > 0)
                if (minn + graph[minx][j] < dis[j]) // 检查是否小于最小距离
                    dis[j] = minn + graph[minx][j];
    }
    for (int i = 1; i <= n; i++) // 打印最短距离
        cout << dis[i] << " ";
    return 0;
}