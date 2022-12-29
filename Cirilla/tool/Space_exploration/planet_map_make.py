import numpy, random


def make_map(size: int):
    """
    生成地图

    :param size: 地图尺寸大小

    :return: 地图数值
    """
    # 生成空数组
    map = numpy.array([], dtype='object')

    def make_map_row(size: int) -> list:
        """
        生成地图的行

        :param size: 地图尺寸大小

        :return: 地图行数值
        """
        # 生成文字
        txt = "金木水火土"
        # 空行列表
        map = []
        # 生成一行
        for i in range(size):
            index = random.randint(0, 4)
            map.append(txt[index])
        return map

    # 生成所有地图-列
    for i in range(size):
        map = numpy.append(map, [make_map_row(size)])
    # 确定形状
    map = numpy.reshape(map, (size, size))
    return map
