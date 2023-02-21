import pyautogui
import time
for i in range(10):
  pyautogui.moveTo(20, 418)
  pyautogui.rightClick()
  time.sleep(1)
  insertrow=pyautogui.locateCenterOnScreen('insertrowsformobsy.png')
  pyautogui.moveTo(137,400)
  pyautogui.click()
  time.sleep(1)
  if(i==0):
    time.sleep(10)

pyautogui.moveTo()

for i in range(6):
  pyautogui.moveRel()
