from nonebot import on_command
from nonebot.rule import to_me
from Cirilla.tool.Money import save_file
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11
import sys

sys.path.append("../")
save = on_command("保存数据", rule=to_me(), priority=5, block=True)


@save.handle()
async def save_data(private_event: v11.PrivateMessageEvent):
    """
    保存数据

    :param private_event: 私聊事件
    """
    # 判断是否为超管
    if int(private_event.user_id) in SUPER_ADMIN.values():
        save_file()
        await save.finish("所有玩家金币保存成功")
    else:
        await save.finish("你不是超级管理员")
