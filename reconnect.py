import autoit
import pyrobloxbot as bot
import pyautogui as pg
from time import sleep as wait
import winwifi

def connect_wifi():
    while True:
        try:
            winwifi.WinWiFi.connect("NOWO_2G_D2A2")
        except RuntimeError:
            try:
                winwifi.WinWiFi.connect("NOWO_5G_D2A2")
            except RuntimeError:
                pass
            else:
                return None
        else:
            return None

def reconnect(team="marine"):
    connect_wifi()

    wait(3)

    while True:
        try:
            x, y = pg.locateCenterOnScreen("reconnect.png", confidence=0.9)
        except pg.ImageNotFoundException:
            pass
        else:
            autoit.mouse_click(x=x, y=y)
            break

    wait(1)
    
    while True:
        if bot.image_is_visible("fastmode.png", confidence=0.9):
            bot.ui_navigate_left()
            if not team == "marine":
                bot.ui_navigate_left()
            bot.ui_click()
            bot.toggle_ui_navigation()

            return None

        elif lost_connection():
            reconnect(team=team)
            return None

        wait(0.1)
    
def lost_connection():
    return bot.image_is_visible("reconnect.png", confidence=0.9)