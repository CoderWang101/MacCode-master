def count_graph_coloring(graph,m):
    n=len(graph)
    colors=[-1]*n
    
    count=0#记录着色数量
    
    def is_valid(colors,vertex,color):
        for i in range(n):
            if graph[vertex][i] and colors[i]==color:
                return False
        return True
    
    def backtrack(colors,vertex):
        nonlocal count #声明count为非局部变量
        if vertex==n:
            count+=1
            print(colors)

            return
        for color in range(m):
            if is_valid(colors,vertex,color):
                colors[vertex]=color
                backtrack(colors,vertex+1)
                colors[vertex]-=1
    backtrack(colors,0)
    return count

graph=[
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0]
]
m=3

print("着色方案数量：")
color_count=count_graph_coloring(graph,m)

print(f"着色可行解的个数为:{color_count}")  # 输出结果