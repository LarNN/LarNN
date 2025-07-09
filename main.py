import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} başarıyla giriş yaptı!")

@bot.command()
async def selam(ctx):
    await ctx.send("Selam Kraliçem! 👋")

@bot.command()
async def atla(ctx):
    sonuc = random.uniform(0, 100)  # 0 ile 100 arasında float sayı üretir
    sonuc_str = f"{sonuc:.2f}%"    # Virgülden sonra 2 basamaklı formatla
    await ctx.send(f"{sonuc_str} atladınız 🪂")

bot.run(os.getenv("TOKEN"))

