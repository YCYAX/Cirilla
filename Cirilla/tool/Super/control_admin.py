"""
函数：
add_super() -> 添加bot超管用户
"""

from Cirilla.tool.Super import SUPER_ADMIN, save_file

path = "tool/Super/admin.json"


def add_super(user_id: int, control: str = "super"):
    """
    添加bot超管用户

    :param user_id: 玩家qq
    :param control: 操作玩家
    """
    SUPER_ADMIN.update({
        control: user_id
    })
    save_file()
