import json
from Cirilla.tool.Super import SUPER_ADMIN, save_file

path = "src/Super/admin.json"


def add_super(user_id: int):
    """
    添加bot超管用户

    :param user_id: 玩家qq
    """
    SUPER_ADMIN.update({
        user_id
    })
    save_file()
