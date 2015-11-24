from blinkstick import blinkstick
from time import sleep

for bstick in blinkstick.find_all():
    try:
        while True:
            for x in xrange(0, 8):
                #clear the previous light
                #mod by num lights to wrap around
                bstick.set_color(channel =3, index = (x-1)%8)               
                bstick.set_color(name="mediumorchid",channel=3, index=x)
                sleep(0.25)          
    except KeyboardInterrupt:
        pass


