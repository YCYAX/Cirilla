#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot,sys
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

sys.path.append("../")
# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

# nonebot.load_builtin_plugins("echo")

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...

# 主要功能
"""
签到	玩家签到随机获得金币
我的金币	查询玩家金币数量
"""
nonebot.load_plugins("src/plugins/Main")
# 管理员
"""
添加超管 [第一次添加不需要超管权限]	给bot添加一个超级管理用户
保存数据 [需要超管权限]	保存玩家的数据 [金币]
私网地址 [需要超管权限]	显示服务器内网地址
广播 [需要超管权限] 广播超管消息
"""
nonebot.load_plugins("src/plugins/Super")
# 菜单
"""
菜单	展示普通菜单
更新菜单 [需要超管权限]	更新菜单内容
菜单内容 [需要超管权限]	展示菜单内容
生成菜单 [需要超管权限]	生成对应菜单
高级菜单 [需要超管权限]	展示高级菜单
"""
nonebot.load_plugins("src/plugins/Menu")
nonebot.load_plugins("src/plugins/Space_exploration")


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
