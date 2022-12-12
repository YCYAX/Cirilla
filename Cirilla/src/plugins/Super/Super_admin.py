from nonebot import on_command
from nonebot.rule import to_me
from nonebot.params import ArgStr
from Cirilla.tool.Super import SUPER_ADMIN
from Cirilla.tool.Super.control_admin import add_super
import nonebot.adapters.onebot.v11 as v11

add = on_command("添加超管", rule=to_me(), priority=1, block=True)


@add.handle()
async def check_is_first_add():
    """检查是否为第一次添加"""
    if SUPER_ADMIN:
        pass
    else:
        await add.send("第一次添加超管用户")


@add.got("add", prompt="输入一个想要添加的超管qq号")
async def add_super_admin(private_event: v11.PrivateMessageEvent, add_id: int = ArgStr("add")):
    """
    添加超管用户

    :param private_event: 私聊事件
    :param add_id: 添加id
    """
    # 获取玩家id
    player_id = private_event.user_id
    # 判断是否为空字典
    if SUPER_ADMIN:
        # 判断是否为超管
        if player_id in SUPER_ADMIN.values():
            # 添加
            add_super(int(add_id), str(player_id))
            await add.finish(f"添加用户{add_id}为超管")
        else:
            await add.finish(f"你权限不足")
    else:
        # 添加
        add_super(int(add_id))
        await add.finish(f"添加用户{add_id}为超管")
