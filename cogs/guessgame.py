import discord, random
from discord.ext import commands
import settings

class guessgame(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    @commands.command(aliases=["guessgameimpossible","ggimpossible"])
    async def ggi(self, ctx, guess=None):
        if guess == None:
            await ctx.send(f":warning: You must specify a guess {ctx.author.mention}!")
            return
        
        try:
            int(guess)
        except:
            await ctx.send(f":warning: Your guess needs to be a valid integer {ctx.author.mention}!")
            return

        real = random.randint(1,100)
        if real == int(guess):
            await ctx.send(f":white_check_mark: You win! Your guess was **{guess}** and the number was **{guess}**.")
        else:
            await ctx.send(f":x: Womp womp. Your guess was **{guess}** but the number was **{guess}**. Better luck next time!")
        

def setup(bot):
    bot.add_cog(guessgame(bot))