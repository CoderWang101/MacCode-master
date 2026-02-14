from pymongo import MongoClient
# 连接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
pipeline = [
    # 阶段1: 将 myscores 按 student_id 分组，并计算总成绩和平均成绩
    {"$group": {"_id": "$student_id","total_score": {"$sum": "$score"},
                "avg_score": {"$avg": "$score"},
                "courses": {"$push": "$course"}}},
    # 阶段2: 连接 mycoll 集合，获取学生年龄
    {"$lookup": {"from": "mycoll","localField": "_id","foreignField": "_id",
                "as": "student_info"}},
    # 阶段3: 展开 student_info 数组
    {"$unwind": "$student_info"},
    # 阶段4: 投影需要的字段，并包含年龄
    {"$project": {"student_id": "$_id","age": "$student_info.age","avg_score": 1}},
    # 阶段5: 按年龄分组，并在每个年龄组内按平均成绩排序
    {"$sort": {
            "age": 1,  # 按年龄升序，以便相同年龄在一起
            "avg_score": -1  # 每个年龄组内按平均成绩降序
        }
    },
    # 阶段6: 按年龄分组，并在每个年龄组内排序
    {"$group": {
            "_id": "$age",
            "students": {
                "$push": {
                    "student_id": "$student_id",
                    "avg_score": "$avg_score"}}}}
]

# 执行聚合操作
result = db['myscores'].aggregate(pipeline)

# 打印结果
for res in result:
    print(f"Age: {res['_id']}")
    for student in res['students']:
        print(f"  Student ID: {student['student_id']}, Average Score: {student['avg_score']}")