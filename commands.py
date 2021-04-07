import os
import core
import pathlib
import discord
import gpiozero


buzzer = gpiozero.Buzzer(core.Config.alarm_gpio)


@core.BerryBot.command()
async def ping(ctx):
    """Reply with a pong"""
    await ctx.send("pong")


@core.BerryBot.command()
async def hello(ctx):
    """Nice to meet you!"""
    await ctx.send(f"Olá {ctx.message.author.mention}, eu sou o {ctx.me.name}!")


alarm_state = False
@core.BerryBot.command()
async def alarm(ctx, on_time:float=1, off_time:float=0.6, n:int=5):
    """Sets the alarm! Scare the Intruder!"""
    buzzer.beep(on_time, off_time, n)
    await ctx.send(f"Alarme acionado")


image_counter = 0
@core.BerryBot.command()
async def picture(ctx, frames:int = 5):
    """Let-me see their face! Let-me see now!"""
    global image_counter
    frames = int(frames) if frames > 0 else 1
    picture_name = os.path.join(
        os.path.join(os.path.join(pathlib.Path(__file__).parent.absolute(), core.Config.image_path)),
        f"frame_{image_counter}.jpg"
    )
    try:
        await ctx.send("Aguarde por favor ...")
        os.system(f"fswebcam -F {frames} {picture_name}")
        with open(picture_name, 'rb') as f:
            df = discord.File(f)
            await ctx.send(file=df)
        image_counter = (image_counter + 1) % core.Config.image_buffer_size
    except Exception as e:
        await ctx.send(f"Error! {e}")
