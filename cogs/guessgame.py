import discord, random
from discord.ext import commands
import settings

class guessgame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["guessgame100"])
    async def gg100(self, ctx, guess=None):
        if guess == None:
            await ctx.send(f":warning: You must specify a guess {ctx.author.mention}!")
            return
        
        try:
            int(guess)
        except:
            await ctx.send(f":warning: Your guess needs to be a valid integer {ctx.author.mention}!")
            return
        
        if int(guess) > 100:
            await ctx.send(f":warning: Your guess cannot be greater than **100**!")
            return

        real = random.randint(1,100)
        if real == int(guess):
            await ctx.send(f":white_check_mark: {ctx.author.mention} You win! Your guess was **{guess}** and the number was **{guess}**.")
        else:
            await ctx.send(f":x: {ctx.author.mention} Womp womp. Your guess was **{guess}** but the number was **{real}**. Better luck next time!")
        
    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["gg","guessgame"])
    async def gg10(self, ctx, guess=None):
        if guess == None:
            await ctx.send(f":warning: You must specify a guess {ctx.author.mention}!")
            return
        
        try:
            int(guess)
        except:
            await ctx.send(f":warning: Your guess needs to be a valid integer {ctx.author.mention}!")
            return

        if int(guess) > 10:
            await ctx.send(f":warning: Your guess cannot be greater than **10**!")
            return

        real = random.randint(1,10)
        if real == int(guess):
            await ctx.send(f":white_check_mark: {ctx.author.mention} You win! Your guess was **{guess}** and the number was **{guess}**.")
        else:
            await ctx.send(f":x: {ctx.author.mention} Womp womp. Your guess was **{guess}** but the number was **{real}**. Better luck next time!")

    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["guessgamed", "guessgamedecimal"])
    async def ggd(self, ctx, guess=None):
        if guess == None:
            await ctx.send(f":warning: You must specify a guess {ctx.author.mention}!")
            return
        
        try:
            float(guess)
        except:
            await ctx.send(f":warning: Your guess needs to be a valid float or integer {ctx.author.mention}!")
            return

        if float(guess) > 51:
            await ctx.send(f":warning: Your guess cannot be greater than **51**!")
            return

        real = round(random.uniform(1.0, 51.0),2)
        if real == float(guess):
            await ctx.send(f":white_check_mark: {ctx.author.mention} You win! Your guess was **{guess}** and the number was **{guess}**.")
        else:
            await ctx.send(f":x: {ctx.author.mention} Womp womp. Your guess was **{guess}** but the number was **{real}**. Better luck next time!")

    @commands.cooldown(8,10,commands.BucketType.user)
    @commands.command(aliases=["guessgame1000"])
    async def ggi(self, ctx, guess=None):
        if guess == None:
            await ctx.send(f":warning: You must specify a guess {ctx.author.mention}!")
            return
        
        try:
            int(guess)
        except:
            await ctx.send(f":warning: Your guess needs to be a valid integer {ctx.author.mention}!")
            return
        
        if int(guess) > 1000:
            await ctx.send(f":warning: Your guess cannot be greater than **1000**!")
            return

        real = random.randint(1,1000)
        if real == int(guess):
            await ctx.send(f":white_check_mark: {ctx.author.mention} You win! Your guess was **{guess}** and the number was **{guess}**.")
        else:
            await ctx.send(f":x: {ctx.author.mention} Womp womp. Your guess was **{guess}** but the number was **{real}**. Better luck next time!")



def setup(bot):
    bot.add_cog(guessgame(bot))