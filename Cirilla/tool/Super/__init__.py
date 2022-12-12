"""
本模块负责处理玩家高级权限相关业务
读取所有高级权限玩家: SUPER_ADMIN

SUPER_ADMIN结构:
{
    “super”：id int
    “id”： id int
}

函数：
save_file() -> 保存内容至admin.json

模块：
control_admin.py -> 对管理员进行操作
"""
import json
import os

from Cirilla.tool.Log import control

path = "tool/Super/admin.json"


def load_file() -> dict:
    """
    加载admin.json内容至内存
    """
    with open(path, "r", encoding="utf8") as file:
        info = file.read()
        player_json = json.loads(info)
        return player_json


def save_file():
    """
    保存内容至admin.json
    """
    with open(path, "w", encoding="utf8") as file:
        info_json = json.dumps(SUPER_ADMIN)
        file.write(info_json)


# 判断路径
if os.path.exists(path):
    # 加载
    SUPER_ADMIN = load_file()
else:
    control("SUCCESS", "Save", "Save检测到缺少admin.json,已创建")
    with open(path, "w+", encoding="utf8") as f:
        f.write(json.dumps({}))
    # 加载
    SUPER_ADMIN = load_file()
