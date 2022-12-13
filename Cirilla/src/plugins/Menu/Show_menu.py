from nonebot.internal.params import ArgStr
from nonebot.rule import to_me
from nonebot import on_command
from PIL import Image, ImageDraw, ImageFont
from Cirilla.tool.Menu import load_file
from Cirilla.tool.Menu.control_menu import show_menu_to_player
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11

menu_common = on_command("菜单", priority=1, block=True)
menu_super = on_command("高级菜单", rule=to_me(), priority=1, block=True)


@menu_common.handle()
async def common_menu(bot: v11.Bot, group_event: v11.GroupMessageEvent):
    """
    展示普通菜单

    :param bot: 机器人
    :param group_event: 群聊事件
    """
    # 获取id
    group_id = group_event.group_id
    # 展示菜单
    cq_txt = show_menu_to_player('common')
    if cq_txt == "404":
        await menu_common.finish("菜单还未生成")
    await bot.send_group_msg(group_id=group_id, message=cq_txt)
    await menu_common.finish()


@menu_super.handle()
async def check_super(private_event: v11.PrivateMessageEvent):
    """
    检查权限

    :param private_event: 私聊事件
    """
    # 获取id
    player_id = private_event.user_id
    # 判断权限
    if player_id in SUPER_ADMIN.values():
        pass
    else:
        await menu_super.finish("你权限不足")


@menu_super.handle()
async def super_menu(bot: v11.Bot, private_event: v11.PrivateMessageEvent):
    """
    展示高级菜单

    :param bot: 机器人
    :param private_event: 私聊事件
    """
    # 获取id
    player_id = private_event.user_id
    # 展示菜单
    cq_txt = show_menu_to_player('super')
    if cq_txt == "404":
        await menu_super.finish("菜单还未生成")
    await bot.send_private_msg(user_id=player_id, message=cq_txt)
    await menu_super.finish()
