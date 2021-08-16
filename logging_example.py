'''import logger, logging

def getlogger():
   
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler(r'log.txt')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger '''

import os
import time
import datetime
import logging
import logger

loggers = {}
def getlogger():
    global loggers
    name='logPython'
    
    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        now = datetime.datetime.now()
        handler = logging.FileHandler('ProvisioningPython' + now.strftime("%Y-%m-%d") + '.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers[name] = logger
                       
        return logger