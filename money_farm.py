from time import sleep as wait
import pyrobloxbot as bot
import pyautogui as pg
import pydirectinput as dinput
from pynput.keyboard import Key, Controller


bot.UI_NAV_KEY = "`"
TRIES_TIL_SCROLL = 4

def switch_server():
    bot.ui_navigate_down()
    bot.ui_navigate_left()
    bot.ui_navigate_down()

    switched_server = False

    tries = 0

    while not switched_server:
        try:
            bot.ui_click() #Click join button
            wait(2) #Wait to join
            ok_button_coords = pg.locateCenterOnScreen("moneyfarm/ok_button.png", confidence=0.9) #Try to find ok button

            #Click ok button
            for i in range(2):
                dinput.click(ok_button_coords[0], ok_button_coords[1])
                dinput.moveRel(20, 0)

            tries += 1

            if tries >= TRIES_TIL_SCROLL:
                tries = 0 #Reset tries

                #Select scrollable region
                bot.ui_navigate_up()

                #Scroll down
                kb = Controller()
                for i in range(17):
                    kb.press(Key.page_down)
                    kb.release(Key.page_down)
                    wait(0.1)

                bot.ui_navigate_right()
                bot.ui_navigate_right()

            else:
                bot.ui_navigate_down()

        except pg.ImageNotFoundException:
            switched_server = True


def grab_chests():
    bot.walk_left(5)
    bot.walk_back(1)
    bot.walk_right(3)
    bot.jump(2)
    bot.walk_right(0.5)


def wait_for_game_to_load():
    while True:
        try:
            pg.locateOnScreen("moneyfarm/pirates.jpg")


def main():
    while True:
        #Pick marines
        bot.ui_navigate_left()
        bot.ui_click()
        bot.toggle_ui_navigation()

        #Open server menu
        bot.ui_click()
        bot.toggle_ui_navigation()
        
        #grab_chests()

        #switch_server()

        #wait(15) #Wait to join new server

main()