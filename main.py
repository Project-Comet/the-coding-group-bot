import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import itertools
bot = Bot(command_prefix="?")
status_list = [("with fire", 1), ("the endless game of debugging", 1), ("cat videos on YouTube", 3), ("tricks on your mind", 1), ("my code being written", 3)]
async def change_status():
    await bot.wait_until_ready()
    msgs = itertools.cycle(status_list)
    while not bot.is_closed:
        next_status = next(msgs)
        await bot.change_presence(game=discord.Game(name=next_status[0], type=next_status[1]))
        await asyncio.sleep(10)
@bot.event
async def on_ready():
    pass
@bot.command(pass_context=True)
async def ping(ctx):
    """Sends a reply with the bot latency."""
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
    print(f'Ping {int(ping)}ms')
@bot.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    """Punches the specified user."""
    await bot.say("Now punching " + user.mention)
    await bot.send_message(user, "You've been punched!")
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount=100):
    """Clear the specified number of messages, default 100 messages."""
    channel = ctx.message.channel
    messages = []
    amount = int(amount) + 1
    async for message in bot.logs_from(channel, limit=amount):
        messages.append(message)
    await bot.delete_messages(messages)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await bot.send_message(ctx.message.channel, "You do not have permission to use that command.".format(ctx.message.author.mention))
bot.loop.create_task(change_status())
bot.run(os.getenv("TOKEN"))
