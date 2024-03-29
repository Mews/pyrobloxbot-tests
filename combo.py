import pyrobloxbot as bot
from time import sleep as wait
import keyboard as kb

combo = [("x", 0.3), ("z", 0), ("3", 0), ("z", 0.2), ("1", 0.2), ("c",0.2), ("3",0.3), ("x",0)]

def hit_combo():
    for move, delay in combo:
        bot.press_key(move)
        wait(delay)

kb.add_hotkey("m", hit_combo)

while True:
    pass