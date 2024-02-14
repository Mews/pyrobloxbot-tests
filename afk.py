from pyrobloxbot import *
from time import sleep as wait
import pyautogui as pg
from random import choice
from spawn_location import reset_until_spawn_location

#Point(x=1033, y=134)
#(39, 202, 28)
#Point(x=767, y=137)
#(39, 202, 28)
#Point(x=867, y=135)
#(39, 202, 28)
BOSS_BAR_PIXEL_CORDS = (1033, 134)
BOSS_BAR_PIXEL_RGB = (39,202,28)
ACTIONS_BEFORE_RESET = 12

def factory_raid_started():
    screen = pg.screenshot()

    boss_bar_pixel = screen.getpixel(BOSS_BAR_PIXEL_CORDS)

    if boss_bar_pixel == BOSS_BAR_PIXEL_RGB:
        #Move camera to confirm pixel color is from boss bar
        hold_keyboard_action("right", 2)

        screen = pg.screenshot()

        boss_bar_pixel = screen.getpixel(BOSS_BAR_PIXEL_CORDS)

        return boss_bar_pixel == BOSS_BAR_PIXEL_RGB

    else:
        return False


def afk_until_factory_raid():
    i = 0

    while not factory_raid_started():
        jump()
        walk(choice(("f", "b", "l", "r")), 1)
        wait(1)

        i+=1
        if i > ACTIONS_BEFORE_RESET:
            i = 0
            reset_until_spawn_location("1", "2", "3")
            wait(5)