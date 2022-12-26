"""
本模块负责处理玩家宇宙探索相关业务
读取所有玩家注册信息: SPACE_SIGN
读取所有星球信息: SPACE_PLANET
SPACE_SIGN结构
{
    "id": {
        "name": "玩家昵称",
        "pos": "星系名字",
        "state": "玩家状态"
    }
}
SPACE_GALAXY结构
{
    "星系名字": {
        "galaxy_pos": [宇宙坐标],
        "galaxy_size": 星系内星球数量
    }
}
函数：
load_file -> 加载json到内存
save_file -> 保存内容至json
模块：
galaxy_make.py -> 生成星系
"""
import json, os
from Cirilla.tool.Log import control

player_sign_path = "tool/Space_exploration/player_sign.json"
planet_path = "tool/Space_exploration/planet.json"
galaxy_path = "tool/Space_exploration/galaxy.json"

path_list = [planet_path, galaxy_path, player_sign_path]


def load_file(path) -> dict:
    """
    加载json到内存
    """
    with open(path, "r", encoding="utf8") as file:
        info = file.read()
        player_json = json.loads(info)
        return player_json


def save_file(path,info):
    """
    保存内容至json
    """
    with open(path, "w", encoding="utf8") as file:
        info_json = json.dumps(info, ensure_ascii=False)
        file.write(info_json)


for path in path_list:
    # 判断路径
    if os.path.exists(path):
        # 读取
        if path == player_sign_path:
            SPACE_SIGN = load_file(path)
        elif path == planet_path:
            SPACE_PLANET = load_file(path)
        elif path == galaxy_path:
            SPACE_GALAXY = load_file(path)
    else:
        control("SUCCESS", "Space", "Space包检测到缺少" + path + "已创建")
        with open(path, "w+", encoding="utf8") as f:
            f.write(json.dumps({}))
        # 读取
        if path == player_sign_path:
            SPACE_SIGN = load_file(path)
        elif path == planet_path:
            SPACE_PLANET = load_file(path)
        elif path == galaxy_path:
            SPACE_GALAXY = load_file(path)
