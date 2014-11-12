# -*- encoding: utf-8 -*-
'''
Created on 2014-11-12

@author: huangtx@itg.net
'''
from myBlogLib.db import nosqlDB
from bson.objectid import ObjectId
from pymongo.cursor import Cursor

def getDB():
    return nosqlDB.getInstance()

class metaModel(dict):
    def __init__(self, **kw):
        for k, v in kw.items():
            self[k] = v
    
    def __getattr__(self, key):
        return self[key]
    
    def __setattr__(self, key, value):
        self[key] = value
        
    def _save2DB(self):
        return getDB().db[self.__tablename__].find_and_modify(query={'_id':self._id}, update=self , upsert=True)
    

class User(metaModel):
    __tablename__ = 'user'
    
    @classmethod
    def getUsers(cls, *args, **kw):
        cur = getDB().db[cls.__tablename__].find(**kw)
        return [u for u in cur]
    @classmethod
    def getUser(cls, *args, **kw):
        return getDB().db[cls.__tablename__].find_one(**kw)
    @classmethod
    def createUser(cls, username, passwd, email, *args, **kw):
        if User.checkUsername(username):
            return (False,u'用户名已经存在')
        try:
            kw.update(dict(_id=ObjectId(), username=username, password=passwd, email=email))
            user = User(**kw)
            user._save2DB()
            return (True,user)
        except BaseException,e:
            print e
            return (False,e)
    @classmethod
    def checkUsername(cls, username):
        return getDB().db[cls.__tablename__].find_one({'username':username})

if __name__ == '__main__':
    
    rs = User.createUser('htx22', 'htx', '123@123.com')
    print rs[1]
    
#     user = User.getUser({'username':'htx'})
#     print user
    
    pass
