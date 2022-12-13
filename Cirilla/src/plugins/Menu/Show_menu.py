from nonebot.rule import to_me
from nonebot import on_command
from Cirilla.tool.Menu import load_file, save_file
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11

show = on_command("菜单内容", rule=to_me(), priority=1, block=True)


@show.handle()
async def check_super_and_show(private_event: v11.PrivateMessageEvent):
    """
    检查权限

    :param private_event: 私聊事件
    """
    # 获取id
    player_id = private_event.user_id
    if player_id in SUPER_ADMIN.values():
        menu_info = load_file()
        await show.finish(f"高级：{menu_info['super']}\n"
                          f"普通：{menu_info['common']}")
    else:
        await show.finish("你权限不足")
