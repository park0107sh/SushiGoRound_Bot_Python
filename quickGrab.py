import ImageGrab
import os
import time


# Globals
# ---------

x_pad = 463
y_pad = 353


def screenGrab() :
    im = ImageGrab.grab(bbox = (x_pad+1,y_pad+1,x_pad+641,y_pad+480))
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main() :
    screenGrab()

if __name__ == '__main__':
    main()

