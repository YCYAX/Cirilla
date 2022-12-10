"""
本模块负责处理玩家金钱相关业务
读取所有玩家金钱: PLAYER_MONEY
"""
import json, os
from Cirilla.no_load.Log import control

path = "tool/Money/money.json"


def load_file() -> dict:
    """
    加载money.json内容到内存
    """
    with open(path, "r") as file:
        info = file.read()
        player_json = json.loads(info)
        return player_json


if os.path.exists(path):
    PLAYER_MONEY = load_file()
else:
    control("SUCCESS", "Money", "Money包检测到缺少money.json,已创建")
    with open(path, "w+") as f:
        f.write(json.dumps({}))
    PLAYER_MONEY = load_file()