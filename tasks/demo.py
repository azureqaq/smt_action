#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 文件: demo.py
# 说明:
# 时间: 2022/12/29 10:48:53
# 作者: Azure
# 版本: 1.0

# 这一步是必须的，引入 TaskBase
from tasks import TaskBase

# 这一步是必须的，继承 TaskBase 来重写run方法
# 这里的 run 方法是这个Task运行的入口和主体


class DemoTask(TaskBase):
    def run(self):
        # 继承了一些方法，可以查看 TaskBase 的实现，来使用
        # 后期也会更新

        # 此方法请用实时的方式编写，比如不要在这里用时间判断 sleep 到指定时间等
        # 对于运行时间及频率操作在其他地方，详见 README 中的相关部分

        # 这里作为此TASK的入口
        # 集成了日志方法，debug不会记录到文件，
        # Warn 及以上的日志，会通过 email_daily_task 每日发送给配置文件中的所有邮件接收者
        # 所以要慎重使用 self.warn('content') 及以上的方法，除非重要信息
        self.debug('实例 Task run ...')

        # 还集成了一种邮件方法 => 即时邮件
        # 详细使用方法请看此方法的函数说明 (如果 receivers 为 [] 那么不会发送邮件)
        # 对于即时性要求高的可以使用此方法，同时，如果此信息只对部分收件人有用，那么请指定 receivers
        self.send_email_now('content', 'title-demo', receivers=[])

        # 配置文件部分-专用配置文件
        # 继承了对配置文件的读取
        config = self.config
        # 此时变量 config 代表的是 本类实例化时依据 appname 参数，在 config.json 中找到的字典
        # 结合本文件最后实例化的代码而言：config 也就是字典 {"arg1": 123, "arg2": 456}
        print(f'{self} 使用的 {str(config)}')
        # 如果，config.json 中未找到相应字典，那么返回 None

        # 通用配置文件
        # 如果好几个Task共同使用一个配置文件部分，比如 email_daily_task email_weekly_task
        # 或者强制使用其他的配置文件
        # 那么可以强制覆盖 self.config，用法:
        self.overwrite_config('email')
        print(f'{self} 使用的配置字典: {self.config.data=}')
        # 此时实例的self.config就变为了 email 的配置

        # 错误处理部分 ！！
        # 此函数运行时，如果返回异常，会被记录到日志文件中(每日发送)
        # 所以请做好错误处理，比如，将可以接受失败的Task，用 try:... 来包含，比如
        try:
            pass
        except Exception as e:
            self.debug(f'demo 错误: {e}')
        # 用debug或者其他方式处理，推荐：debug 和 即时邮件


# 这一步是必须的
# 请注意变量名和DemoTask的参数必须一样(方便使用)
demotask = DemoTask(name='demotask')

# 到这里就完成了task的编写，但是还没有注册
# 下一步，Task的注册 s请阅读 ./__init__.py 中的注释部分
