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
from flask.templating import render_template


if __name__ == '__main__':
    
    app = Flask('myBlog')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/doLogin', methods=['POST'])
    def doLogin():
        flag, obj = User.doLogin(request.form['username'], request.form['password'])
        if flag:
            return render_template('blogManager.html', user=obj)
        else:
            return redirect(url_for('login', error=obj))
        
        
    app.run(host='0.0.0.0', port=8088)
    
