from time import sleep as wait
from datetime import datetime
import pyrobloxbot as bot
import pyautogui as pg
import pydirectinput as dinput
from pynput.keyboard import Key, Controller


bot.UI_NAV_KEY = "\\"
TRIES_TIL_SCROLL = 4

@bot.require_focus
def mega_click(coords, relx=20, rely=0):
    for i in range(2):
        dinput.click(coords[0], coords[1])
        dinput.moveRel(relx, rely)


def switch_server():
    bot.ui_navigate_left()

    #Scroll down
    kb = Controller()
    for i in range(50):
        kb.press(Key.page_down)
        kb.release(Key.page_down)
        wait(0.05)
    
    switched_server = False

    tries = 0

    while not switched_server:
        join_button_coords = pg.locateAllOnScreen("moneyfarm/join.jpg", confidence=0.7)

        for box in join_button_coords:
            #center = (box.left+(round(box.width/2)), box.top+(round(box.height/2)))
            center = (box.left+10, box.top+5)
            mega_click(center)
            center = (box.left+10, box.top)
            mega_click(center)

            wait(2)
            
            #Check if server was full
            try:
                ok_button_coords = pg.locateCenterOnScreen("moneyfarm/ok_button.png", confidence=0.9) #Try to find ok button

                #Click ok button
                for i in range(2):
                    dinput.click(ok_button_coords[0], ok_button_coords[1])
                    dinput.moveRel(20, 0)

            except pg.ImageNotFoundException:
                switched_server = True
        
        #Scroll down
        kb = Controller()
        for i in range(17):
            kb.press(Key.page_down)
            kb.release(Key.page_down)
            wait(0.1)



def grab_chests():
    #bot.reset_player()
    #wait(5)

    bot.walk_left(5)
    bot.jump(3)
    bot.walk_left(0.1)
    bot.walk_back(1.5)
    bot.walk_right(2)
    bot.jump(2)
    bot.walk_right(0.5)
    bot.jump(5, 0.1)
    dinput.keyDown("s")
    for i in range(3):
        bot.jump(1)
        wait(0.3)
    dinput.keyUp("s")
    bot.walk_forward(0.2)
    wait(0.35)
    bot.walk_back(0.4)
    bot.walk_left(0.75)
    bot.walk_right(1.50)
    bot.walk_back(0.1)



def wait_for_game_to_load():
    try:
        pg.locateOnScreen("moneyfarm/marine_join.jpg", confidence=0.7)
        print("Joined new server at", str(datetime.now().time()).split(".")[0])
        bot.UI_NAV_ENABLED = False
        return 0
    except pg.ImageNotFoundException:
        wait_for_game_to_load()


def main():
    servers_visited = 0
    while True:
        wait_for_game_to_load()

        servers_visited += 1
        print("Servers visited:", servers_visited)

        #Pick marines
        while True:
            try:
                mega_click(pg.locateCenterOnScreen("moneyfarm/marine_join.jpg", confidence=0.7))
                break
            except pg.ImageNotFoundException:
                pass
        #bot.toggle_ui_navigation()
        #bot.ui_navigate_left()
        #bot.ui_click()

        wait(1.5)

        #Open server menu
        bot.ui_click()
        bot.toggle_ui_navigation()
        
        grab_chests()

        switch_server()


main()