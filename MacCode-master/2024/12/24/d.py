import pymongo as pm
uri = "mongodb://fox:fox@192.168.154.128:27017"
client = pm.MongoClient(uri)
db = client.get_database("mydb")
myscores = db.get_collection('myscores')
aggs = myscores.aggregate([
    {
        "$group": {
            "_id": "$student_id",
            "avg_score": {"$avg": "$score"}
        }
    }, {
        # 查找学⽣对象
        # 输⼊字段：_id(student_id), avg_score
        "$lookup": {
            "from": "mycoll",
            "localField": "_id",
            "foreignField": "_id",
            "as": "stu"
        }
    }, {
        "$unwind": "$stu"
    }, {
        "$sort": {"avg_score": -1}
    }, {
        "$group": {
            "_id": "$stu.age",
            "sts": {
                "$push": {
                "name": "$stu.name",
                "avg_score": "$avg_score"
                }
            }
        }
    }, {
        "$sort": { "_id": 1}
    }
])
with aggs:
    for agg in aggs:
        print(agg["_id"])
        for st in agg["sts"]:
            print("\t%s\t%6.2f" % (st["name"], st["avg_score"]))

