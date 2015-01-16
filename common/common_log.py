#!/bin/env python
#-*- coding: UTF-8 -*- 
import time
import logging


class Log:
    def __init__(self, log_file):
        self.log_file = log_file

    def init(self):
        self.logger=logging.getLogger()
        self.handler=logging.FileHandler(self.log_file)
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(filename)s %(lineno)d %(message)s ')
        self.handler.setFormatter(formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.NOTSET)
    
        return [self.logger, self.handler]

    def debug(self, msg):
        logger, handler = self.init()
        logger.debug(msg)
        logger.removeHandler(handler)
    
    def info(self, msg):
        logger, handler = self.init()
        logger.info(msg)
        logger.removeHandler(handler)

    def warn(self, msg):
        logger, handler = self.init()
        logger.warn(msg)
        logger.removeHandler(handler)
    
    def error(self,msg):
        logger, handler = self.init()
        logger.error(msg)
        logger.removeHandler(handler)
