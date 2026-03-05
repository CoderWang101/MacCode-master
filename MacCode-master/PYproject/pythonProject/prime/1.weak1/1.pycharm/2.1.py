# 1. split() 方法
def split_():
    # 按空格分割字符串
    text = "hello world python"
    result = text.split()
    print(result)  # ['hello', 'world', 'python']

    # 按指定字符分割
    text2 = "apple,banana,orange"
    result2 = text2.split(',')
    print(result2)  # ['apple', 'banana', 'orange']
    '''
    # 解析CSV数据
        csv_data = "John,Doe,25,USA"
        person = csv_data.split(',')
        print(f"姓: {person[1]}, 名: {person[0]}, 年龄: {person[2]}")
        
        # 解析URL路径
        url = "https://example.com/blog/python-tutorial"
        path_parts = url.split('/')
        print(path_parts)  # ['https:', '', 'example.com', 'blog', 'python-tutorial']
        
        # 提取文件扩展名
        filename = "document.pdf"
        name, extension = filename.split('.')
        print(f"文件名: {name}, 扩展名: {extension}")
    '''


# 2. join() 方法
def join_():
    # 基本用法
    # 列表连接为字符串
    words = ['hello', 'world', 'python']
    result = ' '.join(words)
    print(result)  # 'hello world python'

    # 使用不同连接符
    fruits = ['apple', 'banana', 'orange']
    result2 = ', '.join(fruits)
    print(result2)  # 'apple, banana, orange'

    # 连接数字列表（需要先转为字符串）
    numbers = [1, 2, 3, 4, 5]
    result3 = '-'.join(str(num) for num in numbers)
    print(result3)  # '1-2-3-4-5'


# splitlines() 方法
def splitlines_():
    # 多行文本分割
    text = """第一行
第二行
第三行"""

    lines = text.splitlines()
    print(lines)  # ['第一行', '第二行', '第三行']

    # 包含换行符的文本
    text2 = "line1\nline2\r\nline3"
    lines2 = text2.splitlines()
    print(lines2)  # ['line1', 'line2', 'line3']

    # 处理日志文件
    log_content = """ERROR: File not found
    WARNING: Disk space low
    INFO: Backup completed"""

    lines = log_content.splitlines()
    error_lines = [line for line in lines if line.startswith('ERROR')]
    print(f"错误行数: {len(error_lines)}")

    # 读取配置文件
    config = """host=localhost
    port=5432
    database=mydb
    username=admin"""

    config_dict = {}
    for line in config.splitlines():
        if '=' in line:
            key, value = line.split('=', 1)
            config_dict[key.strip()] = value.strip()

    print(config_dict)

    # 统计代码行数
    code = '''def hello():
        print("Hello, World!")

    def goodbye():
        print("Goodbye!")'''

    lines = code.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    print(f"总行数: {len(lines)}")
    print(f"非空行数: {len(non_empty_lines)}")


split_()
join_()
splitlines_()
