#!/usr/bin/env python3
import core
import commands
import asyncio
import tasks


print(f"! {core.Config.name} v{tuple(core.Config.version)} !")
core.run()
print(f"\n! {core.Config.name} Done !")