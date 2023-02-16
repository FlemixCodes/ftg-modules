from .. import loader
from datetime import datetime

@loader.tds
class PingProMod(loader.Module):
    strings = {"name": "PingPro"}

    async def pingprocmd(self, message):
        start = datetime.now()
        await message.edit(f"Измеряю...")
        end = datetime.now()
        pingtime = (end-start).microseconds / 1000
        await message.edit(f"📲Работаю\n⌚️Время ответа: **{pingtime}** мс.", parse_mode="markdown")