"""
函数：
image_base64() -> image to base64 str
"""
import base64


def image_base64(image_path: str) -> str:
    """
    image to base64 str

    :param image_path: 图片路径
    :return: base64字符串
    """
    with open(image_path, "rb") as f:
        base64_str = base64.b64encode(f.read()).decode()
    return base64_str
