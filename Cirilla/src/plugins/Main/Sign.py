from nonebot import on_command
from Cirilla.tool.Money import PLAYER_MONEY
from Cirilla.tool.Money.control_money import *
import nonebot.adapters.onebot.v11 as v11
import random

sign = on_command("签到", priority=5, block=True)


@sign.handle()
async def player_sign(group_event: v11.GroupMessageEvent):
    """
    玩家签到

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = group_event.user_id
    player_name = group_event.sender.nickname
    # 生成金币数量
    money_mount = random.randint(0, 100)
    # 添加金币
    if PLAYER_MONEY.get(player_id):
        add_money(player_id, money_mount)
    else:
        PLAYER_MONEY.update({
            player_id: money_mount
        })
    await sign.send(f"{player_name} 签到成功\n给你{money_mount}枚金币")

