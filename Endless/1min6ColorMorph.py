from blinkstick import blinkstick
from time import sleep
 
for bstick in blinkstick.find_all():
    #clear lights
    bstick.turn_off()
    try:
        while True:
           bstick.morph(channel=0, steps=10, name="red", duration = 100)
           bstick.morph(channel=0, steps=10, name="blue", duration = 100)
           bstick.morph(channel=0, steps=10, name="green", duration = 100)
           bstick.morph(channel=0, steps=10, name="yellow", duration = 100)
           bstick.morph(channel=0, steps=10, name="purple", duration = 100)
           bstick.morph(channel=0, steps=10, name="orange", duration = 100)
    except KeyboardInterrupt:
        pass
