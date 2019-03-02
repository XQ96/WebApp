# -*- coding:utf-8 -*-
# @Author:xuqi
# @time:2019/3/2 19:25
# @File:models.py

''''
    Models for user,blog,comment
'''

import time,uuid
import ctypes
from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
    return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
    __table__='users'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    email=StringField(ddl='varchar(50)')
    passwd=StringField(ddl='varchar(50)')
    admin=BoooleanField()
    name=StringField(ddl='varchar(50)')
    image=StringField(ddl='varchar(500)')
    created_at=FloatField(default=time.time)


class  Blog(Model):
    __table__='blogs'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    user_id=StringField(ddl='varchar(50)')
    user_name=StringField(ddl='varchar(50)')
    user_image=StringField(ddl='varchar(500)')
    name=StringField(ddl='varchar(50)')
    summary=StringField(ddl='varchar(200)')
    content=TextField()
    created_at=FloatField(default=time.time)

class Comment(Model):
    __table__='comment'

    id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
    blog_id=StringField(ddl='varchar(50)')
    user_id=StringField(ddl='varchar(50)')
    user_name=StringField(ddl='varchar(50)')
    user_image=StringField(ddl='varchar(500)')
    summary=StringField(ddl='varchar(200)')
    content=TextField()
    created_at=FloatField(default=time.time)
