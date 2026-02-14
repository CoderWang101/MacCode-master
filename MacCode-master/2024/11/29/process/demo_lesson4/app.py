from flask import Flask,render_template,jsonify,redirect,request
from flask_sqlalchemy import SQLAlchemy
#redirect重定向

app = Flask(__name__)
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100), nullable=False)

#根目录
@app.route('/')
def hello():
    db.create_all()
    return 'db学习!'

@app.route('/db/add')
@app.route('/db/add/<name>')
@app.route('/db/add/<name>/<pwd>')
def func_add(name='孙悟空',pwd='000'):
    user=User(username=name,password=pwd)
    db.session.add(user)
    db.session.commit()
    return f"{user.username}添加成功！"

#Find
@app.route('/db/query/<name>')
def func_query(name):
    #1.filter_by查询
    users=User.query.filter_by(username=name)
    return render_template('query.html',users=users)

#Print_all
@app.route('/db/print')
def func_print_all():
    #1.filter_by查询
    users=User.query.all()
    return render_template('query.html',users=users)

#Exchange
@app.route('/db/update')
def func_update():
    user=User.query.filter_by(username='孙悟空').first()
    user.password='123'
    user.username='六耳猕猴'
    db.session.commit()
    return f'修改成功'

#Delete
@app.route('/db/delete/<name>')
def func_delete(name):
    user=User.query.filter_by(username=name).first()

    if user:
        db.session.delete(user)
        db.session.commit()
        return f"{user.username}删除成功"
    else:
        return f"{name} 用户不存在"

@app.route('/db/delete/all/<name>')
def func_delete_all(name):
    user=User.query.filter_by(username=name).all()

    if not user:
        return jsonify({"error": f":'{name}'不存在！"}),404

    for user in user:
        db.session.delete(user)
    db.session.commit()
    return jsonify({"true": f"全部删除成功'{name}！"})

# @app.route('/db/delete/<name>')
# @app.route('/db/delete/<name>/<choose>')
# def func_delete_chose(name, all='null'):
#     if all == 'all':
#         users = User.query.filter_by(username=name).all() # 查找所有同名用户
#
#         if not users:
#             return jsonify({"error": f"用户 '{name}' 不存在！"}), 404
#
#         for user in users:
#             db.session.delete(user) # 删除每个同名用户
#             db.session.commit() # 提交删除操作
#             return jsonify({"message": f"所有用户名为 '{name}' 的用户已删除！"}), 200
#         else:
#             user = User.query.filter_by(username=name).first() # 查找第一个同名用户
#
#         if user:
#             db.session.delete(user) # 删除该用户
#             db.session.commit() # 提交删除操作
#             return jsonify({"message": f"用户 '{user.username}' 已删除！"}), 200
#     else:
#         return jsonify({"error": f"用户 '{name}' 不存在！"}), 404

#前端
@app.route('/index',methods=['GET','POST'])
def func_index():
    #Print所有用户
    if request.method =='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        user=User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        print("1")
        return redirect('/db/print')

    return render_template('index.html')

@app.route('/title')
def func_title():
    return render_template('title.html')



if __name__=='__main__':
    app.run(debug=True)