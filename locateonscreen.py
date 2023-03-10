import pyautogui
#button7location = pyautogui.locateOnScreen('edit.png')
#button7location
import time

time.sleep(10)
editcenter= pyautogui.locateCenterOnScreen('open.png')
#print(button7location)
print(editcenter)
pyautogui.moveTo(editcenter)