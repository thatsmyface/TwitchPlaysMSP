import mouse
import keyboard
import datetime
import time
import random

def colToNum(color):
    if color == "red":
        return(0)
    elif color == "orange":
        return(1)
    elif color == "yellow":
        return(2)
    elif color == "green":
        return(3)
    elif color == "blue":
        return(4)
    elif color == "purple":
        return(5)
    elif color == "black":
        return(6)
    elif color == "white":
        return(7)
    else:
        raise Exception('Color invalid')

def colorChange(color):
    px = mouse.get_position()[0]
    py = mouse.get_position()[1]

    if color == 0:
        mouse.move(641,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 1:
        mouse.move(662,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 2:
        mouse.move(685,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 3:
        mouse.move(705,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 4:
        mouse.move(729,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 5:
        mouse.move(773,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 6:
        mouse.move(572,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif color == 7:
        mouse.move(572,85)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    else:
        raise Exception('Color invalid')

    mouse.move(px, py)

def colorChangeAgain(pcolor):
    px = mouse.get_position()[0]
    py = mouse.get_position()[1]

    if pcolor == 0:
        mouse.move(641,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 1:
        mouse.move(662,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 2:
        mouse.move(685,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 3:
        mouse.move(705,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 4:
        mouse.move(729,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 5:
        mouse.move(773,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 6:
        mouse.move(572,68)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif pcolor == 7:
        mouse.move(572,85)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    else:
        raise Exception('Color invalid')

    mouse.move(px, py)

def draw(xModif, yModif): 
    x = mouse.get_position()[0]
    y = mouse.get_position()[1]
    xF = x + int(xModif)
    yF = y + int(yModif)

    if (xF < 5):
        xF = 5
    if (yF < 150):
        yF = 150
    if (xF > 965):
        xF = 965
    if (yF > 730):
        yF = 730
    
    mouse.drag(x, y, xF, yF )

def drawStart(relstartX, relstartY, relfinalX, relfinalY):
    startX = int(relstartX)  + 5
    startY = int(relstartY) + 150
    xF = int(relfinalX)  + 5
    yF = int(relfinalY) + 150

    if (xF < 5):
        xF = 5
    if (yF < 150):
        yF = 150
    if (xF > 965):
        xF = 965
    if (yF > 730):
        yF = 730

    mouse.drag(startX, startY, xF, yF)

def fill(x,y,color):
    px = mouse.get_position()[0]
    py = mouse.get_position()[1]

    xF = int(x)  + 5
    yF = int(y) + 150

    if (xF < 5):
        xF = 5
    if (yF < 150):
        yF = 150
    if (xF > 965):
        xF = 965
    if (yF > 730):
        yF = 730

    # select fill color
    colorChange(colToNum(str(color)))
    # press can
    mouse.move(196,77)
    time.sleep(0.1)
    mouse.press(button='left')
    time.sleep(0.1)
    mouse.release(button='left')
    time.sleep(0.1)
    #press point
    mouse.move(xF, yF)
    time.sleep(0.1)
    mouse.press(button='left')
    time.sleep(0.1)
    mouse.release(button='left')
    time.sleep(0.1)
    #press brush
    mouse.move(269,79)
    time.sleep(0.1)
    mouse.press(button='left')
    time.sleep(0.1)
    mouse.release(button='left')
    time.sleep(0.1)
    #return mouse
    mouse.move(px,py)
    time.sleep(0.1)

def save():
    keyboard.send('ctrl+n')
    keyboard.send('enter')
    timeString = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(":","")
    keyboard.write(timeString+"_SAVED")
    keyboard.send('enter')
    #Post to Twitter

def changeSize(size):
    px = mouse.get_position()[0]
    py = mouse.get_position()[1]
    size = int(size)
    if (size == 1):
        mouse.move(447,78)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
        time.sleep(0.1)
        mouse.move(488,148)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif (size == 2):
        mouse.move(447,78)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
        time.sleep(0.1)
        mouse.move(482,188)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif (size == 3):
        mouse.move(447,78)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
        time.sleep(0.1)
        mouse.move(478,225)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    elif (size == 4):
        mouse.move(447,78)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
        time.sleep(0.1)
        mouse.move(481,265)
        time.sleep(0.1)
        mouse.press(button='left')
        time.sleep(0.1)
        mouse.release(button='left')
    else:
        raise Exception('Size invalid')

    mouse.move(px,py)

def randomThing():
    lines = open('things.txt').read().splitlines()
    myline = random.choice(lines)
    text_file = open("Goal.txt", "w")
    text_file.write(str(myline))
    text_file.close()
    print("New Theme:" + myline)

def test():
    while True:
        print mouse.get_position()
    