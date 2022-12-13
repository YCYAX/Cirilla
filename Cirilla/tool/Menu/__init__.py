"""
本模块负责处理菜单相关业务
结构
{
    "common"：[功能1，功能2，....],
    "super": [功能1，功能2，....]
}

函数：
load_file() -> 加载menu.json内容
save_file() -> 保存内容至menu.json
"""
import json, os
from Cirilla.tool.Log import control

path = "tool/Menu/menu.json"


def load_file() -> dict:
    """
    加载menu.json内容
    """
    with open(path, "r", encoding="utf8") as file:
        info = file.read()
        menu_json = json.loads(info)
        return menu_json


def save_file(info: dict):
    """
    保存内容至money.json
    :param info: 所有菜单内容
    """
    with open(path, "w", encoding="utf8") as file:
        info_json = json.dumps(info, ensure_ascii=False)
        file.write(info_json)


# 判断路径
if os.path.exists(path):
    pass
else:
    control("SUCCESS", "Menu", "Menu包检测到缺少menu.json,已创建")
    with open(path, "w+", encoding="utf8") as f:
        f.write(json.dumps({
            "common": [],
            "super": []
        }))
