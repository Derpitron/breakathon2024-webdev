# todo fill in and implement
import interactions
import os
import subprocess

from dotenv import load_dotenv

load_dotenv()

# import audioanalysis
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
SERVER_ID = os.getenv("SERVER_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

client = commands.Bot(command_prefix="!", intents=intents)

songs = {"angry": ["1.mp3", "2.mp3"], "happy": ["3.mp3", "4.mp3"]}


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def join(context):
    """Command to make the bot join a voice channel."""
    channel = discord.utils.get(context.guild.voice_channels, id=CHANNEL_ID)
    if channel:
        await channel.connect()


def pcm2flac(pcm_file):
    # f is a binary file in pcm format
    flac_f = "tmp/flac_output.flac"
    command = [
        "ffmpeg",
        "-f",
        "s16le",
        "-ar",
        "44100",
        "-ac",
        "2",
        "-i",
        pcm_file,
        flac_f,
    ]
    subprocess.run(command, check=True)


@client.command()
async def record(context):
    """Record audio from the voice channel."""
    channel = discord.utils.get(context.guild.voice_channels, id=CHANNEL_ID)
    if channel:
        voice_client = await channel.connect()
        # Start recording audio (we'll use FFmpeg to process audio)
        # You need to set up ffmpeg to capture the stream
        audio_source = await voice_client.listen()
        pcm_f = "tmp/audio_output.pcm"
        flac_f = "tmp/flac_output.flac"
        with open(pcm_f, "wb") as f:
            while True:
                data = await audio_source.read(1024)
                if not data:
                    break
                f.write(data)
                pcm2flac(f)
        await voice_client.disconnect()

        os.remove(pcm_f)
        os.remove(flac_f)


@client.command()
async def leave(context):
    """Make the bot leave the voice channel."""
    if context.voice_client:
        await context.voice_client.disconnect()


client.run(BOT_TOKEN)
