from nonebot import on_command
from Cirilla.tool.Space_exploration.galaxy_make import Galaxy
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11


into = on_command("进入星系", priority=1, block=True)


@into.handle()
async def check_pos(group_event: v11.GroupMessageEvent):
    """
    检查位置

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 获取玩家状态
    state = SPACE_SIGN[player_id]['state']
    # 判断状态
    if state == 'sign':
        pass
    else:
        await into.finish("你还没有登录，请使用 登录宇宙 命令")
    # 判断位置
    if player_pos is None:
        galaxy_info = Galaxy(player_name).__dict__
        await into.send(f"冒险家 {player_name} ，所在星系 {galaxy_info['galaxy_name']}，所在宇宙位置 {galaxy_info['galaxy_pos']}")
        SPACE_GALAXY.update({
                galaxy_info['galaxy_name']: galaxy_info
            })
        SPACE_SIGN[player_id]['pos'] = galaxy_info['galaxy_name']
        SPACE_SIGN[player_id]['state'] = "galaxy"
    else:
        galaxy_info = SPACE_GALAXY[player_pos]
        SPACE_SIGN[player_id]['state'] = "galaxy"
        await into.send(f"冒险家 {player_name} ，所在星系 {player_pos}，所在宇宙位置 {galaxy_info['galaxy_pos']}")