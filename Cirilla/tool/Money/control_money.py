import json
from Cirilla.tool.Money import PLAYER_MONEY

path = "tool/Money/money.json"


def add_money(user_id: int, money_mount: int):
    """
    给玩家添加金钱

    :param user_id: 玩家qq
    :param money_mount: 金钱数量
    """
    old_mount = PLAYER_MONEY[user_id]
    new_mount = old_mount + money_mount
    PLAYER_MONEY[user_id] = new_mount
