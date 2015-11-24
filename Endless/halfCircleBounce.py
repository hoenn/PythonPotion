from blinkstick import blinkstick
from time import sleep

for bstick in blinkstick.find_all():
    bstick.turn_off()
    try:
        while True:
           for x in xrange(0, 8):
            bstick.set_color(channel =3, index = x, name="purple")
            bstick.set_color(channel =3, index = 8-x-1, name="green")
            sleep(0.1)
    except KeyboardInterrupt:
        pass
