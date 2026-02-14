def calculate_average(numbers):
    assert len(numbers) > 0, '列表为空'
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    try:
        a = calculate_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print(a)
        b = calculate_average([])
        print(b)
    except Exception as e:
        print(e)


