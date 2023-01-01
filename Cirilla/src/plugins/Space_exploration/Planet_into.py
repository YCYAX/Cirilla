from nonebot import on_command
from nonebot.params import CommandArg, ArgStr, Message
from nonebot.matcher import Matcher
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11
from Cirilla.tool.Space_exploration.planet_map_make import make_map
import random, numpy

into = on_command("进入星球", priority=1, block=True)


@into.handle()
async def check_player(matcher: Matcher, group_event: v11.GroupMessageEvent, args: Message = CommandArg()):
    """
    检查玩家

    :param matcher: 事件响应器
    :param group_event: 群聊事件
    :param args: 命令信息
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家状态
    state = SPACE_SIGN[player_id]['state']
    if state == 'galaxy':
        pass
    else:
        await into.finish("你不在星系中")
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("planet_name", args)


@into.got("planet_name", prompt="输入星球名字/序列号")
async def into_planet(group_event: v11.GroupMessageEvent, planet: str = ArgStr("planet_name")):
    """
    进入星球

    :param group_event: 群聊事件
    :param planet: 星球名字
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 判断是否为序列号
    if planet.isnumeric():
        try:
            planet = SPACE_GALAXY[player_pos]["galaxy_planet"][int(planet) - 1]
        except IndexError:
            await into.finish("输入的序号大于此星系星球数量")
    else:
        # 判断是否存在
        if planet in SPACE_GALAXY[player_pos]["galaxy_planet"]:
            pass
        else:
            await into.finish("此星系不存在该星球")
    # 获取星球信息
    planet_size = SPACE_PLANET[planet]['planet_size']
    planet_weather = SPACE_PLANET[planet]['planet_weather']
    planet_state = SPACE_PLANET[planet]['planet_state']
    # 判断星球状态并生成
    if planet_state:
        planet_map = SPACE_PLANET[planet]['planet_map']
        planet_map = numpy.reshape(planet_map, (planet_size, planet_size)).astype('U256')
    else:
        planet_map = make_map(planet_size)
        SPACE_PLANET[planet]['planet_state'] = True
        SPACE_PLANET[planet]['planet_map'] = planet_map.tolist()
    # 生成坐标
    row = random.randint(0, planet_size - 1)
    column = random.randint(0, planet_size - 1)
    await into.send(f"玩家 {player_name},降落在星球的位置 {row, column}")
    # 替换地图位置
    show_system_map = planet_map
    old_map = show_system_map
    old_map[row][column] = "♚"
    # 判断行列大小
    first_index = set_map_pos(row, planet_size)
    second_index = set_map_pos(column, planet_size)
    # 划出基本地图范围
    new_map = old_map[first_index[0]:first_index[1], second_index[0]:second_index[1]]
    # 增加行
    row_list = ["r/c", ]
    for i in range(new_map.shape[1]):
        row_list.append(second_index[1] - (new_map.shape[1] - i))
    # 增加列
    column_list = []
    for i in range(new_map.shape[0]):
        column_list.append(first_index[1] - (new_map.shape[0] - i))
    # 插入
    new_map = numpy.insert(new_map, 0, column_list, axis=1)  # 列
    new_map = numpy.insert(new_map, 0, row_list, axis=0)  # 行
    # 修改位置并设置状态
    SPACE_SIGN[player_id]['pos'] = planet
    SPACE_SIGN[player_id]['state'] = "planet"
    await into.finish(f"{planet}地图\n{new_map}")


def set_map_pos(pos, max_number) -> list[int, int]:
    """
    设置行列值取值范围

    :param pos: 所在行数/列数
    :param max_number: 地图最大值
    """
    if pos < 2:
        return [0, pos + 3]
    if pos > max_number - 3:
        return [pos - 2, max_number]
    else:
        return [pos - 2, pos + 3]
