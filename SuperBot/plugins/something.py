''' Whatever Plugin by Noobs of Telegram i.e. @pureindialover '''

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"lmoon"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("ππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππππππππ\nππ€π»πππππ€π»π\nππππππππ\nππππππππ\nππππππππ")

@borg.on(admin_cmd(pattern=r"city"))
async def test(event):
    if event.fwd_from:
        return 
    await event.edit("""ββπ      β           β
       β  β         β    π    β    β        β          β     β   β

π¬π¨π«π’π€π₯π¦πͺπ«
              π²/     lπ\π³π­
           π³/  π l  π \π΄ π¬                       π¬  π΄/            l  π    \π²
      π²/   π     l               \
   π³/πΆ           |   π         \ π΄π΄π΄
π΄/                    |                     \π²""")


@borg.on(admin_cmd(pattern=r"hi"))
async def hi(event):
    if event.fwd_from:
        return
    await event.edit("πΊβ¨β¨πΊβ¨πΊπΊπΊ\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊπΊπΊπΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨β¨πΊβ¨\nπΊβ¨β¨πΊβ¨πΊπΊπΊ\nββββββββ")

@borg.on(admin_cmd(pattern=r"cheer"))
async def cheer(event):
    if event.fwd_from:
        return
    await event.edit("ππππππ\nβ Cheer Up  π΅\nπ β¨ )) β¨  π\nπβ (( * β£β π\nπβ*π β£β π \nπββββ  ππ For YOU  π°\nππππππ")

@borg.on(admin_cmd(pattern=r"getwell"))
async def getwell(event):
    if event.fwd_from:
        return
    await event.edit("πΉπΉπΉπΉπΉπΉπΉπΉ \nπΉπ·π’ππ·π’π¨πΉ\nπΉπππ΅ππππΉ\nπΉ GetBetter Soon! πΉ\nπΉπΉπΉπΉπΉπΉπΉπΉ")

@borg.on(admin_cmd(pattern=r"sprinkle"))
async def sprinkle(event):
    if event.fwd_from:
        return
    await event.edit("β¨.β’*Β¨*.ΒΈ.β’*Β¨*.ΒΈΒΈ.β’*Β¨*β’ ΖΈΣΖ·\nπΈπΊπΈπΊπΈπΊπΈπΊ\n Sprinkled with loveβ€\nπ·π»π·π»π·π»π·π»\n Β¨*.ΒΈ.β’*Β¨*. ΒΈ.β’*Β¨*.ΒΈΒΈ.β’*Β¨`*β’.β¨\nπΉππΉππΉππΉπ")
