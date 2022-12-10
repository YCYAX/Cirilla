from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import ArgPlainText
from Cirilla.tool.Super import SUPER_ADMIN
from Cirilla.tool.Super.control_admin import add_super
import nonebot.adapters.onebot.v11 as v11

add = on_command("添加超管", rule=to_me(), priority=5, block=True)


@add.handle()
async def check_is_first_add():
    """检查是否为第一次添加"""
    if SUPER_ADMIN:
        pass
    else:
        await add.send("第一次添加超管用户")


@add.got("add", prompt="输入一个想要添加的超管qq号")
async def add_super_admin(private_event: v11.PrivateMessageEvent, add_id: int = ArgPlainText("add")):
    """
    添加超管用户

    :param private_event: 私聊事件
    :param add_id: 添加id
    """
    # 获取玩家id
    player_id = private_event.user_id
    # 判断是否为超管
    if player_id in SUPER_ADMIN:
        # 添加
        add_super(add_id, str(player_id))
        await add.finish(f"添加用户{add_id}为超管")
    else:
        # 添加
        add_super(add_id)
        await add.finish(f"添加用户{add_id}为超管")
