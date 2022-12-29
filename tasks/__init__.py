#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: __init__.py
# 说明:
# 时间: 2022/12/28 19:06:00
# 作者: Azure
# 版本: 1.0

__all__ = [
    'TaskBase',
    'TaskStore',
    'tasks'
]

from tools.error import *

from .email import email_daily_task, email_weekly_task
from .task import TaskBase, TaskStore
from .demo import demotask

tasks = TaskStore()

# 在这里加入所有的tasks
# Tasks 的注册在此
# 把实例化的Task加入此列表即可完成注册
# 否则会提示找不到 Task, 并报错
have_tasks = [
    email_weekly_task,
    email_daily_task,
    demotask
]

# 完成注册后，需要设置 githubaction 的配置 `.yml` 文件，位置在: ./.github/workflows/***.yml
# 可以复制一份已经存在的，然后修改定时部分(cron) 以及替换 运行参数
# 详细可见 .github/workflows/daily_email.yml 中的注释部分

tasks.add_tasks(have_tasks)
