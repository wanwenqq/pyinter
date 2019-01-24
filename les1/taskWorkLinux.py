# -*- coding:utf-8 -*-
from multiprocessing.managers import BaseManager
import queue

#1.创建Queue
import time


class QueueManager(BaseManager):
    pass


#2.获取管理端共享出来的队列，一定要跟管理端注册的名称相同

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#3.连接到服务器上
server_addr='132.232.100.47'
print("正在连接服务端%s......" %(server_addr))

#4.端口号和密码要跟管理端保持一致；
m=QueueManager(address=(server_addr,9999),authkey=b'westos')

#5.进行连接
m.connect()


#6.获取Queue对象
task=m.get_task_queue()
result=m.get_result_queue()

#7.获取管理端共享的任务
for i in range(100):
    try:
        n=task.get()
        #模拟处理任务
        print('run task %d*%d...' %(n,n))
        time.sleep(1)
        r='%d * %d = %d' %(n,n,n**2)
        #将执行的任务结果放入结果队列中
        result.put(r)
    except queue.Empty:
        print('任务队列为空..')
print('执行结束')