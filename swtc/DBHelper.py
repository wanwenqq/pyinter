# -*- coding:utf-8 -*-

#pymysql 封装

import pymysql as ps
from dbconfig import db_config as dc
import hashlib


class DBHelper:
    def __init__(self):
        self.host = dc['host']
        self.user = dc['user']
        self.password = dc['password']
        self.database = dc['database']
        self.charset = dc['charset']
        self.db = None
        self.curs = None

    # 打开数据库
    def openDB(self):
        self.db = ps.connect(host=self.host, user=self.user, password=self.password,database=self.database, charset=self.charset)
        self.curs = self.db.cursor()

    #关闭数据库
    def close(self):
        self.curs.close()
        self.db.close()

    # 数据增删改
    def _cud(self, sql, params):
        self.openDB()
        try:
            self.curs.execute(sql, params)
            self.db.commit()
        except Exception as e:
            print('cud出现错误:'+str(e))
            self.db.rollback()
        self.close()

    # 数据查询
    def find_all(self, sql, params):
        result = ()
        try:
            self.openDB()
            self.curs.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except:
            print('find出现错误')
        return result

            # 数据查询
    def find_one(self, sql, params):
        result = None
        try:
            self.openDB()
            self.curs.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
            return result
        except:
            print('find出现错误')
        return result


    def insert(self,sql,params=[]):
        return self._cud(sql,params)
    def update(self,sql,params=[]):
        return self._cud(sql,params)
    def delete(self,sql,params=[]):
        return self._cud(sql,params)


    def db_md5(self,md5):
        my_md5=hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()
