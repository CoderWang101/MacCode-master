from pymongo import MongoClient

# 连接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']

pipeline = [
    # 阶段1: 将 myscores 按 student_id 分组，并计算总成绩和平均成绩
    {"$group": {"_id": "$student_id", 
                "total_score": {"$sum": "$score"}, 
                "c1_score": {"$first": "$score"},  # 假设 C1 是第一个成绩
                "c2_score": {"$last": "$score"},   # 假设 C2 是最后一个成绩
                "courses": {"$push": "$course"}}},
    # 阶段2: 连接 mycoll 集合，获取学生年龄
    {"$lookup": {"from": "mycoll", 
                 "localField": "_id", 
                 "foreignField": "_id", 
                 "as": "student_info"}},
    # 阶段3: 展开 student_info 数组
    {"$unwind": "$student_info"},
    # 阶段4: 投影需要的字段，并包含年龄
    {"$project": {"student_id": "$_id", 
                  "age": "$student_info.age", 
                  "total_score": 1, 
                  "c1_score": 1, 
                  "c2_score": 1}},
    # 阶段5: 按总成绩、C1、C2 成绩排序
    {"$sort": {
        "total_score": -1,  # 按总成绩降序
        "c1_score": -1,     # 总成绩相同的，按 C1 成绩降序
        "c2_score": -1      # C1 成绩相同的，按 C2 成绩降序
    }}
]

# 执行聚合操作
result = db['myscores'].aggregate(pipeline)

# 打印结果
for res in result:
    print(f"Student ID: {res['student_id']}, Total Score: {res['total_score']}, C1 Score: {res['c1_score']}, C2 Score: {res['c2_score']}")