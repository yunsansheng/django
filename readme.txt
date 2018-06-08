Django常用命令

1.新建project
django-admin.py startproject [project_name]

2.新建app
cd [project_name]
python manage.py startapp [app_name]

3.创建数据库表 或 更新表或字段
# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate

4.使用开发服务器
python manage.py runserver [port 可不填]  

5.清空数据库,只留表结构
python manage.py flush

6.创建管理员
python manage.py createsuperuser

7. 导出数据 导入数据
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json

8. Django 项目环境终端
python manage.py shell
这个命令和 直接运行 python 或 bpython 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的 API，对于操作数据，还有一些小测试非常方便。

9. 数据库命令行
python manage.py dbshell
Django 会自动进入在settings.py中设置的数据库，如果是 MySQL 或 postgreSQL,会要求输入数据库用户密码。


10. 更多命令
终端上输入 python manage.py 可以看到详细的列表，在忘记子名称的时候特别有用。
