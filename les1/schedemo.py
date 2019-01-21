# -*- coding: utf-8 -*-
# 定时任务 apscheduler https://blog.csdn.net/xc_zhou/article/details/80952147
import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json


def timedTask():
    # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    url = 'https://state.jingtum.com/init'
    #包装头部
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    }
    #构建请求
    response = requests.get(url,headers=headers)
    if(response.status_code == 200):
        print(response.json()['data']['ledgers'][0]['ledger_index'])
    
  

if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler = BackgroundScheduler()
    scheduler.add_job(timedTask, 'interval', seconds=10) # 间隔3秒钟执行一次
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))


    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        scheduler.start()    #这里的调度任务是独立的一个线程
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
