import sys

print(sys.argv)
'''
> python ./prime/17.py传参.py 1 2 3
['./prime/17.py传参.py', '1', '2', '3']

'''


def read_conf():
    with open('my_conf', 'r', encoding='utf-8') as f:
        my_dict = eval(f.read())  # eval有安全风险
        print(my_dict)
        return my_dict
