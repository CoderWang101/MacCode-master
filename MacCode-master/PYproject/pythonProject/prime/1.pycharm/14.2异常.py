def divide(a, b):
    try:
        result = a / b
        print(f"a/b={result}")
    except Exception as e:
        print(f'Exception: {e}')
        # 从异常对象中提取并打印异常发生的具体位置信息（文件名和行号）
        print(e.__traceback__.tb_lineno)
        print(e.__traceback__.tb_frame.f_globals['__file__'])
    else:
        print("correct")
        return result
    finally:
        print("是否有异常都会执行\n")  # 上面有return也依旧会执行


divide(2, 3)
divide(1, 0)
divide(0, 1)
