# 生成式
num_list = [i for i in range(1, 10) if i % 2 == 0]
print(num_list)
# 有else要写前面
num_list2 = [i if i % 2 == 0 else i ** 2 for i in range(1, 10)]
print(num_list2)
print('-' * 50)

fruits=['apple', 'orange', 'pear', 'pineapple', 'banana']
dict1={}

for key,value in enumerate(fruits):
    dict1[key] = value
print(dict1)