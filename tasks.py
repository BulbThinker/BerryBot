import core
import discord
import asyncio
import gpiozero
import functools
import time


alert_channel = None
sensor = gpiozero.MotionSensor(core.Config.sensor_gpio)
last_alert_time = 0


def sensor_when_motion_callback():
    async def send_alert():
        global alert_channel
        global last_alert_time
        if alert_channel is None:
            if not core.BerryBot.is_ready():
                await core.BerryBot.wait_until_ready()
            alert_channel = core.BerryBot.get_channel(core.Config.alert_channel)
        current_time = time.time()
        if (current_time - last_alert_time) > core.Config.sensor_time_interval:
            last_alert_time = current_time
            await alert_channel.send("Alerta! Intruso detectado!")
    def _call_on_future():
        asyncio.ensure_future(send_alert())
    core.Loop.call_soon_threadsafe(_call_on_future)


# Motion Sensor Callback
sensor.when_motion = sensor_when_motion_callback
