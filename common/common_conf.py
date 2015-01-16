#!/usr/bin/env /usr/local/bin/python 
#-*- coding: UTF-8 -*- 

import common_log

#配置数据库链接 
db_host = "127.0.0.1"
db_user = "root"
db_passwd = "new-password"
db_name = "wish"

#配置log地址
log_file = "./log/wish.log"
_log = common_log.Log(log_file)
LOG , handle = _log.init()

#nosql 配置地址
wish_mem = ['127.0.0.1:26500']

