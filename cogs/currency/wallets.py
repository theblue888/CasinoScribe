import discord, pymongo
from discord.ext import commands

import settings

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    self.db = settings.db
    self.bank = settings.bank

    @commands.command(aliases=["money","bal","balance","coins"])
    async def wallet(self, ctx):
        query = self.bank.find({
            "userid": ctx.author.id
        })

        balance = 0

        for x in query:
            balance = x["balance"]
        
        embed=discord.Embed(title=f"{ctx.author.username}#{ctx.author.discriminator}'s Wallet", description="Here's your in-game Casino balance that you can gamble with.\n\n**Disclaimer** In-game currency has no tangible value in fiat currency.")
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.add_field(name="Bank Details", value=f"**Balance**: {balance} Coins", inline=False)
        embed.set_footer(text="Made by http.james#6969")
        try:
            await ctx.author.send(embed=embed)
        except:
            await ctx.send(f":warning: I couldn't send you a DM, {ctx.author.mention}. Do you have them enabled?")
            return
        await ctx.send(f":white_check_mark: The banker has sent you a DM, {ctx.author.mention}.")
      

def setup(bot):
    bot.add_cog(help(bot))