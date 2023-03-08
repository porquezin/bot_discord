import discord, os, utils
import models.classes as classes
from discord.ext import commands
from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(join(dirname(__file__), '.env'))

client = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all()
)


@client.event
async def on_ready():
    print('open server')
    try:
        await client.tree.sync()
    except Exception as e:
        print(e)


# slash_commands


@client.tree.command(name='escreva', description='Escreve algo no chat com o bot!')
async def escreva(ctx: discord.Interaction, frase:str):
    view = classes.View()
    await ctx.response.send_message(f'{frase}',view=view)


@client.tree.command(name='ping', description='Checa a latencia do bot')
async def ping(ctx: discord.Interaction):
    await ctx.response.send_message(f"{client.latency}ms")


@client.tree.command(name='clear', description='Limpa o chat atual')
async def clear(ctx: discord.Interaction, quantidade: int):
    await ctx.response.send_message(f'Mesagens apagadoas: {quantidade}', ephemeral=True)
    await ctx.channel.purge(limit=quantidade)


@client.tree.command(name='close_bot', description='Desliga o BOT')
async def close(ctx: discord.Interaction):
    await ctx.response.send_message(f'flw!')
    await client.close()
    exit()


@client.tree.command(name='play_curso_na_australia', description='se tiver algum bug me fala!')
async def play_australia(ctx: discord.Interaction):
    try:
        canal = ctx.user.voice.channel
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        if voice_client == None:
            await canal.connect()
            voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        else:
            await ctx.response.send_message(f'Ja ta tocando!')
            return
            
        if not voice_client.is_playing():
            musica = discord.FFmpegPCMAudio(os.environ.get('MUSICA1'))
            await ctx.response.send_message(f'curso na australia em: {canal}')
            voice_client.play(musica, after=lambda e: utils.replay(guild,client))
        else:
            await ctx.response.send_message(f'Ja ta tocando em: {canal}')
                
    except AttributeError:
        await ctx.response.send_message('Entra em um canal seu fudido!')


@client.tree.command(name='stop',description='Desconecta o bot da call')
async def stop(ctx: discord.Interaction):
    try:
        guild = ctx.guild
        server = ctx.guild.voice_client
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        if voice_client.is_playing():
            voice_client.stop()
        await server.disconnect()
        await ctx.response.send_message("Desconectado!")
    except AttributeError:
        await ctx.response.send_message('Não to em call, burro!')


client.run(os.environ.get("DISCORD_TOKEN"))