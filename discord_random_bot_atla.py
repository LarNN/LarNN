import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

secilenekler = []  # Kullanıcıların eklediği verileri saklayan liste

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

# Komut: !ekle elma armut muz
@bot.command()
async def ekle(ctx, *args):
    if not args:
        await ctx.send("Lütfen eklemek istediğiniz metinleri yazın. Örnek: !ekle elma armut muz")
        return
    secilenekler.extend(args)
    await ctx.send(f"Eklendi: {', '.join(args)}")

# Komut: !atla => rastgele metin ya da % oranı seçer
@bot.command()
async def atla(ctx):
    if not secilenekler:
        # Eğer liste boşsa sadece oran göster
        yuzdelik = f"%{round(random.uniform(0, 100), 2)}"
        await ctx.send(f"{yuzdelik}")
        return

    if random.choice([True, False]):
        secim = random.choice(secilenekler)
        await ctx.send(f"{secim}")
    else:
        yuzdelik = f"%{round(random.uniform(0, 100), 2)}"
        await ctx.send(f"{yuzdelik}")

# Komut: !liste => mevcut listeyi gösterir
@bot.command()
async def liste(ctx):
    if not secilenekler:
        await ctx.send("Liste boş. Önce !ekle komutuyla veriler girin.")
        return
    await ctx.send("Mevcut seçenekler:\n" + "\n".join(f"- {item}" for item in secilenekler))

# Komut: !temizle => listeyi sıfırlar
@bot.command()
async def temizle(ctx):
    secilenekler.clear()
    await ctx.send("Liste temizlendi.")

# Botu başlat
bot.run('TOKEN')
