#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: config.py
# 说明:
# 时间: 2022/12/28 18:20:39
# 作者: Azure
# 版本: 1.0

import json
import os
from typing import Union, List, Dict
from .error import *


class AppConfig(object):
    '''
    App 配置
    '''

    def __init__(self, name: str, **kwargs) -> None:
        '''
        新建一个app配置对象，
        其余为参数，
        :param name: App 的ID，唯一
        '''
        self.name = name
        self.data = {}
        self.data.update(kwargs)

    def __str__(self) -> str:
        return f'AppConf[{self.name}-{len(self.data)}]'


class ConfigFile(object):
    '''配置文件'''

    def __init__(self, path: str) -> None:
        '''
        配置文件对象，
        储存格式为: {APPNAME: {...}, ...}
        '''
        self.path = path
        if not os.path.isfile(path):
            raise ConfigFileNotFoundError(f'无法找到配置文件: {path}')
        self.config = {}

        # 读取配置文件
        try:
            with open(path, 'r', encoding='utf-8') as fr:
                content: dict = json.load(fr)
                self.config.update(content)
        except Exception as e:
            raise ConfigParserError(f'无法解析配置文件: {path}, Err: {e}')

    def __str__(self) -> str:
        return f'ConfigFile[{self.path}-{len(self.config)}]'

    def get_app_config(self, name: str) -> Union[None, AppConfig]:
        '''
        获取appconfig，如果不存在返回None
        :param name: App name
        '''
        data: Union[dict, None] = self.config.get(name, None)
        if data is not None:
            return AppConfig(name, **data)
        else:
            return None

    def save_to_file(self):
        '''
        保存
        '''
        try:
            with open(self.path, 'w', encoding='utf-8') as fr:
                json.dump(self.config, fr, ensure_ascii=False, indent=4)
        except Exception as e:
            raise ConfigFileSaveError(f'无法保存配置到: {self.path}, Err: {e}')

    def add_app_configs(self, configs: List[AppConfig]):
        '''
        覆盖加入appconfig
        '''
        for i in configs:
            self.config.update({
                i.name: i.data
            })

    @classmethod
    def default_dict(cls):
        app1 = AppConfig('test1', enable=False, email='123@qq.com')
        app2 = AppConfig('test2', enable=False, email='123@qq.com')
        return {
            app1.name: app1.data,
            app2.name: app2.data
        }

    @classmethod
    def crate_configfile_default(cls, path: str):
        '''
        新建一个带有默认值的配置文件，会覆盖！
        '''
        try:
            with open(path, 'w', encoding='utf-8') as fr:
                json.dump(cls.default_dict(), fr, ensure_ascii=False, indent=4)
        except Exception as e:
            ConfigFileSaveError(f'无法创建带有默认值的配置文件: {path}, Err: {e}')

    def configs(self) -> Dict[str, AppConfig]:
        confs = {k: AppConfig(k, **v) for k, v in self.config.items()}
        return confs
