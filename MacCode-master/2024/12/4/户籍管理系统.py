from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

'''必要操作'''
app = Flask(__name__)# 创建 Flask 应用实例
app.config['SECRET_KEY'] = 'your_secret_key'# 配置 Flask 应用的密钥
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:561000@localhost:3306/flaskdb'# 配置 SQLAlchemy 的数据库连接 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 初始化 SQLAlchemy 数据库对象
db = SQLAlchemy(app)
# 初始化 Flask-Login 的登录管理器
login_manager = LoginManager(app)
login_manager.login_view = 'func_login'  # 设置登录页面的视图函数

# 定义 User 模型，继承自 UserMixin 和 db.Model
class User(UserMixin, db.Model):
    __tablename__ = 'user'  # 指定数据库表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    username = db.Column(db.String(100), nullable=False, unique=True)  # 用户名，不允许为空，唯一
    password = db.Column(db.String(100), nullable=False)  # 密码，不允许为空
    is_admin = db.Column(db.Boolean, default=False)  # 是否为管理员，默认为 False
    is_id_card_valid = db.Column(db.Boolean, default=True)  # 身份证是否有效，默认为 True
    id_card_expiration = db.Column(db.DateTime, nullable=True)  # 身份证有效期，允许为空
    households = db.relationship('Household', backref='owner', lazy=True)  # 与 Household 表的关系，backref 用于反向引用
    households_member = db.relationship('Household', secondary='household_member', backref=db.backref('members', lazy=True))  # 与 Household 表的多对多关系

# 定义 Household 模型，继承自 db.Model
class Household(db.Model):
    __tablename__ = 'household'  # 指定数据库表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 户主 ID，关联 User 表

# 定义 HouseholdMember 模型，继承自 db.Model
class HouseholdMember(db.Model):
    __tablename__ = 'household_member'  # 指定数据库表名
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)  # 用户 ID，关联 User 表，主键
    household_id = db.Column(db.Integer, db.ForeignKey('household.id'), primary_key=True)  # 户口本 ID，关联 Household 表，主键

# 用户加载回调函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 根据用户 ID 加载用户

# 定义首页路由，重定向到 index 页面
@app.route('/')
def hello():
    return redirect(url_for('func_index'))

# 定义 index 页面路由
@app.route('/index')
def func_index():
    return render_template('index.html')

# 定义登录页面路由，支持 GET 和 POST 方法
@app.route('/login', methods=['GET', 'POST'])
def func_login():
    if request.method == 'POST':  # 处理 POST 请求
        username = request.form.get('username')  # 获取用户名
        password = request.form.get('password')  # 获取密码
        user = User.query.filter_by(username=username, password=password).first()  # 查询用户
        if user:
            if user.is_admin:
                login_user(user)  # 登录用户
                return redirect('/admin_index')  # 重定向到管理员主页
            else:
                return '仅户籍警可以登录！'  # 非管理员用户登录失败提示
        else:
            return '登录失败！'  # 用户名或密码错误提示
    return render_template('login.html')  # 渲染登录页面

# 定义注册页面路由，支持 GET 和 POST 方法
@app.route('/register', methods=['GET', 'POST'])
def func_register():
    if request.method == 'POST':  # 处理 POST 请求
        username = request.form.get('username')  # 获取用户名
        password = request.form.get('password')  # 获取密码
        id_card_expiration = request.form.get('id_card_expiration')  # 获取身份证有效期
        if id_card_expiration:
            id_card_expiration = datetime.fromisoformat(id_card_expiration)  # 将字符串转换为 datetime
        else:
            id_card_expiration = None
        user = User.query.filter_by(username=username).first()  # 查询用户是否存在
        if user:
            return '用户名已存在！'  # 用户名已存在提示
        new_user = User(username=username, password=password, id_card_expiration=id_card_expiration)  # 创建新用户
        db.session.add(new_user)  # 添加新用户到数据库会话
        db.session.commit()  # 提交会话
        return redirect(url_for('func_login'))  # 重定向到登录页面
    return render_template('register.html')  # 渲染注册页面

# 定义注销页面路由，需登录
@app.route('/logout')
@login_required
def func_logout():
    logout_user()  # 注销当前用户
    return redirect('/index')  # 重定向到 index 页面

# 定义管理员首页路由，需登录
@app.route('/admin_index')
@login_required
def admin_index():
    if not current_user.is_admin:
        return '只有管理员可以访问此页面！'  # 非管理员用户访问提示
    return render_template('admin_index.html')  # 渲染管理员首页

