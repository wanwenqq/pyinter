# -*- coding: utf-8 -*-
# 定时任务 apscheduler https://blog.csdn.net/xc_zhou/article/details/80952147
import os
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
import time

from DBHelper import DBHelper

class CrawSwtc:
    def __init__(self, url):
        self.url = url
        
    def timedTask(self):
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # url = 'https://state.jingtum.com/init'
        url = self.url
        #包装头部
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        }
        #构建请求
        response = requests.get(url,headers=headers)
        if(response.status_code == 200):
            deep = response.json()['data']['ledgers'][0]['ledger_index']
            tradenum = response.json()['data']['ledgers'][0]['txn_count']
            hashstr = response.json()['data']['ledgers'][0]['ledger_hash']
            # localTime = time.localtime(response.json()['data']['ledgers'][0]['ledger_time']) 
            creatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) 
            print(hashstr) 
            sql = 'insert into swtc_main(deep,tradenum,hashstr,creatime) values(%s,%s,%s,%s)'
            mh = DBHelper()
            data = (deep,tradenum,hashstr,creatime)
            mh.insert(sql,data)
        

    def craw_swtc(self):
        # 创建后台执行的 schedulers
        scheduler = BackgroundScheduler()
        # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
        scheduler.add_job(self.timedTask, 'interval', seconds=8) # 间隔3秒钟执行一次
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            scheduler.start()    #这里的调度任务是独立的一个线程
            while True:
                time.sleep(2)    #其他任务是独立的线程执行
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            scheduler.shutdown()
            print('Exit The Job!')

