import pyautogui as pg
import keyboard as key

while True:
    if key.is_pressed("m"):
        print(pg.position())