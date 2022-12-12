"""
本包负责处理输出控制台日志相关业务

函数：
control() -> 打印日志到控制台
"""
import time


def control(info_type: str, plugin_name: str, info: str):
    """
    打印日志到控制台

    :param info_type: 信息提示类型
    :param plugin_name: 输出的插件名称
    :param info: 输出的提示信息
    """
    time_info = time.strftime("%m-%d %H:%M:%S")
    print(f"\033[0;32;8m{time_info}\033[0m "
          f"[\033[1;37;8m{info_type}\033[0m] "
          f"\033[4;36;8m{plugin_name}\033[0m "
          f"| {info}")
