from .. import loader
from asyncio import sleep

@loader.tds
class HackProMod(loader.Module):
    strings = {"name": "HackPro"}

    async def hackprocmd(self, message):
        await message.edit("Начинаю сбор информации аккаунта...")
        await sleep(2)
        await message.edit("Найдены нужные uuid4 ключи")
        await sleep(2.3)
        await message.edit("Отправляю запрос к CoreTelegram")
        await sleep(1.9)
        await message.edit("🔓Запрос прошел успешно!\nДанные аккаунта отправлены в избранное\nСписок данных:\n1. API_ID\n2. API_HASH\n3. Прочая информация аккаунта")