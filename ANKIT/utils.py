# By < ANKIT KUMAR >
# // NoUB SPAMMERBOT MADE BY ©LEGEND-ANKIT™ //

import sys
import logging
import importlib
from telethon import TelegramClient, events
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"ANKIT/plugins/{plugin_name}.py")
    name = "ANKIT.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["ANKIT.plugins." + plugin_name] = load
    print("NoUB SPAMMER BOT has IMPoRTED " + plugin_name)
