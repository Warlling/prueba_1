import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hola'):
        await message.channel.send("HOLAA, soy 1tis.GG para servirte.")

    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith('$que eres'):
            await message.channel.send("me creo un pana aqui que esta inventando con los comandos... saquenme de aqui")

    else:
        await message.channel.send("no te entendi >:[")

 

 

bot.run("TOKEN")
