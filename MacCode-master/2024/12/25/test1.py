# 列出每个课程的所有三人组名单。三人组是指这样的三个人，其中第一个人的成绩是n的话，
# 则第二、第三个人的成绩分别是n+1和n+2。
import pymongo as mg    # 引入pymongo包

uri = 'mongodb://fox:fox@192.168.154.128:27017'
client = mg.MongoClient(uri)    # 创建一个Mongo客户端
db = client.get_database('mydb')
myscores = db.get_collection('myscores')

aggs = myscores.aggregate([
    {
        "$lookup": {
             "from": "mycoll",
             "localField": "student_id",
              "foreignField": "_id",
              "as": "student"
          }
    },
    {
        "$unwind": "$student"
    }, {
        "$project": {
             "student_id": 1,
              "course": 1,
               "score": 1,
               "name": "$student.name"
         }
    },
    {
        "$facet": {
            "first": [],
            "second": [],
            "third": []
        }
    },{
        "$unwind": "$first"
    },{
        "$unwind": "$second"
    },{
        "$unwind": "$third"
    }
    ,{
        "$match": {
            "$expr":{
                "$and": [
                    {"$eq": ["$first.course", "$second.course"]},
                    {"$eq": ["$first.course", "$third.course"]},
                    {"$eq": [{"$add":["$first.score",1]},"$second.score"]},
                    {"$eq": [{"$add":["$second.score",1]}, "$third.score"]}
                ]
            }
        }
    },
    {
        "$sort": {"first.course": 1}
    }

])

# num = 0
# for agg in aggs:
#     print(agg)
#     num += 1
# print(num)

# for agg in aggs:
#     print(agg)

for agg in aggs:
    print(agg["first"]["course"])
    print("\t第一个学生",agg["first"]["name"],agg["first"]["score"],
          "第二个学生",agg["second"]["name"], agg["second"]["score"], "第三个学生", 
          agg["third"]["name"], agg["third"]["score"])

