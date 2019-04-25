# airplain

## 环境安装和使用
 
 * python3，依赖库安装pip install -r reqirement.txt
 * pycharm
 * mysql 并创建airplain数据库，在config.py中配置用户名和密码，替代文件中的用户名和密码即可。
 * 运行入口在airplain.py. 运行之后会出现http://localhost:8000/，点击即可访问网站。
 * 使用网站的一些准备
    1. 管理员默认用户名admin，密码123456。
    2. 管理员登录之后首先创建几个company，之后再创建几个机票。之后用户就可以使用。
    3. 用户先注册然后登陆。
    
## 技术细节
 
 * 所有的和用户相关的视图函数都在web文件夹下，具体函数的作用见注释。
 * 所有和管理员相关的视图函数在admin文件夹下。
 * data文件夹下是所有的数据处理函数。
 * form文件夹下是所有的表单定义。
 * models文件夹是所有的数据库模型定义。
 * statics文件夹是所有的静态文件。
 * templates文件夹是所有的模版（HTML）文件。
 