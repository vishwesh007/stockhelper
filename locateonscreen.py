import pyautogui
#button7location = pyautogui.locateOnScreen('edit.png')
#button7location

editcenter= pyautogui.locateCenterOnScreen('usernameforpasswordvault.png')
#print(button7location)
print(editcenter)
pyautogui.moveTo(editcenter)