# def backtrack(state):
#     if is_solution(state):
#         # 找到一个解，处理解
#         process_solution(state)
#     else:
#         for choice in choices(state):
#             if is_valid(state, choice):
#                 make_choice(state, choice)
#                 backtrack(state)
#                 undo_choice(state, choice)  # 回溯

# 判断当前位置是否安全，即是否可以放置皇后
def is_safe(board, row, col):
    """
    检查在(row, col)位置放置皇后是否安全。
    皇后不能在同一行、同一列或同一对角线上。
    
    :param board: 当前棋盘状态
    :param row: 当前要放置皇后的行
    :param col: 当前要放置皇后的列
    :return: True 如果安全，False 如果不安全
    """

    # 1. 检查同一列上是否有皇后
    for i in range(row):  # 遍历当前行之前的所有行
        if board[i][col] == 1:  # 如果同一列上有皇后
            return False  # 不安全，返回 False

    # 2. 检查左上对角线
    # 从当前位置 (row, col) 向左上方遍历
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:  # 如果左上对角线有皇后
            return False  # 不安全，返回 False

    # 3. 检查右上对角线
    # 从当前位置 (row, col) 向右上方遍历
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:  # 如果右上对角线有皇后
            return False  # 不安全，返回 False

    # 如果通过了所有检查，说明该位置安全
    return True

# 递归函数，尝试解决 N 皇后问题
def solve_n_queens_util(board, row):
    """
    递归函数，尝试在棋盘的 row 行中放置皇后。
    
    :param board: 当前棋盘状态
    :param row: 当前要放置皇后的行
    :return: 无需返回值，找到解时打印棋盘
    """

    # 1. 如果已经放置到最后一行，说明找到了一个解
    if row == len(board):
        print_board(board)  # 打印当前棋盘状态
        return True  # 返回 True 表示找到一个解

    # 2. 遍历当前行的每一列，尝试放置皇后
    for col in range(len(board)):
        # 检查当前位置 (row, col) 是否安全
        if is_safe(board, row, col):
            # 如果安全，在当前位置放置皇后
            board[row][col] = 1  # 1 表示放置皇后

            # 递归调用，尝试在下一行放置皇后
            solve_n_queens_util(board, row + 1)

            # 如果上面的递归没有找到解，回溯，撤销当前选择
            board[row][col] = 0  # 0 表示撤销皇后
        # 注意：这里没有返回值，因为我们需要尝试所有可能的列

# 主函数，初始化棋盘并调用递归函数
def solve_n_queens(n):
    """
    主函数，初始化 8x8 棋盘并调用递归函数。
    
    :param n: 棋盘大小，即 N 皇后问题的 N
    :return: 无需返回值
    """
    # 初始化一个 n x n 的棋盘，所有位置初始值为 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    # 调用递归函数，从第一行开始尝试
    solve_n_queens_util(board, 0)
    
# 辅助函数，打印棋盘
def print_board(board):
    """
    打印当前棋盘状态，Q 表示皇后，. 表示空位。
    
    :param board: 当前棋盘状态
    :return: 无需返回值
    """

    # 遍历棋盘的每一行
    for row in board:
        # 打印当前行的状态
        # 将 1 替换为 Q，0 替换为 .
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()  # 打印空行，分隔不同的解

# 调用函数
solve_n_queens(8)                