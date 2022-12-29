#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: logger.py
# 说明:
# 时间: 2022/02/02 15:49:18
# 作者: Azure
# 版本: 1.0

from tools import error
from tasks import tasks

import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    print('使用的Task(s):', *args)

    try:
        tasks.run_tasks(
            *args
        )
    except Exception as e:
        error(f'此次运行有错误: {e}')
