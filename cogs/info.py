import discord
from discord.ext import commands
import requests
from datetime import datetime
import config

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, key):
        try:
            r = requests.get(f"https://keyauth.win/api/seller/?sellerkey={config.sellerkey}&type=info&key={key}")
            data = r.json()
            username = data['usedby']
            status = data['status']
            hwid = data['hwid']
            createdby = data['createdby']

            if username == "":
                username = "Not Username"

            if hwid == "":
                hwid = "Not Hwid"

            embed = discord.Embed(title="Informations", color=0x2ecc71)
            embed.add_field(name="Username: ",value=f'`{username}`', inline=False)
            embed.add_field(name="Status: ",value=f'`{status}`', inline=False)
            embed.add_field(name="Hwid: ",value=f'`{hwid}`', inline=False)
            embed.add_field(name="Created by", value=f'`{createdby}`', inline=False)
            embed.set_footer(text=f'{ctx.guild.name} © 2024')
            await ctx.send(embed=embed)
        except Exception:
            embederror = discord.Embed(title="Ops! Failed", description=f"```Key Not Found```", color=0xe74c3c)
            embederror.set_footer(text=f'{ctx.guild.name} © 2024')
            await ctx.send(embed=embederror)


def setup(bot):     
    bot.add_cog(info(bot))    

