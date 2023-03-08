import discord,os

def replay(guild,client):
    try:
        musica = discord.FFmpegPCMAudio(os.environ.get('MUSICA1'))
        voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
        voice_client.play(musica, after=lambda e: replay(guild))
    except AttributeError:
        musica.cleanup()
