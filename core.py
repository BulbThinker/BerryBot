import os
import pathlib
import asyncio
import discord
from discord.ext import commands
from configuration import Configuration


Loop = asyncio.get_event_loop()
Config = Configuration(os.path.join(pathlib.Path(__file__).parent.absolute(), "config.json"))
BerryBot = commands.Bot(command_prefix=Config.command_prefix)

def run():
    BerryBot.run(Config.token)
