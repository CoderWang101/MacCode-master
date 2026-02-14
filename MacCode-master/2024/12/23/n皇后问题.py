def backtrack(row, n, state, res, cols, diags1, diags2):
    if row == n:
        res.append([list(row) for row in state])
        return
    for col in range(n):
        diag1 = row - col + n - 1#记录当前第几列
        diag2 = row + col
        if not cols[col] and not diags1[diag1] and not diags2[diag2]:
            state[row][col] = "Q"
            cols[col] = diags1[diag1] = diags2[diag2] = True
            backtrack(row + 1, n, state, res, cols, diags1, diags2)
            state[row][col] = "#"
            cols[col] = diags1[diag1] = diags2[diag2] = False

def n_queues(n):
    state = [["#" for _ in range(n)] for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)
    diags2 = [False] * (2 * n - 1)
    res = []
    backtrack(0, n, state, res, cols, diags1, diags2)
    return res

n_queues(4)
[[['#', 'Q', '#', '#'],
  ['#', '#', '#', 'Q'],
  ['Q', '#', '#', '#'],
  ['#', '#', 'Q', '#']],
 [['#', '#', 'Q', '#'],
  ['Q', '#', '#', '#'],
  ['#', '#', '#', 'Q'],
  ['#', 'Q', '#', '#']]]