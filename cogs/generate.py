import discord
from discord.ext import commands
import requests
import config

class generate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #key duration by api documentation is defined in days!!!!!
    async def generate(self, ctx, days):
        try:
            r = requests.get(f"https://keyauth.win/api/seller/?sellerkey={config.sellerkey}&type=add&format=JSON&expiry={days}&mask=******-******-******-******-******-******&level=1&amount=1&owner={ctx.message.author}&character=1&note=note")
            data = r.json()
            key = data['key']
            error = data['message']
            embed = discord.Embed(title="Key Generate Succesfuly", description=f"```{key}```", color=0x2ecc71)
            embed.add_field(name="Duration: ",value=f'`{days}` days', inline=False)
            embed.set_footer(text=f'{ctx.guild.name} © 2024')
            await ctx.send(embed=embed)
        except Exception:
            embederror = discord.Embed(title="Error to generate as key", description=f"```{error}```", color=0xe74c3c)
            embed.set_footer(text=f'{ctx.guild.name} © 2024')
            await ctx.send(embed=embederror)

def setup(bot):     
    bot.add_cog(generate(bot))    

