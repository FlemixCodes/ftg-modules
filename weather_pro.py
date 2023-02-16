from .. import loader, utils
import requests

@loader.tds
class WeatherProMod(loader.Module):
    strings = {"name": "WeatherPro"}

    async def pwprocmd(self, message):
        city = utils.get_args_raw(message)
        if city != "":
            weather = requests.get(f"https://wttr.in/{city}.png?lang=ru").content
            await message.edit(f"˅Погода в {city}˅")
            await message.client.send_file(message.to_id, weather)
        else:
            await message.edit("Укажите город")
        
    async def awprocmd(self, message):
            city = utils.get_args_raw(message)
            if city != "":
                weather = requests.get(f"https://wttr.in/{city}?0?T?&lang=ru")
                await message.edit(weather.text)
            else:
                await message.edit("Укажите город")

    async def mwprocmd(self, message):
        city = utils.get_args_raw(message)
        if city != "":
            weather = requests.get(f"https://v3.wttr.in/{city}.png").content
            await message.edit(f"˅Карта погоды в {city}˅")
            await message.client.send_file(message.to_id, weather)
        else:
            await message.edit("Укажите город")