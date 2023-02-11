import mouse as ms


#recmouse= ms.record()
#ms.play(recmouse, speed_factor = 1)
import time
while(True):
            if(ms.is_pressed()):
               print( ms.get_position())
               time.sleep(0.2)
            