import discord,json
from discord.ext import commands
import sys, traceback

# Import the JSON file variables
import settings

initial_extensions = [
    'cogs.slots',
    'cogs.rolls',
    'cogs.listeners',
    'cogs.help'
]

bot = commands.Bot(command_prefix=settings.configdata["prefix"])
bot.remove_command("help")

# Load the Cog files into memory
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
        print("[Extension] " + str(extension) + " loaded")

@bot.command()
@commands.cooldown(1,30,commands.BucketType.guild)
async def ping(ctx):
    await ctx.send('Pong! {0} seconds.'.format(round(bot.latency, 5)))

# Process commands.
@bot.event
async def on_message(message):
    await bot.process_commands(message)

bot.run(settings.configdata["token"])