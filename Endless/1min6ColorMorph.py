from blinkstick import blinkstick
from time import sleep
 
for bstick in blinkstick.find_all():
    #clear lights
    bstick.turn_off()
    numSteps=300
    dur = 999
    try:
        while True:
            bstick.morph(channel=0, steps=numSteps, name="red", duration = dur)
            sleep(.01)
            bstick.morph(channel=0, steps=numSteps, name="blue", duration = dur)
            sleep(.01)
            bstick.morph(channel=0, steps=numSteps, name="green", duration = dur)
            sleep(.01)
            bstick.morph(channel=0, steps=numSteps, name="yellow", duration = dur)
            sleep(.01)
            bstick.morph(channel=0, steps=numSteps, name="cyan", duration = dur)
            sleep(.01)
            bstick.morph(channel=0, steps=numSteps, name="orange", duration = dur)
            sleep(.01)
    except KeyboardInterrupt:
        pass