# 定义查询用户页面路由，需登录
@app.route('/db/query/<name>')
@login_required
def func_query(name):
    users = User.query.filter_by(username=name).all()  # 根据用户名查询用户
    return render_template('query.html', users=users)  # 渲染查询结果页面

# 定义查询所有用户页面路由，需登录
@app.route('/db/query/all')
@login_required
def func_query_all():
    users = User.query.all()  # 查询所有用户
    return render_template('query.html', users=users)  # 渲染查询结果页面

# 定义添加用户页面路由，需登录
@app.route('/db/add', methods=['GET', 'POST'])
@login_required
def func_add():
    if not current_user.is_admin:
        return '只有管理员可以添加用户！'  # 非管理员用户访问提示

    if request.method == 'POST':  # 处理 POST 请求
        username = request.form.get('username')  # 获取用户名
        password = request.form.get('password')  # 获取密码
        id_card_expiration = request.form.get('id_card_expiration')  # 获取身份证有效期
        is_admin = request.form.get('is_admin') == 'on'  # 获取是否为管理员
        is_id_card_valid = request.form.get('is_id_card_valid') == 'on'  # 获取身份证是否有效

        if id_card_expiration:
            id_card_expiration = datetime.fromisoformat(id_card_expiration)  # 将字符串转换为 datetime
        else:
            id_card_expiration = None

        new_user = User(username=username, password=password, id_card_expiration=id_card_expiration, is_admin=is_admin,
                        is_id_card_valid=is_id_card_valid)  # 创建新用户
        db.session.add(new_user)  # 添加新用户到数据库会话
        db.session.commit()  # 提交会话
        return redirect('/admin_index')  # 重定向到管理员首页

    return render_template('add.html')  # 渲染添加用户页面

# 定义删除用户页面路由，需登录
@app.route('/db/delete/', methods=['GET', 'POST'])
@login_required
def func_delete():
    if not current_user.is_admin:
        return '只有管理员可以删除用户！'  # 非管理员用户访问提示

    if request.method == 'POST':  # 处理 POST 请求
        id = request.form.get('id')  # 获取用户 ID
        name = request.form.get('username')  # 获取用户名
        user = User.query.filter_by(id=id, username=name).first()  # 根据 ID 和用户名查询用户
        if user:
            db.session.delete(user)  # 删除用户
            db.session.commit()  # 提交会话
            return redirect('/db/query/all')  # 重定向到查询所有用户页面
        else:
            return f"ID：{id}Name：{name} 的用户不存在或输入错误"  # 用户不存在或输入错误提示

    return render_template('delete_user.html')  # 渲染删除用户页面

# 定义输入用户 ID 页面路由，需登录
@app.route('/db/input_user_id', methods=['GET', 'POST'])
@login_required
def input_user_id():
    if request.method == 'POST':  # 处理 POST 请求
        user_id = request.form.get('user_id')  # 获取用户 ID
        if not user_id or user_id == '0':
            flash('请输入用户ID！', 'error')  # 提示用户输入 ID
        else:
            return redirect(url_for('func_update', user_id=user_id))  # 重定向到更新用户页面
    return render_template('input_user_id.html')  # 渲染输入用户 ID 页面

# 定义更新用户信息页面路由，需登录
@app.route('/db/update/<id>', methods=['GET', 'POST'])
@login_required
def func_update(id):
    if not current_user.is_admin:
        return '只有管理员可以更新用户信息！'  # 非管理员用户访问提示

    user = User.query.get(id)  # 根据用户 ID 查询用户
    if not user:
        return f"用户不存在"  # 用户不存在提示

    if request.method == 'POST':  # 处理 POST 请求
        user.username = request.form.get('username')  # 更新用户名
        user.password = request.form.get('password')  # 更新密码
        id_card_expiration = request.form.get('id_card_expiration')  # 获取身份证有效期
        user.is_admin = request.form.get('is_admin') == 'on'  # 更新是否为管理员
        user.is_id_card_valid = request.form.get('is_id_card_valid') == 'on'  # 更新身份证是否有效

        if id_card_expiration:
            user.id_card_expiration = datetime.fromisoformat(id_card_expiration)  # 将字符串转换为 datetime
        else:
            user.id_card_expiration = None

        db.session.commit()  # 提交会话
        return redirect('/db/query/all')  # 重定向到查询所有用户页面

    return render_template('update.html', user=user)  # 渲染更新用户信息页面

