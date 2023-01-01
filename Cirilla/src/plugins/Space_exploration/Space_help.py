from nonebot import on_command


help = on_command("宇宙帮助", priority=1, block=True)


@help.handle()
async def help_show():
    """
    帮助菜单
    """
    txt = "|登录宇宙|加入宇宙探索游戏|\n" \
          "|进入星系|进入一个星系|\n" \
          "|进入星球|进入一个星球|\n" \
          "|星系信息|查看当前星系信息|\n" \
          "|移动|在星球上移动位置|\n" \
          "|离开星球|离开星球回到星系|"

    await help.finish(f"{txt}")
