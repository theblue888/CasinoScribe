import random, json
from discord.ext import commands


import settings

class rolls(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["cr"])
    async def catroll(self, ctx):
        allcats = []

        for x in range(10):
            allcats.append(random.choice(settings.emojidata["catroll"]))

        await ctx.send(''.join(allcats))

def setup(bot):
    bot.add_cog(rolls(bot))