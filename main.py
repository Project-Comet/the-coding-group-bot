import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time
bot = Bot(command_prefix="?")
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with fire"))
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply with the bot latency."""
    await bot.delete_message(ctx.message)
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')
bot.run(os.getenv("TOKEN"))
