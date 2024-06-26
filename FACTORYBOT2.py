import pyrobloxbot as bot
import sys

input("TEST UI NAVIGATION...")
bot.toggle_ui_navigation()
ans = input("Did ui navigation mode turn on? (y\\n): ").lower().rstrip().lstrip()
if ans == "n":
    sys.exit("Restart the computer")
elif ans == "y":
    bot.toggle_ui_navigation()

print("""
MAKE SURE THAT:
- YOU'RE MARINE
- YOUR SWORD DOESNT MOVE YOU (buddy sword, midnight blade, saber, etc)
- YOU HAVE BUDDHA EQUIPED
- YOU DIDNT OPEN THE MENU
- YOU TURNED YOUR SENSITIVITY DOWN
- YOU HAVE HUNTER CAPE EQUIPED
- YOUR HOME IS IN CAFE
- FRUIT IS SLOT 2
- SWORD IS SLOT 3
- FRUITS ARE SLOT 5
- YOU ARE IN 1st PERSON
- YOU HAVE SHIFT LOCK ENABLED
""")
input("Start...")

from time import sleep as wait
import time
import random
import datetime
import pyscreeze as screeze
import pyautogui as pg
import reconnect
import autoit

def tp_home():
    for i in range(6):
        bot.ui_navigate_left()
    
    for i in range(2):
        bot.ui_navigate_up()
    
    for i in range(2):
        bot.ui_navigate_right()
    
    bot.ui_click()
    bot.toggle_ui_navigation()

def raid_started():
    return bot.image_is_visible("core.png", 0.8)

def afk_move():
    bot.hold_key("space", random.choice(["a", "d"]), duration=0.25+random.random())

def log_screen():
    filename = str(datetime.datetime.now()).split(".")[0].replace(":", "-") + ".png"
    screeze.screenshot().save("factorylogs/"+filename)

@bot.require_focus
def mouse1():
    pg.click()

def drop_fruit():
    bot.equip_slot(5)
    mouse1()
    wait(2)
    bot.ui_navigate_down()
    bot.ui_navigate_down()
    bot.ui_click()
    bot.toggle_ui_navigation()
    mouse1()

def store_fruit():
    bot.equip_slot(5)
    mouse1()
    wait(2)
    bot.ui_navigate_down()
    bot.ui_navigate_down()
    bot.ui_navigate_down()
    bot.ui_click()
    bot.toggle_ui_navigation()

    bot.ui_navigate_down()
    bot.ui_navigate_down()
    bot.ui_click()
    bot.toggle_ui_navigation()

    bot.equip_slot(5)

    mouse1()

def walk_to_factory():
    bot.walk_right(4)

    bot.jump(3)
    wait(0.1)
    bot.walk_forward(1.75)

    bot.walk_right(1.5)
    bot.key_down("w")
    bot.key_down("d")
    for i in range(9):
        bot.press_key("q")
        wait(0.5)
    bot.key_up("w")
    bot.key_up("d")

def kill_core():
    bot.walk("f", "r", duration=2.4)
    bot.walk("b", "l", duration=0)
    bot.equip_slot(2)
    bot.jump(3, 0.1)
    bot.press_key("z")
    wait(2)
    bot.jump(5, 0.1)
    bot.walk("f", "r", duration=0.5)
    bot.equip_slot(3)
    while raid_started():
        mouse1()
        wait(0.2)
    for i in range(10):
        mouse1()
        wait(0.2)

def main_loop():
    print("Starting with reset")
    bot.reset_player()
    wait(10)
    bot.press_key("j")

    while True:
        print("Afking")
        #Move around until raid starts
        bot.walk_forward(0.29)
        while not raid_started():
            if reconnect.lost_connection():
                print("\033[91m"+"LOST CONNECTION AT", str(datetime.datetime.now())+"\033[0m")
                reconnect.reconnect()
                print("\033[92m"+"Reconnected at", str(datetime.datetime.now())+"\033[0m")
                wait(1)
                autoit.mouse_wheel("up", 100) #Zoom in to first person
                wait(0.5)
                bot.toggle_shift_lock()
                return None

            afk_move()
            wait(1)
        print("\033[36m"+"Found raid at", str(datetime.datetime.now())+"\033[0m")
        tp_home()
        wait(7)
        print("Moving to factory")
        walk_to_factory()
        print("Waiting for door to open")
        wait(5)
        print("Killing core")
        kill_core()
        bot.equip_slot(2)
        bot.press_key("z")
        bot.equip_slot(2)
        print("Logging screenshot")
        log_screen()
        tp_home()
        wait(7)
        print("Trying to store fruit")
        bot.equip_slot(1)
        bot.equip_slot(1)
        store_fruit()
        print("Trying to drop fruit")
        bot.walk_left(4.5)
        bot.key_down("w")
        bot.jump(3, 0.1)
        wait(0.2)
        bot.key_up("w")
        bot.walk("f", "l", duration=0.35)
        drop_fruit()
        print("Reseting player")
        wait(2)
        bot.reset_player()
        wait(10)

while True:
    main_loop()