from time import sleep as wait
import pyrobloxbot as bot
import pyautogui as pg


bot.UI_NAV_KEY = "`"

def switch_server():
    bot.ui_click()
    bot.ui_navigate_down()
    bot.ui_navigate_left()
    bot.ui_navigate_down()

    switched_server = False

    while not switched_server:
        try:
            bot.ui_click()
            wait(1)
            ok_button_coords = pg.locateCenterOnScreen("ok_button.png")
            print(ok_button_coords)
            pg.click(ok_button_coords)
        except pg.ImageNotFoundException:
            print("Couldn't find image")
            switched_server = True


switch_server()