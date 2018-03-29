# -*- coding : utf-8  -*-

import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    # 创建连接池
    db_dict = {'host':'127.0.0.1', 'port':3306, 'user': 'root', 'password': 'bookan', 'db': 'awesome'}
    await orm.create_pool(loop=loop, **db_dict)
    # u = User(id='123', emai='test@example.com', passwd='12345',admin=1,name='Test', image='about:blank', )
    u = User( )
    u.id = 1
    u.email = 'test@example.com'
    u.passwd = '12345'
    u.admin = 1
    u.name = 'anders'
    u.image = 'about:blank'
    await u.save()
    # await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()