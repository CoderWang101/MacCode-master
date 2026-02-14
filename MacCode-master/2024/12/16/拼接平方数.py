def is_square(n):
    """检查 n 是否为平方数."""
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n

def find_concatenated_squares(start, end):
    """找到区间 [start, end] 内的所有拼接平方数."""
    squares = set()
    n = 1
    while True:
        square = n * n
        if square > end:
            break
        squares.add(square)
        n += 1

    concatenated_squares = []
    for square in squares:
        if square < start:
            continue
        square_str = str(square)
        for i in range(1, len(square_str)):
            part1 = int(square_str[:i])
            part2 = int(square_str[i:])
            if part1 in squares and part2 in squares:
                if part2 == 0:
                    continue
                concatenated_squares.append(square)
                break

    return concatenated_squares

# 示例使用
start = 169
end = 10000
result = find_concatenated_squares(start, end)
print(result)