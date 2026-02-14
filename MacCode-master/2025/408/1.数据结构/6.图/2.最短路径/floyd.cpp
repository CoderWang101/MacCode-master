#include <iostream>
#include <climits> // 用于定义INF（无穷大）

#define INF INT_MAX // 定义一个大值表示无穷大

using namespace std;

// 函数声明
// void floyd_warshall(int n, int distance[][n]);

/**
 * @brief 使用Floyd-Warshall算法计算图中所有节点之间的最短路径
 * @param n 节点的数量
 * @param distance 距离矩阵，distance[i][j]表示节点i到节点j的直接距离
 */
void floyd_warshall(int n, int distance[][n])
{
    // 通过中间节点k逐步更新距离矩阵
    for (int k = 0; k < n; ++k)
    { // 中间节点k
        for (int i = 0; i < n; ++i)
        { // 起点i
            for (int j = 0; j < n; ++j)
            { // 终点j
                // 检查是否可以通过k节点来缩短i到j的路径
                if (distance[i][k] + distance[k][j] < distance[i][j])
                    distance[i][j] = distance[i][k] + distance[k][j];
            }
        }
    }
}

int main()
{
    // 定义图的节点数
    const int n = 4; // 假设图有4个节点：0, 1, 2, 3

    // 初始化距离矩阵
    int distance[n][n] = {
        {0, 5, INF, 10},
        {5, 0, 3, INF},
        {INF, 3, 0, 1},
        {10, INF, 1, 0}};

    // 调用Floyd-Warshall算法
    floyd_warshall(n, distance);

    // 输出结果
    cout << "所有节点之间的最短距离：" << endl;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (distance[i][j] == INF)
                cout << "INF ";
            else
                cout << distance[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
