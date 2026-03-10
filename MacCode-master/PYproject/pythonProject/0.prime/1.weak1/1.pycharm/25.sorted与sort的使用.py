def sorted_dict_more():
    student = [
        {"name": "张三", "age": 18},
        {"name": "李四", "age": 19},
        {"name": "王五", "age": 20},
        {"name": "赵六", "age": 18},
    ]
    #   按年龄降序排列,如果年龄相同,则按姓名升序排列 key=lambda x: (x["age"], x["name"])
    sorted_student = sorted(student, key=lambda x: (x["age"], x["name"]), reverse=True)
    print(sorted_student)

def sorted_object():
    student=[
        {"name": "张三", "age": 18,"score":90},
        {"name": "李四", "age": 19,"score":80},
        {"name": "王五", "age": 20,"score":70},
        {"name": "赵六", "age": 18,"score":60},
    ]
    #转换
    # 定义一个简单的 Student 类(class最好不要定义到函数内部)
    class Student:
        def __init__(self, name, age, score):
            self.name = name
            self.age = age
            self.score = score

        def __repr__(self):
            return f"Student(name={self.name!r}, age={self.age}, score={self.score})'\n'"
    '''
    1. 设计目标不同(__repr__)
        方法	面向对象	目标	示例
        __repr__	开发者	精确、无歧义,调试时看到对象“真实身份”	datetime.date(2026, 2, 13)
        __str__	最终用户	美观、易读,print() 时呈现友好格式	2026-02-13
    ''' 

    students = [Student(**s) for s in student]#将字典转换为对象
    
    #按分数降序排列
    sorted_student=sorted(students,key=lambda x:x.score,reverse=True)
    print(sorted_student)

if __name__ == "__main__":
    # sorted_dict_more()
    sorted_object()
