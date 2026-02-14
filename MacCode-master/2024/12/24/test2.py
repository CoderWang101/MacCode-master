import pymongo as mg

uri = 'mongodb://root:123456@101.133.160.33:27017'
client = mg.MongoClient(uri)
db = client.get_database('mydb')
mycoll = db.get_collection('mycoll')
aggs = mycoll.aggregate([{
    "$facet": {
        "f1": [{"$match": {"age": 23}}],
        "f2": [{"$match": {"age": 24}}]
    }
}])
for agg in aggs:
    print(agg)

