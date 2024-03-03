from time import sleep as wait
import pyscreeze as screeze
from desktopmagic.screengrab_win32 import getScreenAsImage
from windows_toasts import Toast, WindowsToaster
import pyrobloxbot as bot

GAME_ID = 2753915549

def send_notification(title="", subtitle="", body1="", body2=""):
    toaster = WindowsToaster(title)
    toast = Toast([subtitle,body1,body2])
    toaster.show_toast(toast)

def wait_for_game_launch():
    while not bot.image_is_visible("moneyfarm\\marine_join.jpg", confidence=0.7):
        wait(0.1)

def boss_bar_is_visible():
    try:
        screeze.locate("bossbar.png", getScreenAsImage(), confidence=0.9)
        return True
    except screeze.ImageNotFoundException:
        return False

while not boss_bar_is_visible():
    bot.launch_game(GAME_ID)
    wait_for_game_launch()

    #Pick marines
    bot.ui_navigate_left()
    bot.ui_click()
    bot.toggle_ui_navigation()

    wait(3)

#send_notification("Found cursed captain")
print(boss_bar_is_visible())