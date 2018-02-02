import win32api, win32con
import ImageGrab
import os
import time
import ImageOps
from numpy import *

# Globals
# ---------

x_pad = 463
y_pad = 353


def screenGrab() :
    im = ImageGrab.grab(bbox = (x_pad+1,y_pad+1,x_pad+641,y_pad+480))

    ##im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im

def grab() :
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+1,y_pad+1,x_pad+641,y_pad+480)))
    a = array(im.getcolors())
    a = a.sum()
    print a
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    print "Click"

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left Release'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def startGame():
    #location of the first menu
    mousePos((x_pad-153, y_pad-148))
    leftClick()
    time.sleep(.1)

    #location of second menu
    mousePos((x_pad-148, y_pad+43))
    leftClick()
    time.sleep(.1)

    #location of third menu
    mousePos((x_pad+116, y_pad+101))
    leftClick()
    time.sleep(.1)

    #location of fourth menu
    mousePos((x_pad-152, y_pad+23))
    leftClick()
    time.sleep(.1)

class Cord:

    f_shrimp = (37,338)
    f_rice = (94,335)
    f_nori = (41,392)
    f_roe = (91,393)
    f_salmon = (38,450)
    f_unagi = (93,450)

#------------------------
    
    phone = (586, 368)
 
    menu_toppings = (530, 274)
     
    t_shrimp = (496, 228)
    t_nori = (497, 282)
    t_roe = (576, 282)
    t_salmon = (493, 334)
    t_unagi = (577, 225)
    t_exit = (593, 335)
 
    menu_rice = (520, 295)
    buy_rice = (545, 283)

    menu_sake = (521, 316)
    
    delivery_norm = (495, 296)

def clear_tables():
    mousePos((95, 212))
    leftClick()
 
    mousePos((195, 211))
    leftClick()
 
    mousePos((298, 210))
    leftClick()
 
    mousePos((397, 212))
    leftClick()
 
    mousePos((497, 211))
    leftClick()
 
    mousePos((603, 210))
    leftClick()
    time.sleep(1)

def makeFood(food):
    if food == 'caliroll':
        print 'Making a caliroll'
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)
     
    elif food == 'onigiri':
        print 'Making a onigiri'
        foodOnHand['rice'] -= 2 
        foodOnHand['nori'] -= 1
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(.05)
         
        time.sleep(1.5)
 
    elif food == 'gunkan':
        print 'Making a gunkan'
        foodOnHand['rice'] -= 1 
        foodOnHand['nori'] -= 1 
        foodOnHand['roe'] -= 2 
        mousePos(Cord.f_rice)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.1)
        mousePos(Cord.f_nori)
        leftClick()
        time.sleep(.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(.05)
        foldMat()
        time.sleep(1.5)


def foldMat():
    mousePos((Cord.f_rice[0]+40,Cord.f_rice[1])) 
    leftClick()
    time.sleep(.1)

def buyFood(food):
     
    mousePos(Cord.phone)
     
    mousePos(Cord.menu_toppings)
     
     
    mousePos(Cord.t_shrimp)
    mousePos(Cord.t_nori)
    mousePos(Cord.t_roe)
    mousePos(Cord.t_salmon)
    mousePos(Cord.t_unagi)
    mousePos(Cord.t_exit)
     
    mousePos(Cord.menu_rice)
    mousePos(Cord.buy_rice)

    mousePos(Cord.menu_sake)
    
    mousePos(Cord.delivery_norm)

def buyFood(food):
     
    if food == 'rice':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_rice)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.buy_rice) != (34, 16, 41):
            print 'rice is available'
            mousePos(Cord.buy_rice)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['rice'] += 10     
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'rice is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
             
    if food == 'nori':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
        print 'test'
        time.sleep(.1)
        if s.getpixel(Cord.t_nori) != (38, 130, 255):
            print 'nori is available'
            mousePos(Cord.t_nori)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['nori'] += 10         
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'nori is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)
 
    if food == 'roe':
        mousePos(Cord.phone)
        time.sleep(.1)
        leftClick()
        mousePos(Cord.menu_toppings)
        time.sleep(.05)
        leftClick()
        s = screenGrab()
         
        time.sleep(.1)
        if s.getpixel(Cord.t_roe) != (54, 9, 72):
            print 'roe is available'
            mousePos(Cord.t_roe)
            time.sleep(.1)
            leftClick()
            mousePos(Cord.delivery_norm)
            foodOnHand['roe'] += 10                
            time.sleep(.1)
            leftClick()
            time.sleep(2.5)
        else:
            print 'roe is NOT available'
            mousePos(Cord.t_exit)
            leftClick()
            time.sleep(1)
            buyFood(food)

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe':
            if j <= 2:
                print '%s is low and needs to be replenished' % i
                buyFood(i)


