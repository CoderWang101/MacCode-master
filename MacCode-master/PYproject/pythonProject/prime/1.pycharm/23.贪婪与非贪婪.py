import re

"""

"""


def use_greedy_pattern():
    text = "<div>内容1</div><div>内容2</div>"
    # 1.贪婪匹配(.*尽可能多匹配, 从第一个<div>开始, 直到最后一个</div>)
    pattern1 = r"<div>.*</div>"
    match1 = re.search(pattern1, text)
    print(match1.group())  # 输出<div>内容1</div><div>内容2</div>

    # 2.非贪婪匹配(.*?尽可能少匹配, 从第一个<div>开始, 直到第一个</div>)
    pattern2 = r"<div>.*?</div>"
    match2 = re.search(pattern2, text)
    print(match2.group())  # 输出<div>内容1</div>

def use_r():
    # 方法1：直接匹配整个路径
    pattern = r'C:\\'       # 原始字符串避免转义困扰
    ret = re.match(pattern, 'C:\\')
    print(ret.group())      # C:\
        
    print('-'*50)
    
    # 方法2：查找反斜杠并输出其所在上下文
    ret = re.search(r'\\', 'C:\\')
    if ret:
        print(ret.group())  # \


if __name__ == "__main__":
    # use_greedy_pattern()
    use_r()
