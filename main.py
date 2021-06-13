import discord
import os , json , random
from discord.ext import commands
from functions.events import Events
from functions.function import func

bot = commands.Bot(command_prefix='m!', case_insensitive=True)
bot.remove_command('help')

event = Events(bot)
bot.event(event.on_command_error)
bot.event(event.on_guild_leave)
events = func()

@bot.event
async def on_ready():
    print("We are ready to Go!")

async def on_message(message):
    if events.is_not_restricted_channel(message):
        if bot.user.mentioned_in(message):
            await message.channel.send("Hello I am Minecord the ultimate Minecraft Discord Bot, my prefix is ```m!```.")
        elif "start" in message.content[1:] or "help" in message.content[1:]:
            await bot.process_commands(message)
        elif events.has_profile(message):
            await bot.process_commands(message)
        else:
            await message.channel.send(f"{message.author.mention} you haven't created a profile, create a profile by the ```start``` command.")

if __name__ == '__main__':
    bot.run('Token')

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    print("Loaded All Cogs")

