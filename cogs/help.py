import discord
import datetime as dt
from discord.ext import commands
import settings

class help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Re-define the bot object into the class.

    @commands.cooldown(1,10,commands.BucketType.guild)
    @commands.command()
    async def help(self, ctx):
        title = settings.configdata["help"]["title"]
        desc = settings.configdata["help"]["desc"]
        prefix = settings.configdata["prefix"]
        embed=discord.Embed(title=f"{title}", description=f"{desc}", color=0x32e6ff)
        embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_thumbnail(url="https://user-images.githubusercontent.com/7556992/40873750-8065e8e6-6690-11e8-9417-69fd6e759c9b.png")
        embed.add_field(name="Slots", value=f"`{prefix}fs` - Fruit slots\n`{prefix}pps` - Pepe slots\n`{prefix}pog` - Pog slots\n`{prefix}vpn` - VPN slots\n`{prefix}cat` - Cat slots", inline=False)
        embed.add_field(name="Rolls", value=f"`{prefix}cr` - Cat roll", inline=False)
        embed.add_field(name="Guess Games", value=f"`{prefix}ggw <guess>` - Win your every guess game.\n`{prefix}gg10 <guess>` - 1/10\n`{prefix}ggd <guess>` - 1-51 with decimals\n`{prefix}ggd+ <guess>` - 1-101 with decimals\n`{prefix}ggi <guess>` - 1/1000\n`{prefix}ggc <limit> <guess>` - A custom guess game with a limit of your choice.", inline=False)
        embed.add_field(name="Contribute", value="Are you a developer? Contribute code to the project at the [git repo](https://github.com/httpjamesm/CasinoScribe).", inline=False)
        embed.set_footer(text="Made by http.james#6969")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))