# 定义查询特定户口本信息页面路由，需登录
@app.route('/db/household/query/<id>')
@login_required
def func_query_household(id):
    household = Household.query.get(id)  # 根据户口本 ID 查询户口本
    if household:
        return render_template('household_query.html', household=household)  # 渲染查询结果页面
    else:
        return f"户主 {id} 户口本不存在"  # 户口本不存在提示

# 定义查询所有户口本信息页面路由，需登录
@app.route('/db/household/query_all')
@login_required
def func_query_household_all():
    if not current_user.is_admin:
        return '只有管理员可以查询所有户口本！'  # 非管理员用户访问提示

    households = Household.query.all()  # 查询所有户口本
    return render_template('household_query_all.html', households=households)  # 渲染查询结果页面

# 定义添加户口本页面路由，需登录
@app.route('/db/household/add', methods=['GET', 'POST'])
@login_required
def func_add_household():
    if not current_user.is_admin:
        return '只有管理员可以添加户口本！'  # 非管理员用户访问提示

    if request.method == 'POST':  # 处理 POST 请求
        owner_id = request.form.get('owner_id')  # 获取户主 ID
        members_ids = request.form.getlist('members_ids')  # 获取成员 ID 列表
        owner = User.query.get(owner_id)  # 根据户主 ID 查询户主
        if not owner:
            return '户主不存在'  # 户主不存在提示

        household = Household(owner=owner)  # 创建新户口本
        for member_id in members_ids:
            member = User.query.get(member_id)  # 根据成员 ID 查询成员
            if member:
                household.members.append(member)  # 添加成员到户口本
            else:
                return f'用户 {member_id} 不存在'  # 成员不存在提示

        db.session.add(household)  # 添加新户口本到数据库会话
        db.session.commit()  # 提交会话
        return redirect('/admin_index')  # 重定向到管理员首页

    users = User.query.all()  # 查询所有用户
    return render_template('household_add.html', users=users)  # 渲染添加户口本页面

# 定义删除户口本页面路由，需登录
@app.route('/db/household/delete/<id>')
@login_required
def func_delete_household(id):
    if not current_user.is_admin:
        return '只有管理员可以删除户口本！'  # 非管理员用户访问提示

    household = Household.query.get(id)  # 根据户口本 ID 查询户口本
    if household:
        db.session.delete(household)  # 删除户口本
        db.session.commit()  # 提交会话
        return redirect('/db/household/query_all')  # 重定向到查询所有户口本页面
    else:
        return f"户主 {id} 户口本不存在"  # 户口本不存在提示

# 定义更新户口本信息页面路由，需登录
@app.route('/db/household/update/<id>', methods=['GET', 'POST'])
@login_required
def func_update_household(id):
    if not current_user.is_admin:
        return '只有管理员可以更新户口本信息！'  # 非管理员用户访问提示

    household = Household.query.get(id)  # 根据户口本 ID 查询户口本
    if not household:
        return f"户主 {id} 户口本不存在"  # 户口本不存在提示

    if request.method == 'POST':  # 处理 POST 请求
        owner_id = request.form.get('owner_id')  # 获取新的户主 ID
        members_ids = request.form.getlist('members_ids')  # 获取新的成员 ID 列表
        owner = User.query.get(owner_id)  # 根据新户主 ID 查询户主
        if not owner:
            return '户主不存在'  # 新户主不存在提示

        household.owner = owner  # 更新户主
        household.members = []  # 清空成员列表
        for member_id in members_ids:
            member = User.query.get(member_id)  # 根据成员 ID 查询成员
            if member:
                household.members.append(member)  # 添加成员到户口本
            else:
                return f'用户 {member_id} 不存在'  # 成员不存在提示

        db.session.commit()  # 提交会话
        return redirect('/db/household/query_all')  # 重定向到查询所有户口本页面

    users = User.query.all()  # 查询所有用户
    return render_template('household_update.html', household=household, users=users)  # 渲染更新户口本信息页面

# 定义用户查询自己的户口本信息页面路由，需登录
@app.route('/user/household')
@login_required
def func_user_household():
    user = current_user  # 获取当前登录用户
    household = Household.query.filter_by(owner_id=user.id).first()  # 根据用户 ID 查询其户口本
    if household:
        return render_template('user_household.html', household=household)  # 渲染查询结果页面
    else:
        return render_template('user_household.html', household=None)  # 无户口本信息时渲染空页面

# 主函数
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建所有数据库表
    app.run(debug=True)  # 启动 Flask 应用，调试模式开启
