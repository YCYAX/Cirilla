from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import ArgStr
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11
import json

broadcast = on_command("广播", rule=to_me(), priority=1, block=True)


@broadcast.handle()
async def check_player(private_event: v11.PrivateMessageEvent):
    """
    检查是否为超管

    :param private_event: 私聊事件
    """
    # 判断是否为超管
    if int(private_event.user_id) in SUPER_ADMIN.values():
        pass
    else:
        await broadcast.finish("你权限不足")


@broadcast.got("message", prompt="输入广播信息")
async def add_super_admin(bot: v11.Bot, info: str = ArgStr("message")):
    """
    广播消息

    :param bot: 机器人
    :param info: 广播信息
    """
    group_json = await bot.get_group_list()
    for i in group_json:
        await bot.send_msg(group_id=int(i['group_id']), message=info)
    await broadcast.finish("广播成功")
