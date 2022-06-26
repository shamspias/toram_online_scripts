import pyautogui
import basic_methods as toram_options
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

pyautogui.hotkey('alt', 'tab')
toram_options.recive_gifts(45)
# pyautogui.click('gift_recive.png')