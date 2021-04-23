import random, json
from discord.ext import commands


import settings

class slots(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.
    
    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["fs"])
    async def fruitslots(self, ctx):
        firstrow = []
        secondrow = []
        thirdrow = []

        for x in range(3):
            firstrow.append(random.choice(settings.emojidata["fruitslots"]))
        
        for x in range(3):
            secondrow.append(random.choice(settings.emojidata["fruitslots"]))

        for x in range(3):
            thirdrow.append(random.choice(settings.emojidata["fruitslots"]))
        
        allrows = []
        allrows.append(''.join(firstrow))
        allrows.append(''.join(secondrow))
        allrows.append(''.join(thirdrow))
        
        await ctx.send('\n'.join(allrows))

    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["ps"])
    async def pepeslots(self, ctx):
        firstrow = []
        secondrow = []
        thirdrow = []

        for x in range(3):
            firstrow.append(random.choice(settings.emojidata["pepeslots"]))
        
        for x in range(3):
            secondrow.append(random.choice(settings.emojidata["pepeslots"]))

        for x in range(3):
            thirdrow.append(random.choice(settings.emojidata["pepeslots"]))
        
        allrows = []
        allrows.append(''.join(firstrow))
        allrows.append(''.join(secondrow))
        allrows.append(''.join(thirdrow))
        
        await ctx.send('\n'.join(allrows))

def setup(bot):
    bot.add_cog(slots(bot))