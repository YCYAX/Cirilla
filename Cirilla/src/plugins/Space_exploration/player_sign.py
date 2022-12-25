from nonebot import on_command
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11

sign = on_command("登录宇宙", priority=1, block=True)

@sign.handle()
async def player_sign(group_event: v11.GroupMessageEvent):
    """
    玩家签到

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    player_name = group_event.sender.nickname
    # 判断是否首次登录
    if player_id in SPACE_SIGN:
        await sign.finish(f"欢迎回来！ {SPACE_SIGN[player_id]} 冒险者")
    else:
        if player_name in SPACE_SIGN.values():
            SPACE_SIGN.update({
                player_id: player_name + "#" + player_id[-4:]
            })
            save_file()
        else:
            SPACE_SIGN.update({
                player_id: player_name
            })
            save_file()
        await sign.send(f"欢迎加入宇宙！ {SPACE_SIGN[player_id]} 冒险者，回复 宇宙帮助 来开始探索吧")

