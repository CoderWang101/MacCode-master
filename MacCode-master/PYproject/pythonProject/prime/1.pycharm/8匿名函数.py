# 引用计数为0才会被删除
t1 = [1, 2, 3, 4]
t2 = t1
print("t1_id=", id(t1))  # 4341276224
print("t2_id=", id(t2))
print("delete t1")
del t1  # 在有别的引用情况下,列表无法被删除,只能删除变量名
print(t2)
print("t2_id=", id(t2))  # 4341276224
print("引用计数为0才会被删除")
