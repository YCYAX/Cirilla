from nonebot import on_command
from Cirilla.tool.Space_exploration.planet_make import Planet
from Cirilla.tool.Space_exploration import *
import nonebot.adapters.onebot.v11 as v11

show = on_command("星系信息", priority=1, block=True)


@show.handle()
async def show_galaxy(group_event: v11.GroupMessageEvent):
    """
    查看星系

    :param group_event: 群聊事件
    """
    # 获取玩家名字和id
    player_id = str(group_event.user_id)
    # 获取玩家宇宙信息
    player_name = SPACE_SIGN[player_id]['name']
    player_pos = SPACE_SIGN[player_id]['pos']
    # 获取玩家状态
    state = SPACE_SIGN[player_id]['state']
    # 获取星系状态
    galaxy_state = SPACE_GALAXY[player_pos]['galaxy_state']
    galaxy_planet: list = SPACE_GALAXY[player_pos]['galaxy_planet']
    galaxy_size = SPACE_GALAXY[player_pos]['galaxy_size']
    # 判断状态
    if state == 'galaxy':
        pass
    else:
        await show.finish("你不在星系中")
    # 判断是否生成星球
    if galaxy_state:
        pass
    else:
        # 生成星球
        for i in range(galaxy_size):
            planet_info = Planet(player_pos).__dict__
            SPACE_PLANET.update({
                planet_info["planet_name"]: planet_info
            })
            galaxy_planet.append(planet_info["planet_name"])
        SPACE_GALAXY[player_pos]['galaxy_state'] = True
    txt = ""
    index_number = 0
    for planet in galaxy_planet:
        index_number += 1
        txt += str(index_number) + "." +planet+"\n"
    await show.send(f"玩家 {player_name},所在星系 {player_pos}\n星球有:\n{txt}")
