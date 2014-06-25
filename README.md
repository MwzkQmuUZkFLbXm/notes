notes
=====

简单的Flask博客

Credits
=======

[charlesleifer](http://charlesleifer.com/blog/saturday-morning-hack-a-little-note-taking-app-with-flask/)

本地部署
========

##建议利用[Virtualenv](http://virtualenv.readthedocs.org/en/latest/)进行本地环境搭建

1. 创建虚拟环境

    * ```pip install virtualenv```
    
    * ```virtualenv webapp```
    
    * ```cd webapp```
    
    * ```source bin/activate```

2. 克隆代码

    * ```git clone git@github.com:kmlg/notes.git```
    
    * ```cd notes```
    
    * ```pip install -r requirements.txt```
    

3. 运行应用

    * ```python manage.py```

Todo
====

1. 添加多用户动能
2. RESTful API
3. 重构前端
