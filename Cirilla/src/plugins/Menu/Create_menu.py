from nonebot.internal.params import ArgStr
from nonebot.rule import to_me
from nonebot import on_command
from PIL import Image, ImageDraw, ImageFont
from Cirilla.tool.Menu import load_file
from Cirilla.tool.Super import SUPER_ADMIN
import nonebot.adapters.onebot.v11 as v11

create = on_command("生成菜单", rule=to_me(), priority=1, block=True)


@create.handle()
async def check_super(private_event: v11.PrivateMessageEvent):
    """
    检查权限

    :param private_event: 私聊事件
    """
    # 获取id
    player_id = private_event.user_id
    # 判断权限
    if player_id in SUPER_ADMIN.values():
        pass
    else:
        await create.finish("你权限不足")


@create.got("create_info", prompt="输入你想生成的菜单类型和字号\n例如：普通/高级 30")
async def create_menu(arg_info: str = ArgStr("create_info")):
    """
    更新菜单

    :param arg_info: 命令后参数
    """
    # 获取输入信息
    info_list = arg_info.split(" ")
    try:
        menu_type = info_list[0]
        ttf_size = int(info_list[1])
    except IndexError:
        await create.finish("输入格式错误")
    # 判断菜单类型
    if menu_type == "普通":
        menu_type = 'common'
    elif menu_type == "高级":
        menu_type = 'super'
    else:
        await create.finish("菜单类型参数错误,请选择 普通/高级 ")
    # 调用函数
    draw_txt_in_photo(menu_type, ttf_size)


def sum_menu(menu_type: str) -> tuple[int, list]:
    """
    确定菜单类型并返回宽度最大值和对应菜单

    :param menu_type: 菜单类型
    """
    # 菜单信息
    menu_info: list = load_file()[menu_type]
    # 菜单最长值
    max_name_int = len(menu_info[0])
    return max_name_int, menu_info


def draw_txt_in_photo(menu_type: str, ttf_size: int):
    """
    根据返回的参数生成文字并画图

    :param menu_type: 菜单类型
    :param ttf_size: 字号大小
    """
    # 读取菜单和最大值
    max_left_and_info: tuple[int, list] = sum_menu(menu_type)
    # 创建底片
    image = Image.new(mode='RGB',
                      size=(ttf_size * max_left_and_info[0], (ttf_size + 2) * len(max_left_and_info[1])),
                      color="white")
    # 创建画图
    image_draw = ImageDraw.Draw(image)
    # 加载字体
    fnt = ImageFont.truetype("ttf/三极泼墨体.ttf", ttf_size)
    # 定义需要写的字
    txt = "\n".join(max_left_and_info[1])
    # 写字
    image_draw.multiline_text((0, 0), txt, font=fnt, fill=(0, 0, 0))
    # 保存照片
    image.save("photo/output/" + menu_type + ".jpg")
