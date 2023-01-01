from nonebot import on_command
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11

leave = on_command("离开星球", priority=1, block=True)


@leave.handle()
async def player_leave(group_event: v11.GroupMessageEvent):
    """
    检查玩家

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家状态
    state = SPACE_SIGN[player_id]['state']
    if state == 'planet':
        pass
    else:
        await leave.finish("你不在星球中")
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 获取星球所在星系
    galaxy_name = SPACE_PLANET[player_pos]["planet_galaxy"]
    # 设置玩家状态
    SPACE_SIGN[player_id]['state'] = "galaxy"
    SPACE_SIGN[player_id]['pos'] = galaxy_name
    await leave.finish(f"玩家 {player_name} 回到当前星球所在星系 {galaxy_name}")
