#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: email.py
# 说明:
# 时间: 2022/12/28 19:40:06
# 作者: Azure
# 版本: 1.0

'''
基于日志发送消息
'''

import time
from tasks.task import TaskBase
from tools.command import *

class EmailDailyTask(TaskBase):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def run(self):
        content = get_today_log()
        if len(content):
            con = ''.join(content)
            self.send_email_now(con, 'TasksBot 每日邮件')
        else:
            self.debug('今天无事发生')


class EmailWeeklyTask(TaskBase):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def run(self):
        content = get_week_log()
        if len(content):
            con = ''.join(content)
            self.send_email_now(con, "TaskBot 每周邮件")
        else:
            self.debug('这周无事发生')


TIME_F = r'%Y-%m-%d'
today = time.localtime()


def __need_is_today(s: str) -> bool:
    try:
        s_l = s.split(' ')[0]
        l_t = time.strptime(s_l, TIME_F)
        if l_t.tm_year == today.tm_year and \
            l_t.tm_mon == today.tm_mon and \
                l_t.tm_mday == today.tm_mday and \
        r'INFO' not in s :
            return True
    except:
        return False


def __need_is_week(s: str) -> bool:
    try:
        s_l = s.split(' ')[0]
        l_t = time.strptime(s_l, TIME_F)
        if 0 <= time.mktime(today) - time.mktime(l_t) <= 604800 and \
                'INFO' in s:
            return True
    except:
        return False


def get_week_log() -> list:
    '''
    获取这一周所有的log
    '''
    content = []
    with open(LOG_PATH, 'r', encoding='utf-8') as fr:
        for line in fr.readlines():
            if __need_is_week(line):
                content.append(line)

    return content


def get_today_log() -> list:
    '''
    从日志中获取今天需要发送的,
    一天一发送 Warn 及以上的，
    有可能是空的!
    '''
    content = []
    with open(LOG_PATH, 'r', encoding='utf-8') as fr:
        for line in fr.readlines():
            if __need_is_today(line):
                content.append(line)

    return content

email_daily_task = EmailDailyTask('email_daily_task')
email_weekly_task = EmailWeeklyTask('email_weekly_task')
