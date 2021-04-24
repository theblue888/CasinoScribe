import discord, pymongo
from discord.ext import commands

import settings

class wallet(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    db = settings.db
    bank = settings.bank      

def setup(bot):
    bot.add_cog(wallet(bot))