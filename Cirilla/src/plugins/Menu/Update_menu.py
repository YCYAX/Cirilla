from nonebot.internal.params import ArgStr
from nonebot.rule import to_me
from nonebot import on_command
from Cirilla.tool.Menu import load_file, save_file
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11

up_menu = on_command("更新菜单", rule=to_me(), priority=1, block=True)


@up_menu.handle()
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
        await up_menu.finish("你权限不足")


@up_menu.got("up", prompt="输入你想增加的菜单类型和文字\n例如：普通/高级 签到")
async def up_data(info: str = ArgStr("up")):
    """
    更新菜单

    :param info: 命令后参数
    """

    async def update_menu(menu_type: str, info: str):
        """
        更新菜单内容

        :param menu_type: 菜单类型
        :param info: 文字信息
        """
        # 判断菜单类型
        if menu_type == "普通":
            menu_type = 'common'
        elif menu_type == "高级":
            menu_type = 'super'
        else:
            await up_menu.finish("菜单类型错误")
            pass
        # 加载菜单并更新
        menu_info = load_file()
        menu_list: list = menu_info[menu_type]
        menu_list.append(info)
        # 排序存入,最长的放在第0位
        menu_list.sort(key=lambda i: len(i), reverse=True)
        save_file(menu_info)
        await up_menu.send("添加成功")
        await up_menu.finish(f"高级：{menu_info['super']}\n"
                             f"普通：{menu_info['common']}")

    # 获取输入信息
    info_list = info.split(" ")
    try:
        await update_menu(info_list[0], info_list[1])
    except IndexError:
        await up_menu.finish("输入格式错误")
