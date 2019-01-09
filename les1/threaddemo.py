# -*- coding:utf-8 -*-

import threadpool 
import time,random 
import queue

def hello1(str): 
    time.sleep(2) 
    return str 

def print_ret(request, result): 
    print ("the result is %s %r "  % (request.requestID, result))


def deal_task(pool):
    try:
        pool.poll(True)
    except Exception as e:
        print (str(e))

#lst = [1,2,3,4,5,6,7]
q = queue.Queue()
for i in range(100):
    q.put(i)

lst = [q.get() for i in range(q.qsize())]

pool = threadpool.ThreadPool(10) 
requests = threadpool.makeRequests(hello1, lst, print_ret) 
for req in requests:
    pool.putRequest(req)
    #deal_task(pool)

pool.wait()