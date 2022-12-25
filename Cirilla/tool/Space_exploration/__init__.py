"""
本模块负责处理玩家宇宙探索相关业务
读取所有玩家注册信息: SPACE_SIGN
SPACE_SIGN结构
{
    “id”："名称"
}

函数：


模块：

"""
import json, os
from Cirilla.tool.Log import control

path = "tool/Money/player_sign.json"


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
        info_json = json.dumps(SPACE_SIGN, ensure_ascii=False)
        file.write(info_json)


# 判断路径
if os.path.exists(path):
    # 读取
    SPACE_SIGN = load_file()
else:
    control("SUCCESS", "Space", "Space包检测到缺少player_sign.json,已创建")
    with open(path, "w+", encoding="utf8") as f:
        f.write(json.dumps({}))
    # 读取
    SPACE_SIGN = load_file()
