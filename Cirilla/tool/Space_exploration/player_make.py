from ..Space_exploration import *


class Player:
    def __init__(self, name, id):
        # 玩家注册账号
        self.id = id
        # 玩家名字
        # 判断名字是否重复
        if name in SPACE_SIGN.values():
            self.name = name + "#" + id[-4:],
        else:
            self.name = name
        # 玩家位置
        self.pos = None
        # 玩家状态
        self.state = 'sign'
        # 玩家生命值
        self.health = 100
        # 玩家魔法值
        self.intelligence = 100
        # 玩家气力值
        self.strength = 100
        # 玩家氧气值
        self.oxygen = 100
        # 玩家防御值
        self.defense = 100
        # 玩家攻击值
        self.atk = 100
        # 玩家敏捷值
        self.speed = 100
        # 玩家洞察值
        self.watch = 100
        # 玩家经验值
        self.exp = 0
        # 玩家等级
        self.level = 0
