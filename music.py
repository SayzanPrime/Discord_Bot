import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get

import utils


class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if utils.is_author_in_channel(ctx):
            await ctx.send('Connect to a voice channel before calling me you idiot :)')
            return

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        await ctx.send(f'Joined {voice_channel}.')

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.send(f'Disconnected.')

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        ydl_options = {
            'format': 'bestaudio',
            'noplaylist': 'True'
        }
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url, download=False)
            ydl_url = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(ydl_url, **ffmpeg_options)
            vc.play(source)

    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()
        await ctx.send(f'Stoped.')

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Paused.')

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Resumed.')


def setup(client):
    client.add_cog(MusicBot(client))
