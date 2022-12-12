"""
本模块负责处理玩家金钱相关业务
读取所有玩家金钱: PLAYER_MONEY
PLAYER_MONEY结构
{
    “id”：{
        “签到时间”：str
        “金币数量”：int
    }
}

函数：
save_file() -> 保存内容至money.json

模块：
control_money.py -> 对玩家金钱进行操作
"""
import json, os
from Cirilla.tool.Log import control

path = "tool/Money/money.json"


def load_file() -> dict:
    """
    加载money.json内容到内存
    """
    with open(path, "r", encoding="utf8") as file:
        info = file.read()
        player_json = json.loads(info)
        return player_json


def save_file():
    """
    保存内容至money.json
    """
    with open(path, "w", encoding="utf8") as file:
        info_json = json.dumps(PLAYER_MONEY, ensure_ascii=False)
        file.write(info_json)


# 判断路径
if os.path.exists(path):
    # 读取
    PLAYER_MONEY = load_file()
else:
    control("SUCCESS", "Money", "Money包检测到缺少money.json,已创建")
    with open(path, "w+", encoding="utf8") as f:
        f.write(json.dumps({}))
    # 读取
    PLAYER_MONEY = load_file()
