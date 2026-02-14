def max_load_items(items, capacity):
    # 对集装箱按质量进行排序
    sorted_items = sorted(items)
    
    total_weight = 0
    selected_items = []
    
    # 装载集装箱
    for item in sorted_items:
        if total_weight + item <= capacity:
            total_weight += item
            selected_items.append(item)
        else:
            break
    
    return selected_items

# 测试数据
items = {1: 8, 2: 4, 3: 2, 4: 5, 5: 7}
capacity = 15

# 计算能够放入货轮的物品编号
selected_items = max_load_items(list(items.values()), capacity)
selected_item_ids = [item_id for item_id, weight in items.items() if weight in selected_items]

print("能够放入货轮的物品编号:", selected_item_ids)