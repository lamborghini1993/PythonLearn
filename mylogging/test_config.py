# -*- coding:utf-8 -*-
'''
@Description: logging的配置测试
@Author: lamborghini1993
@Date: 2019-04-25 20:24:24
@UpdateDate: 2019-04-25 20:43:46
'''

import logging
import logging.config

logging.config.fileConfig("logging.conf")

root_logger = logging.getLogger()
file_logger = logging.getLogger(name="fileLogger")
rotating_logger = logging.getLogger(name="rotatingFileLogger")

root_logger.info("1")
file_logger.error("2")
rotating_logger.warning("3")
