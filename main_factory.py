from pyrobloxbot import *
from time import sleep as wait
from afk import afk_until_factory_raid
from factory_raid import *
from datetime import datetime
import pygetwindow

while True:
    try:
        print("Afk at", datetime.now().time())
        afk_until_factory_raid()
        print("Moving to factory at", datetime.now().time())
        move_to_factory()
        print("Killing core at", datetime.now().time())
        kill_core()
        print("Storing fruits at", datetime.now().time())
        store_fruits()
    except pygetwindow.PyGetWindowException:
        pass