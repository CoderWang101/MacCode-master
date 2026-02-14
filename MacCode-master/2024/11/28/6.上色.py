def is_safe(v, graph, color, c):
    # 检查是否可以将颜色c分配给顶点v
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    # 如果所有顶点都已着色，返回True
    if v == len(graph):
        return True
    
    # 尝试不同的颜色
    for c in range(1, m + 1):
        if is_safe(v, graph, color, c):
            color[v] = c
            # 递归尝试为下一个顶点着色
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            # 如果当前颜色c不能得到有效解，回溯
            color[v] = 0
    
    return False

def graph_coloring(graph, m):
    # 初始化颜色列表
    color = [0] * len(graph)
    
    # 调用回溯方法
    if not graph_coloring_util(graph, m, color, 0):
        print("无法为图着色")
        return False
    
    # 输出结果
    print("图的着色方案:")
    for i in range(len(graph)):
        print(f"顶点 {i} 的颜色: {color[i]}")
    return True

# 测试数据：4顶点图的邻接矩阵
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
m = 3  # 3种颜色

# 进行图的着色
graph_coloring(graph, m)