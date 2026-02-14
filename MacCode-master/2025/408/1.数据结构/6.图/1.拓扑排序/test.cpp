#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <string>
#include <set>

// 拓扑排序函数，接受一个用邻接表表示的图，返回拓扑排序后的节点序列
// 如果图中存在环，则返回一个空的向量
std::vector<std::string> topologicalSort(std::unordered_map<std::string, std::vector<std::string>> &graph)
{
    // 用于存储每个节点的入度，键为节点名，值为入度
    std::unordered_map<std::string, int> inDegree;
    // 用于收集图中所有的节点，使用 set 可自动去重
    std::set<std::string> nodes;

    // 步骤 1: 遍历邻接表，收集所有节点并初始化入度表
    // 遍历图中的每个节点及其邻接节点
    for (const auto &entry : graph)
    {
        // 将当前节点加入到 nodes 集合中
        nodes.insert(entry.first);
        // 遍历当前节点的所有邻接节点
        for (const std::string &neighbor : entry.second)
        {
            // 将邻接节点加入到 nodes 集合中
            nodes.insert(neighbor);
        }
    }

    // 初始化所有节点的入度为 0
    for (const auto &node : nodes)
    {
        inDegree[node] = 0;
    }

    // 步骤 2: 计算所有节点的入度
    // 再次遍历图中的每个节点及其邻接节点
    for (const auto &entry : graph)
    {
        // 遍历当前节点的所有邻接节点
        for (const std::string &neighbor : entry.second)
        {
            // 邻接节点的入度加 1
            ++inDegree[neighbor];
        }
    }

    // 步骤 3: 将入度为 0 的节点加入队列
    // 用于存储入度为 0 的节点，采用队列实现广度优先搜索
    std::queue<std::string> q;
    // 遍历所有节点
    for (const auto &node : nodes)
    {
        // 如果当前节点的入度为 0
        if (inDegree[node] == 0)
        {
            // 将该节点加入队列
            q.push(node);
        }
    }

    // 用于存储拓扑排序的结果
    std::vector<std::string> result;

    // 步骤 4: Kahn 算法核心过程
    // 当队列不为空时，持续进行处理
    while (!q.empty())
    {
        // 取出队列的队首节点
        std::string u = q.front();
        // 队首节点出队
        q.pop();
        // 将该节点加入到拓扑排序结果中
        result.push_back(u);

        // 遍历当前节点的所有邻居
        // 检查当前节点是否在图中存在邻接节点
        auto it = graph.find(u);
        if (it != graph.end())
        {
            // 遍历当前节点的所有邻接节点
            for (const std::string &v : it->second)
            {
                // 邻接节点的入度减 1
                --inDegree[v];
                // 如果邻接节点的入度变为 0
                if (inDegree[v] == 0)
                {
                    // 将该邻接节点加入队列
                    q.push(v);
                }
            }
        }
    }

    // 步骤 5: 检查是否存在环
    // 如果拓扑排序结果的节点数量不等于图中所有节点的数量
    if (result.size() != nodes.size())
    {
        // 说明图中存在环，返回空向量
        return {};
    }
    // 否则返回拓扑排序的结果
    return result;
}

// 主函数，用于测试拓扑排序功能
int main()
{
    // 示例 1: 有向无环图
    // 定义一个有向无环图，使用邻接表表示
    std::unordered_map<std::string, std::vector<std::string>> graph1 = {
        {"A", {"B", "C"}},
        {"B", {"D"}},
        {"C", {"D"}},
        {"D", {}}};
    // 对图 1 进行拓扑排序
    std::vector<std::string> result1 = topologicalSort(graph1);
    // 遍历拓扑排序的结果并输出
    for (const std::string &s : result1)
    {
        std::cout << s << " ";
    }
    // 可能输出 "A B C D " 或 "A C B D "

    // 示例 2: 存在环
    // 定义一个有环的有向图，使用邻接表表示
    std::unordered_map<std::string, std::vector<std::string>> graph2 = {
        {"A", {"B"}},
        {"B", {"C"}},
        {"C", {"A"}} // 形成环 A → B → C → A
    };
    // 对图 2 进行拓扑排序
    std::vector<std::string> result2 = topologicalSort(graph2);
    // 如果拓扑排序结果为空，说明图中存在环，输出 "Has Cycle"
    std::cout << std::endl
              << (result2.empty() ? "Has Cycle" : "");

    return 0;
}
