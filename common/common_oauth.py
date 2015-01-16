#!/usr/bin/env /usr/local/bin/python 
#-*- coding: UTF-8 -*- 

import web
import pycurl
import StringIO
import common_def
import common_conf
import json

class CommonOauth:
    def __init__(self):
        self.opnid = ""
    def Auth(self):
       param = web.input(code = "")
       if len(param.code) == 0:
              common_conf.LOG.error("oauth code not found [%s]" % param) 
              return ECODE_CGI_OAUTH_REFUSE 
       html = StringIO.StringIO()
       http_obj = pycurl.Curl()
       url = "https://api.weixin.qq.com/sns/oauth2/access_token?"
       url = url+"appid=wxf02b23d581276094&secret=9c4e236db14a024b7426d03b9ab27b36"
       url = url+"&code=%s&grant_type=authorization_code" % (param.code)
       http_obj.setopt(pycurl.URL, url)
       http_obj.setopt(pycurl.WRITEFUNCTION, html.write)
       http_obj.perform()
       try:
          token = json.loads(html.getvalue())
          if "errcode" in token:
              common_conf.LOG.error("get token error [%s][%s]" 
                                                % (html.getvalue(),param.code)) 
              return common_def.ECODE_CGI_OAUTH_INVAILD
       except ValueError,err:
              common_conf.LOG.error("get token error [%s]" % (err) )
              return common_def.ECODE_CGI_OAUTH_INVAILD

       url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN" % (token['access_token'],token['openid'])
       
       common_conf.LOG.debug("get user info [%s]"  % (url))
       #清理请求数据
       html.seek(0)
       html.truncate()
       http_obj.setopt(pycurl.URL, url)
       http_obj.perform()
       try:
          user_info = json.loads(html.getvalue())
          if "errcode" in user_info:
               common_conf.LOG.error("get userinfo [%s]" % (html.getvalue()) )
               return common_def.ECODE_CGI_OAUTH_INVAILD
       except ValueError,err:
               common_conf.LOG.error("parse json[%s] error %s"
                                    %(html.getvalue() , err))
               return common_def.ECODE_CGI_OAUTH_INVAILD
       except TypeError,err:
               common_conf.LOG.error("parse json[%s] error %s"
                                    %(html.getvalue() , err))
               return common_def.ECODE_CGI_OAUTH_INVAILD
       self.opnid = user_info['openid']
       return common_def.ECODE_CGI_OK

