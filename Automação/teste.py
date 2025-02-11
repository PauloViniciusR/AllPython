import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')

pyautogui.write('whatsapp')
pyautogui.press('enter')

time.sleep(2) 
pyautogui.write('eu')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)
pyautogui.press('enter')
pyautogui.write('a')
pyautogui.press('enter')

