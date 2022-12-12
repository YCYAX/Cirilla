from Cirilla.tool.Money import PLAYER_MONEY
import sys

sys.path.append("../")
path = "tool/Money/money.json"


def add_money(user_id: str, money_mount: int, time_info:str):
    """
    给玩家添加金钱

    :param user_id: 玩家qq
    :param money_mount: 金钱数量
    :param time_info: 签到时间
    """
    old_mount = PLAYER_MONEY[user_id]["金币数量"]
    new_mount = old_mount + money_mount
    PLAYER_MONEY[user_id]["金币数量"] = new_mount
    PLAYER_MONEY[user_id]["签到时间"] = time_info
