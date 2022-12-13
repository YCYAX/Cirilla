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
查询玩家金币
签到
"""
nonebot.load_plugins("src/plugins/Main")
# 管理员
"""
保存数据：金币
展示私网地址
添加超管
"""
nonebot.load_plugins("src/plugins/Super")
# 菜单
"""
"""
nonebot.load_plugins("src/plugins/Menu")


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
