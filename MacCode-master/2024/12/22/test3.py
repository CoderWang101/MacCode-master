import pymongo as mg    # 引入pymongo包

uri = 'mongodb://fox:fox@192.168.29.133:27017'
client = mg.MongoClient(uri)    # 创建一个Mongo客户端
db = client.get_database('mydb')
myscores = db.get_collection('myscores')

# 有mycoll和myscores集合。当前数据中，mycoll有3条数据，myscores有6条数据，每个学生考2门。

aggs = myscores.aggregate([
{
    # _id, student_id, course, score
    "$facet": {
        "sums": [{
            "$group": {
                "_id": "$student_id",
                "sum": {
                    "$sum": "$score"
                }
            }
        }],
        "c1s": [{
            "$match": {
                "$expr": {"$eq": ["$course", "C1"]}
            }
        }],
        "c2s": [{
            "$match": {
                "$expr": {"$eq": ["$course", "C2"]}
            }
        }]
    }
},
# sums:[{_id, sum}], c1s:[{_id,student_id,score,course}], c2s:[{_id,student_id,score,course}]
# sums里面是每个学生的总成绩，c1s中是课程C1的所有学生成绩，c2s是课程c2的所有学生成绩。
# 1条数据，3个顶级字段。sums、c1s、c2s都是数组类型，并且都有3个元素。
{
    "$unwind": "$sums"
}
# sums:{_id, sum}, c1s:[{_id,student_id,score,course}], c2s:[{_id,student_id,score,course}]
# 数据条数增加，sums数组中有几个元素，展开后就有几条数据。每一条数据中的c1s数据一样，c2s的数据一样
# 3条数据，3个顶级字段
,
{
    "$unwind": "$c1s"
},
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:[{_id,student_id,score,course}]
# 数据条数增加，c1s数组中有几个元素，展开后就有几条数据。每一条数据中的c2s值一样
# 9条数据，3个顶级字段。
{
    "$match": {
        "$expr": {
            "$eq": ["$sums._id", "$c1s.student_id"]
        }
    }
}
# match是过滤数据，字段名字不变。数据条数发生改变。只要$sums._id=$c1s.student_id的数据
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:[{_id,student_id,score,course}]
# 3条数据，3个顶级字段。
,
{
    "$unwind": "$c2s"
}
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:{_id,student_id,score,course}
# 数据条数增加，c2s数组中有几个元素，展开后就有几条数据。
# 9条数据，3个顶级字段。
,
{
    "$match": {
        "$expr": {
            "$eq": ["$sums._id", "$c2s.student_id"]
        }
    }
}
# match是过滤数据，字段名字不变。数据条数发生改变。只要$sums._id=$c2s.student_id的数据
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:{_id,student_id,score,course}
# 经过上面的操作，可以获取每个学生的总成绩，C1课程成绩，C2课程成绩。数据拼到一起
# 3条数据，3个顶级字段。
,
{
    "$sort": {
        "sums.sum": -1,
        "c1s.score": -1,
        "c2s.score": -1
    }
}
# 排序，数据条数，列数都不发生改变
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:{_id,student_id,score,course}
,
{
    "$lookup": {
        "from": "mycoll",
        "localField": "sums._id",
        "foreignField": "_id",
        "as": "st"
    }
},
# 为了获取到学生姓名，学生姓名在mycoll表中，所以要用lookup进行关联。关联的时候要指明关联字段。
# 关联到的学生信息以数组的方式返回给st。
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:{_id,student_id,score,course}, st:[{_id,name,age,grade}]
{
    "$unwind": "$st"
}
# sums:{_id, sum}, c1s:{_id,student_id,score,course}, c2s:{_id,student_id,score,course}, st:{_id,name,age,grade}
])

# for agg in aggs:
#     print(agg)

for agg in aggs:
    print(agg['st']['name'], agg['sums']['sum'], agg['c1s']['score'], agg['c2s']['score'])