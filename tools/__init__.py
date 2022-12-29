#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: __init__.py
# 说明:
# 时间: 2022/01/23 00:10:21
# 作者: Azure
# 版本: 1.0

'''
tools，
logger 和 配置文件 已经在这里初始化了
'''

__all__ = [
    # 日志记录
    'debug', 'info', 'warn', 'error', 'critical', 'logexception', 'configfile'
]

from .config import ConfigFile
from .logger import logger


debug = logger.debug
info = logger.info
warn = logger.warning
error = logger.error
critical = logger.critical
logexception = logger.exception


configfile = ConfigFile('config.json')
