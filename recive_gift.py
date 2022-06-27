import pyautogui
import basic_methods as toram_options
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

number = int(input("Number of gift want to recive: "))
pyautogui.hotkey('alt', 'tab')
toram_options.recive_gifts(number)
# pyautogui.click('gift_recive.png')