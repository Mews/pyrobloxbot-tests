import pyautogui as pg
import pyrobloxbot as bot
import keyboard as key
from PIL import Image, ImageChops, ImageStat
import os
import math
from time import sleep as wait

SCREENSHOT_REGION = (425, 80, 1175, 360)
SCREENS_PATH = "spawn_location_screens"

def GETSCREENSHOTS():
    while True:
        bot.reset_player()
        input("Take screenshot...")
        screen = pg.screenshot(region=SCREENSHOT_REGION)
        screen.save("spawn_location_screens/"+input("Path:")+".jpg")

def get_difference_value(difference_image):
   #Returns average luminance of difference_image
   #Lower luminance means less differences
   im = difference_image.convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

@bot.require_focus
def identify():
    wait(0.2) #Give time for window to maximize

    screen = pg.screenshot(region=SCREENSHOT_REGION)

    difference_values = []

    for spawn_location_file in os.listdir(SCREENS_PATH):
        path = SCREENS_PATH+"/"+spawn_location_file
        spawn_location = spawn_location_file.replace(".jpg", "")
        spawn_location_screen = Image.open(path)

        #Generate difference image from screenshot and stored spawn location images
        difference_image = ImageChops.difference(screen, spawn_location_screen)

        difference_values.append( (spawn_location, get_difference_value(difference_image)) )
    
    #Return tuple with smallest difference value
    return min(difference_values, key=lambda tpl: tpl[1])

"""
#Test if it works
while True:
    while not key.is_pressed("y"):
        wait(0.1)
    bot.reset_player()
    wait(5)
    print(identify())
"""