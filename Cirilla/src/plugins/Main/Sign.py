from nonebot import on_command
from nonebot.rule import to_me

sign = on_command("签到", priority=5, block=True)


@sign.handle()
async def sign_handle():
    await sign.send("签到成功")
