from PIL import Image
from pyrobloxbot import image_is_visible
from desktopmagic.screengrab_win32 import getScreenAsImage
import pyscreeze as screeze

try:
    #This is the actual full monitors function
    screeze.locate("moneyfarm\\marine_join.jpg", getScreenAsImage(), confidence=0.7)
    print(True)
except screeze.ImageNotFoundException:
    print(False)
print(image_is_visible("moneyfarm\\marine_join.jpg"), confidence=0.7)