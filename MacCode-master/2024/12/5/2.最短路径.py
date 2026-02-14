import sys

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    # 初始化距离矩阵
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # 计算最短路径
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def print_shortest_paths(dist):
    n = len(dist)
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print(f"从节点 {i+1} 到节点 {j+1} 不可达", end="\t")
            else:
                print(f"从节点 {i+1} 到节点 {j+1} 的最短路径为 {dist[i][j]}", end="\t")
        print()

# 示例有向权网
graph = [
    [0, 2, 6, 4],
    [0, 0, 3, 0],
    [7, 0, 0, 1],
    [5, 0, 12, 0]
]

# 计算并输出最短路径
dist = floyd_warshall(graph)
print_shortest_paths(dist)