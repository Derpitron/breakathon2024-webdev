# todo fill in and implement
import interactions
from interactions.api.voice.audio import AudioVolume
import os
import subprocess
from audioanalysis import get_highest_score_label

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

song = '..\\audio\\angry.mp3'


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def join(context):
    """Command to make the bot join a voice channel."""
    channel = discord.utils.get(context.guild.voice_channels, id=CHANNEL_ID)
    if channel:
        await channel.connect()

@interactions.command()
async def play_file(ctx: interactions.SlashContext):
    audio = AudioVolume("some_file.wav")
    await ctx.voice_state.play(audio)

#todo record flac audio from system mic


@client.command()
async def leave(context):
    """Make the bot leave the voice channel."""
    if context.voice_client:
        await context.voice_client.disconnect()


client.run(BOT_TOKEN)
