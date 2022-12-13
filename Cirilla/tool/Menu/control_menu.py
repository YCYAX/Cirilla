"""
函数：
show_menu_to_player() -> 给玩家展示菜单
"""
from Cirilla.tool.Conversion import image_base64


def show_menu_to_player(menu_type: str):
    path = "photo/output/" + menu_type + ".jpg"
    image = image_base64(path)
    cq_str = "[CQ:image,file=base64://" + image + "]"
    return cq_str
