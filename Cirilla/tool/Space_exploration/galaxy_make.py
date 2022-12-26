import random
from Cirilla.tool.Space_exploration import *


class Galaxy:
    """
    星系生成
    """

    def __init__(self, first_name):
        # 随机后名字
        range_number = random.randint(2, 8)
        last_name = ""
        yes_or_no = True
        while yes_or_no:
            for i in range(range_number):
                index = random.randint(0, 35)
                last_name += "QWERTYUIOPASDFGHJKLZXCVBNM0147852369"[index]
            if last_name in SPACE_GALAXY:
                pass
            else:
                yes_or_no = False
        # 星系名字
        self.galaxy_name = first_name + " " + last_name
        # 星系内含星球
        self.galaxy_size = random.randint(2, 10)
        # 星系在宇宙中的坐标
        self.galaxy_pos = (random.randint(0, 1000), random.randint(0, 1000))
