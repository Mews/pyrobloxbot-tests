from pyrobloxbot import *
from time import sleep as wait
import pyautogui as pg
from random import choice

BOSS_BAR_PIXEL_CORDS = (922, 100)
BOSS_BAR_PIXEL_RGB = (0,0,0)
ACTIONS_BEFORE_RESET = 10

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


def startAfk():
    i = 0

    while not factory_raid_started():
        jump()
        walk(choice(("f", "b", "l", "r")), 1)
        wait(1)

        i+=1
        if i > ACTIONS_BEFORE_RESET:
            i = 0
            reset_player()
            wait(5)

startAfk()