# -*- encoding: utf-8 -*-
'''
Created on 2014年11月12日

@author: huangtx
'''
from flask.app import Flask
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from myBlogLib.models.Model import User


if __name__ == '__main__':
    
    app = Flask('myBlog')
    
    @app.route('/login')
    def login():
        return u'<html><form action=\'/doLogin\' method="POST"><input type="text" name="username"><br><input type="password" name="password"><br><input type="submit" value="提交"></form></html>'
    
    @app.route('/doLogin',methods=['POST'])
    def doLogin():

        user = User.getDoc(dict(username=request.form['username'],password=request.form['password']))
        if user:
            return u'欢迎登陆'
        else:
            return redirect(url_for('login'))
        
        
    app.run()
    