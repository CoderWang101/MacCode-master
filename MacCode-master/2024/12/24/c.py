import pymongo as mg    # 引入pymongo包
uri = 'mongodb://fox:fox@192.168.29.133:27017'
client = mg.MongoClient(uri)    # 创建一个Mongo客户端
db = client.get_database('mydb')
myscores = db.get_collection('myscores')
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
{
    "$unwind": "$sums"
},
{
    "$unwind": "$c1s"
},
{
    "$match": {
        "$expr": {
            "$eq": ["$sums._id", "$c1s.student_id"]
        }
    }
},
{
    "$unwind": "$c2s"
},
{
    "$match": {
        "$expr": {
            "$eq": ["$sums._id", "$c2s.student_id"]
        }
    }
},
{
    "$sort": {
        "sums.sum": -1,
        "c1s.score": -1,
        "c2s.score": -1
    }
},
{
    "$lookup": {
        "from": "mycoll",
        "localField": "sums._id",
        "foreignField": "_id",
        "as": "st"
    }
},
{
    "$unwind": "$st"
}
])

# for agg in aggs:
#     print(agg)

for agg in aggs:
    print(agg['st']['name'], agg['sums']['sum'], agg['c1s']['score'], agg['c2s']['score'])