# -*- coding:utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager
 
#第一步：建立task_queue和result_queue，用来存放任务和结果
task_queue = queue.Queue()
result_queue = queue.Queue()
 
class Queuemanager(BaseManager):
	pass
 
 
#第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，将Queue对象在网络中暴露
Queuemanager.register('get_task_queue', callable=lambda: task_queue)
Queuemanager.register('get_result_queue', callable=lambda: result_queue)
 
#第三步:绑定端口8001，设置验证口令'lyz',这个相当于对象的初始化
manager = Queuemanager(address=('', 8001), authkey='qiye'.encode(encoding='UTF-8'))
 
#第四步：启动管理，监听信息通道
manager.start()
 
try:

    # 通过网络获取任务队列和结果队列
    task = manager.get_task_queue()
    result = manager.get_result_queue()



    # 添加任务
    for url in ["ImageUrl_" + str(i) for i in range(10)]:
        print('url is %s' % url)
        task.put(url)

    print('try get result')
    for i in range(10):
        print('result is %s' % result.get(timeout=10))

except Exception as e:
    print (str(e))
finally:
    manager.shutdown()


