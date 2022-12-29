from nonebot import on_command
from nonebot.params import CommandArg, ArgStr, Message
from nonebot.matcher import Matcher
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11
from Cirilla.tool.Space_exploration.planet_map_make import make_map
import numpy

move = on_command("移动", priority=1, block=True)


@move.handle()
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
        await move.finish("你不在星系中")
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("move_pos", args)


@move.got("move_pos", prompt="输入移动方向行与列\n例如：移动 2 5")
async def player_move(group_event: v11.GroupMessageEvent, move_pos: str = ArgStr("move_pos")):
    """
    玩家移动

    :param group_event: 群聊事件
    :param move_pos: 移动到的位置
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 处理输入信息
    move_pos = move_pos.split()
    move_info = move_pos
    if len(move_pos) != 2:
        await move.finish(f"输入的参数过多")
    if "".join(move_pos).isnumeric():
        pass
    else:
        await move.finish(f"输入的数据不符合格式")
    # 分出行与列
    row = int(move_info[0])
    column = int(move_info[1])
    # 读取星球大小
    planet_size = SPACE_PLANET[player_pos]['planet_size']
    # 判断输入值是否超限
    if row > planet_size - 1 or column > planet_size - 1:
        await move.finish(f"输入的数据大于星球最大尺寸")
    # 读取地图
    planet_map = SPACE_PLANET[player_pos]['planet_map']
    planet_map = numpy.reshape(planet_map, (planet_size, planet_size)).astype('U256')
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
    await move.finish(f"{player_pos}地图({row},{column})\n{new_map}")


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
