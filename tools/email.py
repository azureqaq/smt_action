#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: email.py
# 说明:
# 时间: 2022/12/28 19:00:33
# 作者: Azure
# 版本: 1.0

import smtplib
from email.mime.text import MIMEText
from tools import error, debug
from tools import configfile
from typing import Union
from .error import *

email_config = configfile.get_app_config('email')


def send_email_now(content: str, title: Union[str, None] = None,
                   receivers: Union[list, None] = None):
    '''
    立即发送邮件, 除了 content 必须写以外，
    其他参数如果不写就用 默认值/配置文件中的值
    :param receivers: 如果不指定(None) => 使用配置文件中的值，如果是 [] 则不发送
    '''
    if receivers is not None and not len(receivers):
        return
    try:
        data = email_config.data
    except:
        raise EmailError('无法获取邮件设置')

    user = data['user']
    sender = data['sender']
    pwd = data['pwd']
    receivers: list = receivers or data['receivers']

    port = data['port']
    host = data['host']

    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = title or 'TasksBot'
    message['From'] = sender
    message['To'] = receivers[0]

    try:
        smtpobj = smtplib.SMTP_SSL(host=host)
        smtpobj.connect(host, int(port))
        smtpobj.login(user, pwd)
        smtpobj.sendmail(
            sender, receivers, message.as_string()
        )
        smtpobj.quit()
        debug('邮件发送成功')
    except Exception as e:
        error(f'发送邮件失败, Err: {e}')
    finally:
        try:
            smtpobj.quit()
        except:
            pass

    debug(f'发送邮件:\n{content}')
