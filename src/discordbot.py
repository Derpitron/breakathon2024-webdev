#todo fill in and implement
import interactions

from dotenv import load_dotenv

#import audioanalysis
import random

BOT_ID     = load_dotenv("BOT_ID")
BOT_TOKEN  = load_dotenv("BOT_TOKEN")
SERVER_ID  = load_dotenv("SERVER_ID")
CHANNEL_ID = load_dotenv("CHANNEL_ID")

import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command()
async def join(context):
    """Command to make the bot join a voice channel."""
    channel = discord.utils.get(context.guild.voice_channels, id=CHANNEL_ID)
    if channel:
        await channel.connect()

@client.command()
async def record(context):
    """Record audio from the voice channel."""
    channel = discord.utils.get(context.guild.voice_channels, id=CHANNEL_ID)
    if channel:
        voice_client = await channel.connect()
        # Start recording audio (we'll use FFmpeg to process audio)
        # You need to set up ffmpeg to capture the stream
        audio_source = await voice_client.listen()
        with open('tmp/audio_output.pcm', 'wb') as f:
            while True:
                data = await audio_source.read(1024)
                if not data:
                    break
                f.write(data)
        await voice_client.disconnect()

@client.command()
async def leave(context):
    """Make the bot leave the voice channel."""
    if context.voice_client:
        await context.voice_client.disconnect()

client.run(BOT_TOKEN)
