luthor__ = 'Max'  #作者
__date__ = "2017/9/10 14:41"  #创建时间

import orm, asyncio
from Model import User, Blog, Comment

def test(loop):
    yield from orm.create_pool(loop=loop, user='root', password='653155073', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
