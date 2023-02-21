
import mouse as ms
import keyboard as kb  
# Recording all the keyboard activities in the output  
recKeys = kb.record(until ='Esc')  
# Replaying back all the keys recorded from the keyboard  
#kb.play(recKeys, speed_factor = 1) 
print(recKeys)

