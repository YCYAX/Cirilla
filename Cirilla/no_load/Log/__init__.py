import time


def control(info_type: str, plugin_name: str, info: str):
    time_info = time.strftime("%m-%d %H:%M:%S")
    print(f"\033[0;32;8m{time_info}\033[0m "
          f"[\033[1;37;8m{info_type}\033[0m] "
          f"\033[4;36;8m{plugin_name}\033[0m "
          f"| {info}")
