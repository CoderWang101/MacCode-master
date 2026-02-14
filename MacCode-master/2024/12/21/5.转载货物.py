class Thing:
    def __init__(self,No,Wi):
        self.No = No
        self.Wi = Wi

items1=Thing(1,8)
items2=Thing(2,4)
items3=Thing(3,2)
items4=Thing(4,5)
items5=Thing(5,7)

items=[items1,items2,items3,items4,items5]

for i in range(len(items)):
    for j in range(len(items)-1-i):
        if items[j].Wi > items[j+1].Wi:
            items[j],items[j+1]=items[j+1],items[j]
            
sum_w=0
total_w=12
print("以下是装载的物品编号：")

for i in range(len(items)):
    if sum_w+items[i].Wi<=total_w:
        print(items[i].No)
        sum_w+=items[i].Wi
        