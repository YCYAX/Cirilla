"""
函数：
show_menu_to_player() -> 给玩家展示菜单
"""
import os
from Cirilla.tool.Conversion import image_base64


def show_menu_to_player(menu_type: str) -> str:
    """
    给玩家展示菜单
    :param menu_type: 菜单类型
    :return: cq码
    """
    path = "photo/output/" + menu_type + ".jpg"
    if os.path.exists(path):
        image = image_base64(path)
        cq_str = "[CQ:image,file=base64://" + image + "]"
        return cq_str
    else:
        return "404"
