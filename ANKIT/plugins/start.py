# By < ANKIT KUMAR >
# // NOUB SPAMMERBOT MADE BY ©LEGEND-ANKIT™ //

from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://github.com/LEGEND-ANKIT")],
                        [Button.inline("Cнєϲκ мє",data="noub")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="noub"))
async def ex(event):
    await event.edit("υѕє τнιѕ ρℓєαѕє /help",
                    buttons=[
                        [Button.url("οωиєя", url="https://github.com/LEGEND-ANKIT")]
                    ])



