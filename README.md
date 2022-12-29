# smt_action
使用Github Action来定时运行python脚本

## 如何使用
**注意：Fork此仓库或者使用此仓库作为模版，如果不是单纯想贡献代码，请保持仓库私有状态！**

**否则会导致个人信息泄露!**

### 编写Task
示例: `./tasks/demo.py`

1. 在 `./tasks` 文件夹下新建一个 `.py` 文件，命名应该具有辨识度
2. 按照示例完成自己的task
3. 注册task: 阅读 `./tasks/__init__.py` 中的注释部分
3. 设置 github action: 复制一份已经存在的 `action.yml` 文件，重命名并修改，修改部分为: `cron` 部分以及最后运行传入的 参数
4. 测试: `python ./main.py demotask`

### 注意
1. 可以在 `config.json` 中自行添加参数，格式为 appname: {"k": v, ...}，也可以为已经存在的参数增加字段，但是不要修改已经存在的字段
2. Task 配置寻找逻辑：
  - 比如: `demotask = DemoTask("demotask")`
  - 会在配置文件中拿到 `"demotask"` 所对应的字典，并解析为 `AppConfig` 对象，其中 `Appconfig.data` 就是原始的字典
3. 通过删除 `*.yml` 文件，来删除指定的 `Task` 运行，或者注释掉 `cron` 设置
