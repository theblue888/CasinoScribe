import discord
import datetime as dt
from discord.ext import commands
import settings

class listeners(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    # When the bot logs in, print bot details to console
    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        prefix = settings.configdata["prefix"]
        print('[BOOT] Logged in at ' + str(dt.datetime.now()))
        await self.bot.change_presence(activity=discord.Game(name=f"{prefix}?help"))
        print("[INFO] Username:",self.bot.user.name)
        print("[INFO] User ID:",self.bot.user.id)

    # When a message is det
    @commands.Cog.listener('on_command_error')
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            # Avoid flooding the console when a command is spammed
            return

def setup(bot):
    bot.add_cog(listeners(bot))