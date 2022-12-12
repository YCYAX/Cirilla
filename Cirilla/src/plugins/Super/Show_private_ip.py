from nonebot import on_command
from nonebot.rule import to_me
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11
import socket

ip = on_command("私网地址", rule=to_me(), priority=5, block=True)


@ip.handle()
async def show_ip(private_event: v11.PrivateMessageEvent):
    """
    显示当前bot服务器内网地址

    :param private_event: 私聊事件
    """
    # 获取玩家id
    player_id = private_event.user_id
    # 判断权限
    if player_id in SUPER_ADMIN.values():
        private_ip = socket.gethostbyname(socket.gethostname())
        await ip.finish(f"内网地址：{private_ip}")
    else:
        await ip.finish("你权限不足")
