#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <climits> // 用于INT_MAX表示无穷大
#include <utility> // 用于pair

using namespace std;

void dijkstra(const map<char, vector<pair<char, int> > > &graph, char start_node)
{
    /*
    Dijkstra算法用于寻找图中从一个起点到其他所有节点的最短路径。

    参数:
        graph: 邻接表表示的图，格式为 {node: [(neighbor, weight), ...]}
        start_node: 起始节点
    */
    // 初始化所有节点的距离为无穷大
    map<char, int> distance;
    
    for (const auto &node : graph)
    {
        distance[node.first] = INT_MAX;
    }
    // 起始节点的距离设为0
    distance[start_node] = 0;

    // 优先队列，存储pair（当前距离，当前节点）
    //      队列中存储的元素类型是pair  vector作为底层容器来存储元素    小堆
    priority_queue <pair<int, char>, vector<pair<int, char> >, greater<pair<int, char> > > heap;
    heap.push(make_pair(0, start_node));//距离为0，起始节点,节点按照小堆排序

    // 记录已处理的节点
    map<char, bool> visited;
    for (const auto &node : graph)
    {
        visited[node.first] = false;
    }

    
    while (!heap.empty())
    {
        // 弹出距离最小的节点
        int current_distance = heap.top().first;
        char current_node = heap.top().second;
        heap.pop();

        // 如果当前节点已处理过，跳过
        if (visited[current_node])
        {
            continue;
        }
        // 标记为已处理
        visited[current_node] = true;

        // 遍历当前节点的所有邻居
        for (const auto &neighbor : graph.at(current_node))
        {
            char neighbor_node = neighbor.first;//邻居节点
            int weight = neighbor.second;//邻居距离

            // 计算从当前节点到邻居的总距离
            int new_distance = current_distance + weight;

            // 如果找到更短的路径，更新距离并加入队列
            if (new_distance < distance[neighbor_node])
            {
                distance[neighbor_node] = new_distance;
                heap.push(make_pair(new_distance, neighbor_node));
            }
        }
    }

    // 输出结果
    cout << "最短距离：" << endl;
    for (const auto &node : graph)
    {
        cout << "节点 " << node.first << " 的距离为 " << distance[node.first] << endl;
    }
}

int main()
{
    // 示例图：邻接表表示
    // map<char, vector<pair<char, int> > > graph = {
    //     {'A', {{'B', 1}, {'C', 4}}},
    //     {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
    //     {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
    //     {'D', {{'B', 5}, {'C', 1}}}};

    /*
    最短距离：
    节点 A 的距离为 0
    节点 B 的距离为 1
    节点 C 的距离为 3
    节点 D 的距离为 4
    */


    // 从节点 'A' 开始运行Dijkstra算法
    // dijkstra(graph, 'A');

    return 0;
}