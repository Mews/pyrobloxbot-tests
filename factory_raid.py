import pyrobloxbot as bot
from spawn_location import reset_until_spawn_location
import pyautogui as pg
from time import sleep as wait
from time import perf_counter

CLICK_ATTACK_COORDS = (1280, 633) #Where mouse should move to use m1 attack
                                  #And also to open fruit dialog

@bot.require_focus
def move_to_factory():
    reset_until_spawn_location("3")
    bot.walk_forward(3)
    bot.walk_right(3.75)
    bot.walk("f", "r", duration=15)
    wait(5) #Make sure door is open

@bot.require_focus
def kill_core():
    start_time = perf_counter()

    bot.walk("f", "r", duration=4.2)
    bot.hold_keyboard_action("l", "b", duration=0)
    bot.equip_slot(2)
    bot.keyboard_action("v")
    wait(0.2)
    bot.jump()
    wait(0.5)
    bot.walk("f", "r", duration=0.3)

    while perf_counter() - start_time < 5*60:
        pg.click(CLICK_ATTACK_COORDS[0], CLICK_ATTACK_COORDS[1])
        bot.keyboard_action("z")
        wait(0.5)

@bot.require_focus
def store_fruits():
    reset_until_spawn_location("2")

    bot.walk_forward(0.7)
    bot.jump(2)
    bot.walk_forward(0.3)
    bot.equip_slot(5)
    pg.click(CLICK_ATTACK_COORDS[0], CLICK_ATTACK_COORDS[1])
    bot.UI_NAV_KEY = "`"
    bot.toggle_ui_navigation()
    for i in range(2):
        wait(1)
        bot.ui_navigate_down()
        wait(1)
    bot.ui_click()