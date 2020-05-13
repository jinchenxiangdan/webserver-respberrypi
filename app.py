from flask              import Flask, render_template
from flask_login        import LoginManager
from werkzeug.security  import generate_password_hash

# create flask application
app = Flask(__name__)
# set interaction key
app.secret_key = 'abc'
#
login_manager = LoginManager()      # 实例化登录管理对象
login_manager.init_app(app)         # 初始化应用
login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint


#
# root of the website 
#
@app.route('/')
def index():
    return render_template('index.html')

#
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/datashow')
def show_data(): 
    return render_template('data_show.html')

@app.route('/hello/<name>')
def hello(name): 
    return render_template('page.html', name=name)

@app.route('/mystatus')
def mystatus():
    pass







# this portion runs the server of the app
if __name__ == '__main__':
    # host = 0.0.0.0 : means the web app will be accessible to any device
    app.run(debug=True, host='0.0.0.0')



# ...
USERS = [
    {
        "id": 1,
        "name": 'lily',
        "password": generate_password_hash('123')
    },
    {
        "id": 2,
        "name": 'tom',
        "password": generate_password_hash('123')
    }
]

from werkzeug.security import generate_password_hash
import uuid
# ...
def create_user(user_name, password):
    # create new user 
    user = {
        "name": user_name,
        "password": generate_password_hash(password),
        # 使用 uuid 模板的 uuid4 方法生成一个全球唯一码
        "id": uuid.uuid4()
    }
    USERS.append(user)

def get_user(user_name):
    # get user record according to user name 
    for user in USERS:
        if user.get("name") == user_name:
            return user
    return None