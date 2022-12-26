from nonebot import on_command
import nonebot.adapters.onebot.v11 as v11


help = on_command("宇宙帮助", priority=1, block=True)


@help.handle()
async def help_show(group_event: v11.GroupMessageEvent):
    """
    帮助菜单

    :param group_event: 群聊事件
    """
    txt = "|登录宇宙|加入宇宙探索游戏|\n" \
          "|进入星系|进入一个星系|\n" \
          "|进入星球|进入一个星球|\n" \
          "|星系信息|查看当前星系信息|\n"
    await help.finish(f"{txt}")