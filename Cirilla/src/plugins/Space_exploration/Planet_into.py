from nonebot import on_command
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11
from nonebot.internal.params import ArgStr
from Cirilla.tool.Space_exploration.planet_map_make import make_map
import random,numpy

into = on_command("进入星球", priority=1, block=True)


@into.handle()
async def check_player(group_event: v11.GroupMessageEvent):
    """
    检查玩家

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家状态
    state = SPACE_SIGN[player_id]['state']
    if state == 'galaxy':
        pass
    else:
        await into.finish("你不在星系中")


@into.got("planet_name", prompt="输入星球名字")
async def into_planet(group_event: v11.GroupMessageEvent, planet: str = ArgStr("planet_name")):
    """
    进入星球

    :param group_event: 群聊事件
    :param planet: 星球名字
    """
    # 判断用户状态
    if planet in SPACE_PLANET:
        pass
    else:
        await into.finish("该星球不存在")
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 获取星球信息
    planet_size = SPACE_PLANET[planet]['planet_size']
    planet_weather = SPACE_PLANET[planet]['planet_weather']
    planet_state = SPACE_PLANET[planet]['planet_state']
    # 判断星球状态并生成
    if planet_state:
        planet_map = SPACE_PLANET[planet]['planet_map']
        planet_map = numpy.reshape(planet_map, (planet_size, planet_size))
    else:
        planet_map = make_map(planet_size)
        SPACE_PLANET[planet]['planet_state'] = True
        SPACE_PLANET[planet]['planet_map'] = planet_map.tolist()
    # 生成坐标
    row = random.randint(0, planet_size-1)
    column = random.randint(0, planet_size-1)
    await into.send(f"玩家 {player_name},降落在星球的位置 {row, column}")
    # 替换地图位置
    show_system_map = planet_map
    old_map = show_system_map
    old_map[row][column] = "♚"
    # 判断行列大小
    if row < 3 and column < 3:
        new_map = old_map[0:row + 4, 0:column + 4]
    elif row < 3:
        new_map = old_map[0:row + 4, column - 3:column + 4]
    elif column < 3:
        new_map = old_map[row - 3:row + 4, 0:column + 4]
    else:
        new_map = old_map[row - 3:row + 4, column - 3:column + 4]
    # 更改状态
    SPACE_PLANET[planet]['planet_state'] = 'planet'
    await into.finish(f"{planet}地图\n{new_map}")
