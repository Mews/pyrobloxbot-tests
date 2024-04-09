import pyautogui as pg
import keyboard as kb

def show_screen():
    s = pg.screenshot()
    s.show()

kb.add_hotkey("m", show_screen)

while not kb.is_pressed("p"):
    pass