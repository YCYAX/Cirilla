import time


def control(info_type: str, plugin_name: str, info: str):
    time_info = time.strftime("%m-%d %H:%M:%S")
    print(f"{time_info} [{info_type} {plugin_name} | {info}")
