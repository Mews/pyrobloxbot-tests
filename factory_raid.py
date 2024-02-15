from pyrobloxbot import *
from spawn_location import reset_until_spawn_location
import pyautogui as pg
from time import sleep as wait
from time import perf_counter
from statistics import mode
from pynput.keyboard import Key, Controller

CLICK_ATTACK_COORDS = (1280, 633) #Where mouse should move to use m1 attack

@require_focus
def move_to_factory():
    reset_until_spawn_location("3")
    walk_forward(3)
    walk_right(3.75)
    hold_keyboard_action("w", "d", duration=15)
    wait(5) #Make sure door is open

@require_focus
def kill_core():
    start_time = perf_counter()

    hold_keyboard_action("w", "d", duration=4.2)
    hold_keyboard_action("a", "s", duration=0)
    equip_slot(2)
    keyboard_action("v")
    wait(0.2)
    jump()
    wait(0.5)
    hold_keyboard_action("w", "d", duration=0.3)

    while perf_counter() - start_time < 5*60:
        pg.click(CLICK_ATTACK_COORDS[0], CLICK_ATTACK_COORDS[1])
        keyboard_action("z")
        wait(0.5)