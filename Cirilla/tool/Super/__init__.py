import json
import os

from Cirilla.tool.Log import control

path = "src/Super/admin.json"


def load_file() -> dict:
    """
    加载admin.json内容至内存
    """
    with open(path, "r") as file:
        info = file.read()
        player_json = json.loads(info)
        return player_json


def save_file():
    """
    保存内容至admin.json
    """
    with open(path, "w") as file:
        info_json = json.dumps(SUPER_ADMIN)
        file.write(info_json)


# 判断路径
if os.path.exists(path):
    # 加载
    SUPER_ADMIN = load_file()
else:
    control("SUCCESS", "Save", "Save检测到缺少admin.json,已创建")
    with open(path, "w+") as f:
        f.write(json.dumps({}))
    # 加载
    SUPER_ADMIN = load_file()
