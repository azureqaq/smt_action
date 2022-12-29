#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: task.py
# 说明:
# 时间: 2022/12/28 20:09:21
# 作者: Azure
# 版本: 1.0

from typing import Dict, List, Union

from tools import configfile, debug, error, info
from tools.email import send_email_now
from tools.error import *


class TaskBase(object):
    def __init__(self, name: str) -> None:
        self.name = name
        self.config = configfile.get_app_config(name)

    def run(self):
        '''
        程序入口，对于每一个Task应该独自实现一次，如果对结果不是很需要，
        请做好错误处理:
        这个函数如果引起异常，会被记录到日志，
        可以使用即时邮件
        '''
        self.debug(f'{self} 需要重写run方法')

    @property
    def debug(self):
        return debug

    @property
    def info(self):
        return info

    @property
    def error(self):
        return error

    @property
    def send_email_now(self):
        return send_email_now
    
    def overwrite_config(self, name: str):
        '''
        强制使用配置文件
        :param name: 哪个配置文件
        '''
        self.config = configfile.get_app_config(name)

    def __str__(self) -> str:
        return f'Task[{self.name}]'


class TaskStore(object):
    def __init__(self) -> None:
        self.tasks: Dict[str, TaskBase] = {}

    def add_tasks(self, tasks: List[TaskBase]):
        for i in tasks:
            self.tasks[i.name] = i

    def get_task(self, name: str) -> Union[TaskBase, None]:
        return self.tasks.get(name, None)

    def run_a_task(self, name: str):
        '''
        尝试运行一个 Task，如果失败则返回错误
        '''
        t = self.get_task(name)
        if t is None:
            raise TaskError(f'无法找到Task: {name}')
        else:
            t.run()

    def run_tasks(self, *ts):
        '''
        尝试运行 几个 Task，如果失败返回错误，
        其中一个失败不会阻止其他部分
        '''
        err_list = []

        for i in ts:
            try:
                print()
                print(f' Run: {i} '.center(40, '#'))
                self.run_a_task(i)
            except Exception as e:
                err_list.append(f'{i}: {str(e)}')

        print()
        print(f' All Tasks Done '.center(40, '#'))

        if len(err_list):
            err_str = '; '.join([str(x) for x in err_list])
            raise TaskError(f'{err_str}')
