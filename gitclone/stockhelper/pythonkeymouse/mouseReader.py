# import mouse as ms


# recmouse= ms.record()
# print(recmouse)
# f= open("C:\Users\vishwesh.chicklinge\Desktop\pyexample1.txt")
# f.write(recmouse)
# f.close()
# ms.play(recmouse, speed_factor = 1)
# import time
# while(True):
#            # if(ms.is_pressed()):
#                print( ms.get_position())
#                time.sleep(10)
import threading
import mouse
import keyboard

mouse_events = []


mouse.hook(mouse_events.append)
keyboard.start_recording()

keyboard.wait("a")

mouse.unhook(mouse_events.append)
keyboard_events = keyboard.stop_recording()

#Keyboard threadings:

k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
k_thread.start()

#Mouse threadings:

m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
m_thread.start()

#waiting for both threadings to be completed

k_thread.join() 
m_thread.join()