def get_seat_one(): 
    im = ImageOps.grayscale(ImageGrab.grab(bbox=(x_pad+28,y_pad+61,x_pad+28+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    ##print a
    ##im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')    
    return a


def get_seat_two():
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+129,y_pad+61,x_pad+129+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    ##im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_three():
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+230,y_pad+61,x_pad+230+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    
    ##im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_four():
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+331,y_pad+61,x_pad+331+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    
    ##im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_five():
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+432,y_pad+61,x_pad+432+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    
    ##im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')    
    return a

def get_seat_six():
    im = ImageOps.grayscale(ImageGrab.grab(bbox = (x_pad+533,y_pad+61,x_pad+533+59,y_pad+61+15)))
    a = array(im.getcolors())
    a = a.sum()
    
    ##im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')    
    return a
 
def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()
      
sushiTypes = {2321:'onigiri', 
              2794:'caliroll',
              2328:'gunkan',}

class Blank:
    seat_1 = 6465
    seat_2 = 5738
    seat_3 = 10418
    seat_4 = 10601
    seat_5 = 6785
    seat_6 = 7932

def check_bubs():
 
    checkFood()
    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if sushiTypes.has_key(s1):
            print 'table 1 is occupied and needs %s' % sushiTypes[s1]
            makeFood(sushiTypes[s1])
        else:
            print 'sushi not found!\n sushiType = %i' % s1
 
    else:
        print 'Table 1 unoccupied'
 
    clear_tables()
    checkFood()
    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if sushiTypes.has_key(s2):
            print 'table 2 is occupied and needs %s' % sushiTypes[s2]
            makeFood(sushiTypes[s2])
        else:
            print 'sushi not found!\n sushiType = %i' % s2
 
    else:
        print 'Table 2 unoccupied'
 
    checkFood()
    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if sushiTypes.has_key(s3):
            print 'table 3 is occupied and needs %s' % sushiTypes[s3]
            makeFood(sushiTypes[s3])
        else:
            print 'sushi not found!\n sushiType = %i' % s3
 
    else:
        print 'Table 3 unoccupied'
 
    checkFood()
    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if sushiTypes.has_key(s4):
            print 'table 4 is occupied and needs %s' % sushiTypes[s4]
            makeFood(sushiTypes[s4])
        else:
            print 'sushi not found!\n sushiType = %i' % s4
 
    else:
        print 'Table 4 unoccupied'
 
    clear_tables()
    checkFood()
    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if sushiTypes.has_key(s5):
            print 'table 5 is occupied and needs %s' % sushiTypes[s5]
            makeFood(sushiTypes[s5])
        else:
            print 'sushi not found!\n sushiType = %i' % s5
 
    else:
        print 'Table 5 unoccupied'
 
    checkFood()
    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if sushiTypes.has_key(s6):
            print 'table 1 is occupied and needs %s' % sushiTypes[s6]
            makeFood(sushiTypes[s6])
        else:
            print 'sushi not found!\n sushiType = %i' % s6
 
    else:
        print 'Table 6 unoccupied'
 
    clear_tables()
    time.sleep(3)


def main() :
    startGame()
    while True:
        check_bubs()

if __name__ == '__main__':
    main()
