from blinkstick import blinkstick
from time import sleep

for bstick in blinkstick.find_all():
    try:
        while True:
           for x in xrange(0, 8):
            #trail
            bstick.set_color(channel =3, index = (x-1)%8, name="blue")
            bstick.set_color(channel =3, index = (x-2)%8, name="blue")
            bstick.set_color(channel =3, index = (x-3)%8, name="blue")
            bstick.set_color(channel =3, index = (x-4)%8, name="blue")
            #clear previous last light 
            bstick.set_color(channel =3, index = (x-5)%8)
            #head
            bstick.set_color(channel =3, index = x, name="green")
            sleep(0.1)
    except KeyboardInterrupt:
        pass
