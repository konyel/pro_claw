#!/usr/bin/env /usr/local/bin/python 
#-*- coding: UTF-8 -*- 

#数据库操作类，读取商品列表到内存中

import time
import MySQLdb
import common_log 
import common_conf
import urllib

_load_time = 0 
_goods_info = {}
_conn = MySQLdb.connect(host = common_conf.db_host,
                        user = common_conf.db_user,
                        passwd = common_conf.db_passwd,
                        db = common_conf.db_name)

class CommonGoodsUtil:
     def __init__(self):
         self.goods_id = 0
         self.name = "" 
         self.img_url = ""
         self.source_url = ""
         self.price = 0
         self.pieces = 0

     def Init(self,row):
         self.goods_id = row[0]
         self.name = urllib.quote(str(row[1]))
         self.img_url = urllib.quote(str(row[2]))
         self.source_url = urllib.quote(str(row[3]))
         self.price = row[4]
         self.pieces = row[5]
     
     def ToString(self):
         data = {}
         data["goods_id"] = self.goods_id
         data["name"] = self.name
         data["img_url"] = self.img_url
         data["source_url"] = self.source_url
         data["price"] = self.price
         return data

def GetGoodsInfo(goods):
       ret = 0
       common_conf.LOG.debug("interv time [%d]" % (time.time() - _load_time) )
       if time.time() - _load_time > 10:
            ret = LoadMysql()
            if ret: return ret
       goods = _goods_info[goods.goods_id]
       return 0 
def GetGoodsList(goods_list):
       ret = 0
       common_conf.LOG.debug("interv time [%d]" % (time.time() - _load_time) )
       if time.time() - _load_time > 10:
            ret = LoadMysql()
            if ret : return ret
       for var in _goods_info.keys():
              common_conf.LOG.debug("good info key [%s] " % (var))
              goods_list.append(_goods_info[var].ToString())
            
def LoadMysql():
        if not _conn.ping():
            ret = MysqlConnect()
            if ret: return ret
        cursor = _conn.cursor()  
        count = cursor.execute('select goods_id, \
                                       name, \
                                       img_url, \
                                       source_url, \
                                       pieces, \
                                       price from wish_goods_list')
        result = cursor.fetchall()
        common_conf.LOG.debug("sql resutl [%s]" % (result));
        for row in result:
             goods = CommonGoodsUtil()
             goods.Init(row)
             _goods_info[goods.goods_id] = goods
        _load_time = time.time()
        
def MysqlConnect():
       try:
           _conn = MySQLdb.connect(host = common_conf.db_host,
                        user = common_conf.db_user,
                        passwd = common_conf.db_passwd,
                        db = common_conf.db_name)
       except MySQLdb.Error,e:
           common_conf.LOG.error("mysql connect error ! [%s] [%s] [%s] [%s]" 
                                    % (common_conf.db_host, 
                                       common_conf.db_user, 
                                       common_conf.db_name,
                                       common_conf.db_passwd))
           return ECODE_CGI_MYSQL_CONN

