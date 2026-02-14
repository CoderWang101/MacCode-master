#include <iostream>
#include <vector>
#include <climits> // 用于INT_MAX表示无穷大

using namespace std;

// 定义图的顶点数
const int V = 4;

// 初始化图的邻接矩阵
void initializeGraph(vector<vector<int> > &graph)
{
    // 初始化为无穷大（INT_MAX表示没有直接边）
    for (int i = 0; i < V; ++i)
        for (int j = 0; j < V; ++j)
            graph[i][j] = INT_MAX;

    // 设置顶点到自身的距离为0
    for (int i = 0; i < V; ++i)
        graph[i][i] = 0;

    // 设置其他顶点之间的距离（示例）
    // 例如，顶点0到顶点1的距离为5，顶点1到顶点2的距离为3，等等
    graph[0][1] = 5;
    graph[0][3] = 10;
    graph[1][2] = 3;
    graph[2][3] = 1;
}

// 打印图的邻接矩阵
void printGraph(const vector<vector<int> > &graph)
{
    cout << "图的邻接矩阵：" << endl;
    for (int i = 0; i < V; ++i)
    {
        for (int j = 0; j < V; ++j)
        {
            if (graph[i][j] == INT_MAX)
                cout << "∞ ";
            else
                cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

// Floyd-Warshall算法实现
void floydWarshall(vector<vector<int> > &graph, vector<vector<int> > &path)
{
    // 初始化路径矩阵：path[i][j]表示从i到j的最短路径经过的中间顶点
    for (int i = 0; i < V; ++i)
        for (int j = 0; j < V; ++j)
            path[i][j] = -1; // 初始时，没有中间顶点

    // 外层循环：枚举中间顶点k
    for (int k = 0; k < V; ++k)
    {
        // 中层循环：枚举起点i
        for (int i = 0; i < V; ++i)
        {
            // 内层循环：枚举终点j
            for (int j = 0; j < V; ++j)
            {
                // 如果通过k可以使i到j的路径更短
                if (graph[i][k] != INT_MAX && graph[k][j] != INT_MAX && graph[i][j] > graph[i][k] + graph[k][j])
                {
                    // 更新距离矩阵
                    graph[i][j] = graph[i][k] + graph[k][j];
                    // 更新路径矩阵：记录中间顶点k
                    path[i][j] = k;
                }
            }
        }
    }
}

// 打印路径矩阵
void printPath(const vector<vector<int> > &path)
{
    cout << "最短路径矩阵：" << endl;
    for (int i = 0; i < V; ++i)
    {
        for (int j = 0; j < V; ++j)
        {
            if (i == j)
            {
                cout << " - ";
                continue;
            }
            if (path[i][j] == -1)
                cout << "无 ";
            else
                cout << path[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    // 初始化图的邻接矩阵
    vector<vector<int> > graph(V, vector<int>(V));
    initializeGraph(graph);

    // 初始化路径矩阵
    vector<vector<int> > path(V, vector<int>(V));

    // 打印初始图
    printGraph(graph);

    // 运行Floyd-Warshall算法
    floydWarshall(graph, path);

    // 打印最终结果
    cout << endl
         << "最短路径矩阵：" << endl;
    printGraph(graph);

    // 打印路径矩阵
    cout << endl;
    printPath(path);

    return 0;
}