import autoit
import pyrobloxbot as bot
import pyautogui as pg
from time import sleep as wait

def reconnect(team="marine"):
    while lost_connection():
        x, y = pg.locateCenterOnScreen("reconnect.png", confidence=0.9)
        autoit.mouse_click(x=x, y=y)
    
    while not bot.image_is_visible("fastmode.png", confidence=0.9):
        wait(0.1)
    
    bot.ui_navigate_left()
    if not team == "marine":
        bot.ui_navigate_left()
    bot.ui_click()
    bot.toggle_ui_navigation()

def lost_connection():
    return bot.image_is_visible("reconnect.png", confidence=0.9)