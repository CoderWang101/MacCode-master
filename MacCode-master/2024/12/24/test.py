aggs = myscores.aggregate([{
    "$lookup": {
        "from": "mycoll",
        " localField ": "student_id",
        " foreignField ": "_id",
        "as": "st"
    }
}, {
    "$unwind": "$st"
}, {
    "$project": {
        "_id": 0,
        "course": 1,
        "score": 1,
        "name": "$st.name",
        "age": "$st.age",
        "grade": "$st.grade",
        "level": {
            " $switch ": {
                " branches ": [{
                    "case": {"$eq": ["$st.grade", 1]},
                    "then": '低年级'
                }, {
                    "case": {"$eq": ["$st.grade", 4]},
                    "then": '高年级'
                }],
                "default": " 中年级 "
            }
        }
    }
}, {
    "$sort": {
        "score": -1,
    }
}, {
    "$group": {
        "_id": {
            "course": "$course",
            "level": "$level"
        },
        "sts": {
            " $push ": {
                "score": "$score",
                "name": "$name",
                "age": "$age",
                "grade": "$grade"
            }
        }
    }
}, {
    "$sort": {
        " _id .level": 1,
    }
}, {
    "$group": {
        "_id": "$_id.course",
        "levels": {
            "$push": {
                "level": " $_id.level ",
                "sts": " $sts "
            }
        }
    }
}])
for agg in aggs:
    print(agg[" _id "])
    for level in agg["levels"]:
        print("	", level["level"])
        for st in level["sts"]:
            print("	", st["name"], st["age"], st["grade"], st["score"], sep="	")
