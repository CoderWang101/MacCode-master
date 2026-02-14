> db.mycoll.aggregation([{
   $group: {
       "_id":"$grade",
       "平均年龄": {"$avg": "$age"},
       "最大年龄": {"$max": "$age"},
       "最小年龄": {"$min": "$age"},
       "学生数量": {"$sum": 1}
   }
}])
