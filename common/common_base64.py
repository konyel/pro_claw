#!/usr/bin/env /usr/local/bin/python 
#-*- coding: UTF-8 -*- 

import base64
import random
import time

def EncodeOrderId(opnid):
    #订单信息由用户id 当前时间 和 1-10000随机数组成 由#分隔
    var_list = [opnid,str(time.time()),str(random.randint(1,10000)) ] 
    str_encode = '#'.join(var_list) 
    return base64.b64encode(str_encode)
    
