import json
from Cirilla.tool.Money import PLAYER_MONEY

path = "tool/Money/money.json"


def add_money(user_id: int, money_mount: int):
    old_mount = PLAYER_MONEY[user_id]
    new_mount = old_mount + money_mount
    PLAYER_MONEY[user_id] = new_mount
