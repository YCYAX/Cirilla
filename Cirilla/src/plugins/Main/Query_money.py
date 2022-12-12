from nonebot import on_command
from Cirilla.tool.Money import PLAYER_MONEY
from Cirilla.tool.Money.control_money import query_money
import nonebot.adapters.onebot.v11 as v11

query = on_command("我的金币", priority=1, block=True)


@query.handle()
async def query_player_money(group_event: v11.GroupMessageEvent):
    """
    查询玩家金币

    :param group_event: 群聊事件
    """
    # 获取玩家id
    player_id = group_event.user_id
    player_name = group_event.sender.nickname
    # 判断是否注册
    try:
        mount = query_money(str(player_id))
        await query.finish(f"{player_name} 的金币数量：{mount}")
    except KeyError:
        await query.finish(f"{player_name} 还没有使用过本bot,请先签到")
