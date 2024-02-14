import pyautogui as pg
import keyboard as key
from time import sleep as wait

while True:
    if key.is_pressed("m"):
        print(pg.position())
        print(pg.screenshot().getpixel(pg.position()))
        wait(0.5)