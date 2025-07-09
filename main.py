import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} başarıyla giriş yaptı!")

@bot.command()
async def selam(ctx):
    await ctx.send("Selam Musamert! 👋")

@bot.command()
async def atla(ctx):
    await ctx.send("Atla komutu çalıştı! ⏭️")

bot.run(os.getenv("TOKEN"))

