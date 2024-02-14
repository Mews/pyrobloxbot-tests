import pyautogui as pg
import pyrobloxbot as bot
from PIL import Image, ImageChops
import os

SCREENSHOT_REGION = (425, 80, 1175, 360)
SCREENS_PATH = "spawn_location_screens"

def GETSCREENSHOTS():
    while True:
        bot.reset_player()
        input("Take screenshot...")
        screen = pg.screenshot(region=SCREENSHOT_REGION)
        screen.save("spawn_location_screens/"+input("Path:")+".jpg")

def identify():
    screen = pg.screenshot(region=SCREENSHOT_REGION)

    for spawn_location_file in os.listdir(SCREENS_PATH):
        spawn_location_screen = Image.open(SCREENS_PATH+"/"+spawn_location_file)

        spawn_location_screen.show()

identify()