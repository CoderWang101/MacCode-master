import os


class ReadFile:
    """只读模式 'r' - 文件必须存在"""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        """读取全部内容"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def readlines(self):
        """按行读取"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return f.readlines()


class WriteFile:
    """只写模式 'w' - 文件不存在则创建，存在则清空"""

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, content):
        """覆盖写入字符串"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def writelines(self, lines):
        """写入多行"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)


class AppendFile:
    """追加模式 'a' - 文件不存在则创建，写入追加到末尾"""

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, content):
        """追加写入字符串"""
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.write(content)

    def writelines(self, lines):
        """追加多行"""
        with open(self.filepath, 'a', encoding='utf-8') as f:
            f.writelines(lines)


class ReadWriteFile:
    """读写模式 'r+' - 文件必须存在，可读可写，写入从开头覆盖"""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        """读取全部内容"""
        with open(self.filepath, 'r+', encoding='utf-8') as f:
            return f.read()

    def write(self, content):
        """写入内容（从文件开头覆盖）"""
        with open(self.filepath, 'r+', encoding='utf-8') as f:
            f.write(content)

    def append(self, content):
        """移动到末尾再写入（实现追加效果）"""
        with open(self.filepath, 'r+', encoding='utf-8') as f:
            f.seek(0, os.SEEK_END)  # 指针移至末尾
            f.write(content)


class ExclusiveFile:
    """独占创建模式 'x' - 文件必须不存在，创建后写入"""

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, content):
        """写入内容，若文件已存在则抛出 FileExistsError"""
        with open(self.filepath, 'x', encoding='utf-8') as f:
            f.write(content)


class BinaryReadFile:
    """二进制只读 'rb' - 用于图片、音频等"""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, 'rb') as f:
            return f.read()


class BinaryWriteFile:
    """二进制只写 'wb' - 清空/创建文件"""

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, data):
        with open(self.filepath, 'wb') as f:
            f.write(data)
