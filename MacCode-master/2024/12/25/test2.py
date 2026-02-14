import pymongo as mg    # 引入pymongo包

uri = 'mongodb://fox:fox@192.168.29.131:27017'
client = mg.MongoClient(uri)    # 创建一个Mongo客户端
db = client.get_database('mydb')
myscores = db.get_collection('myscores')

aggs = myscores.aggregate([{
    # _id, student_id, course, score
    "$sort": {"score": -1}
}, {
    "$lookup": {
        "from": "mycoll",
        "localField": "student_id",
        "foreignField": "_id",
        "as": "student"
    }
    # _id, student_id, course, score, student: [{_id, name, age, grade}]
}, {
    "$unwind": "$student"
    # _id, student_id, course, score, student: {_id, name, age, grade}
}, {
    "$project": {
        "student_id": 1,
        "course": 1,
        "score": 1,
        "name": "$student.name",
        "grade": "$student.grade"
    }
    # _id, student_id, course, score, name, grade
}, {
    "$facet": {
        "main": [],
        "sub": []
    }
    # main:[{_id, student_id, course, name, score, grade}],
    # sub: [{_id, student_id, name, course, score, grade}]
}, {
    "$unwind": "$main"
    # main: {_id, student_id, course, name, score, grade},
    # sub: [{_id, student_id, name, course, score, grade}]
}, {
    "$unwind": "$sub"
    # main: {_id, student_id, course, name, score, grade},
    # sub:  {_id, student_id, name, course, score, grade}
}, {
    "$match": {
        "$expr": {"$and": [{"$ne": ["$main.course", "$sub.course"]},
                           {"$ne": ["$main.student_id", "$sub.student_id"]}
                           ]}
    }
# main: {_id, student_id, course, name, score, grade},
    # sub:  {_id, student_id, name, course, score, grade}
},{
   "$project": {
       "main":1,
       "sub":1,
       "difference": { "$abs": { "$subtract": ["$main.grade", "$sub.grade"] } }
   }
},{
   "$project": {
       "main":1,
       "sub":1,
       "difference": 1,
       "branches": {
       "$switch": {
             "branches":[
                   {"case": {"$lte": ["$difference", 1] },
                  "then": "$sub"}],
            "default": None
         }
       }
   }
}
    , {
    # main: {_id, student_id, course, name, score},
    # sub:  {_id, student_id, name, course, score}
    "$group": {
        "_id": {
            "main_course": "$main.course",
            "main_id": "$main.student_id"
        },
        "main_name": {"$first": "$main.name"},
        "main_score": {"$first": "$main.score"},
        "main_grade": {"$first": "$main.grade"},
        "similars": {
            "$addToSet": {
                "sub_course": "$branches.course",
                "sub_name": "$branches.name",
                "sub_score": "$branches.score",
                "sub_grade": "$branches.grade"
            }
        }
    }
    # _id: {main_course, main_id}, main_name, main_score, similars: [{sub_name, sub_score}]
}, {
    "$sort": {
        "main_score": -1
    }
    # _id: {main_course, main_id}, main_name, main_score, similars: [{sub_name, sub_score}]
}, {
    "$group": {
        "_id": "$_id.main_course",
        "students": {
            "$push": {
                "main_id": "$_id.main_id",
                "main_name": "$main_name",
                "main_score": "$main_score",
                "main_grade": "$main_grade",
                "similars": "$similars"
            }
        }
    }
    # _id<course>, students: [{main_id, main_name, main_score, main_grade, similars:[{sub_name, sub_score, sub_grade}]}]
}, {
    "$sort": {
        "_id": 1
    }
    # _id<course>, students: [{main_id, main_name, main_score, main_grade, similars:[{sub_name, sub_score, sub_grade}]}]
}
])

num = 0
for agg in aggs:
    # print(agg)
    print(agg["_id"])
    for st in agg['students']:
        print('\t', st['main_name'], st['main_score'], st['main_grade'])
        for sim in st['similars']:
            # print(sim)
            if len(sim) == 0:
                continue
            print('\t\t', sim['sub_course'], '\t', sim['sub_name'], '\t', sim['sub_score'], '\t', sim['sub_grade'])
            num += 1
print(num)
