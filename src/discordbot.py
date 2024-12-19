#todo fill in and implement
import discord
from discord.ext import commands

from dotenv import load_dotenv

import audioanalysis
import random

BOT_ID     = load_dotenv("BOT_ID")
BOT_TOKEN  = load_dotenv("BOT_TOKEN")
SERVER_ID  = load_dotenv("SERVER_ID")
CHANNEL_ID = load_dotenv("CHANNEL_ID")

intents = discord.intents.default()
intents.voice_states = True
bot = commands.Bot(command_prefix="!", intents=intents)

vclients_perguild = {}

@bot.event
async def on_ready():
    print("Logged in as", bot.user)

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    vcstate = channel.voice_states
    if len(vcstate) > 0:
        vclient = await channel.connect()
        vclients_perguild[ctx.guild.id] = vclient
        print("connected to voice channel")

@bot.command()
async def listen(ctx):
    if ctx.guild.id in voice_clients:
        vclient = vclients_perguild[ctx.guild.id]
        vclient.listen(lambda audio: process_audio(audio))
        

        sentiment = audio-analysis.getStream(audioStream)

        audioList = {
            "angry": ['list', 'of', 'songfilenames'],
            "happy": ['list', 'of', 'songfilenames'],
        }

        bot.playAudio(random.randchoice(audioList[sentiment]))