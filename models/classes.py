import discord
from discord.ext import commands


class View(discord.ui.View):
    @discord.ui.button(label='De Novo',style=discord.ButtonStyle.success)
    async def novamente(self, ctx: discord.Integration,btn):
        await ctx.response.send_message(ctx.message.content)