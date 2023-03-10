import pyautogui
#button7location = pyautogui.locateOnScreen('edit.png')
#button7location


#start snipping tool
windows =pyautogui.locateCenterOnScreen('windowsstart.png')
pyautogui.moveTo(windows)
pyautogui.click()
pyautogui.typewrite("snipping")


vdiimage= pyautogui.locateCenterOnScreen('vdiimage.png')
#print(button7location)
print(vdiimage)
pyautogui.moveTo(vdiimage)

