def is_safe(board,row,col):
    #检查列(因为只在一行放一个皇后，所以只需要检查列)
    for i in range(row):
        if board[i][col]==1:
            return False
    #检查左上对角线
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    #检查右上对角线
    for i,j in zip(range(row,-1,-1),range(col,len(board))):
        if board[i][j]==1:
            return False
    return True

def solve_n_queens_util(board,row):
    #结束条件
    if row==len(board):
        print_board(board)
        return True
    #放置皇后(按行放置)
    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row][col]=1#放置皇后
            solve_n_queens_util(board,row+1)
            board[row][col]=0#回溯
            
def print_board(board):
    for row in board:
        # 将 1 替换为 Q，0 替换为 .
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()  # 打印空行，分隔不同的解
    
def solve_n_queens(n):
    # 初始化一个 n x n 的棋盘，所有位置初始值为 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    # 调用递归函数，从第一行开始尝试
    solve_n_queens_util(board, 0)
    
# 调用函数
solve_n_queens(8)  