from nonebot import on_command
from Cirilla.tool.Money.control_money import *
import nonebot.adapters.onebot.v11 as v11
import random,time
import sys

sys.path.append("../")
sign = on_command("签到", priority=5, block=True)


@sign.handle()
async def player_sign(group_event: v11.GroupMessageEvent):
    """
    玩家签到

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    player_name = group_event.sender.nickname
    # 生成金币数量和签到时间
    money_mount = random.randint(0, 100)
    time_info = time.strftime("%y-%m-%d")
    # 判断是否首次签到
    try:
        player_last_sign_time = PLAYER_MONEY.get(player_id)["签到时间"]
    except TypeError:
        player_last_sign_time = time_info + "1"
    # 判断签到时间
    if player_last_sign_time < time_info:
        add_money(player_id, money_mount, time_info)
        await sign.send(f"{player_name} 签到成功\n给你{money_mount}枚金币")
    elif player_last_sign_time == time_info:
        await sign.send(f"{player_name} 你今天签到过了")
    else:
        PLAYER_MONEY.update({
            player_id: {
                "签到时间": time_info,
                "金币数量": money_mount
            }
        })
        await sign.send(f"{player_name} 签到成功\n给你{money_mount}枚金币")

