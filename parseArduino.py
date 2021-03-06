from subprocess import Popen
import fileinput
import math
import subprocess

DEBUG_INPUT = True
MAX_JOYSTICK_ARDUINO = 512
UNLOCK_BUTTONS=[True,True,True,True,True]
BUTTONS_NAMES=["Joystick button","switch_down button","switch_left button","switch_up button","switch_right button"]

## [0,6[ , one button <=> one action 
BUTTON_JOYSTICK=0
BUTTON_SWITCH_DOWN=1
BUTTON_SWITCH_LEFT=2
BUTTON_SWITCH_UP=3
BUTTON_SWITCH_RIGHT=4

BUTTONS_ROTATE_SWITCH=BUTTON_JOYSTICK
BUTTONS_SWITCH_MODE=BUTTON_SWITCH_DOWN
BUTTONS_FREE_WALKING=BUTTON_SWITCH_LEFT
BUTTONS_SWITCH_SPIDER_MODE=BUTTON_SWITCH_RIGHT
BUTTONS_SAVE=[0,0,0,0,0]


def buttonsSave():
    if(DEBUG_INPUT):
        print BUTTONS_SAVE
    return BUTTONS_SAVE
## Get the tab with 5 buttons values , 1 == pressed . 
## See buttons_names for order .
## Buttons cannot be hold . Only count for 1 time pressed for simplicity (UNLOCK_BUTTONS) .
def buttons(tabValue):
    tabRetour=[0,0,0,0,0]
    if(DEBUG_INPUT):
        print tabValue
    assert(len(tabValue)>=7)
    for i in range(2,7):
        assert(tabValue[i]==0 or  tabValue[i] == 1)
        ## Prevent buttons to be pressed multiple time by waiting each one to be released before watching them again
        ## 0011111001 -> 00100000001 
        if(UNLOCK_BUTTONS [i-2]) :
            tabRetour[i-2]=(tabValue[i]+1)%2
        else :
            tabRetour[i-2]=0
        if((tabValue[i]+1)%2 == 0):
            UNLOCK_BUTTONS[i-2]= True
        else:
            UNLOCK_BUTTONS[i-2]= False
    
    for i in range(5):
        BUTTONS_SAVE[i]=tabRetour[i]
    return tabRetour


def coeff(tabValue):
    assert(len(tabValue)>=2)
    if(tabValue[0]<0):
        signeX=-1
    else:
        signeX=1
    if(-tabValue[1]<0):
        signeY=-1
    else:
        signeY=1
    
    return [signeX*abs(tabValue[0])/512.,signeY*abs(tabValue[1])/512.]

def angleRad(tabValue):
    assert(len(tabValue)>=2)
    return math.atan2(-tabValue[1],-tabValue[0])


def direction(tabValue):
    directionX=0
    directionY=0
    assert(len(tabValue)>=2)
    if(tabValue[0]> 10 ):
        directionX=1
    elif (tabValue[0]< -10):
        directionX=-1
    if(tabValue[1]>10):
        directionY=1
    elif(tabValue[1]< -10):
        directionY=-1
    tabDirection=[-directionY,-directionX]
    if(tabDirection == [0,0]):
        return "waiting"
    elif (tabDirection == [0,1]):
        return "rightwalking"
    elif (tabDirection == [0,-1]):
        return "leftwalking"
    elif (tabDirection == [1,0]):
        return "forwardwalking"
    elif (tabDirection == [1,1]):
        return "forwardrightwalking"
    elif (tabDirection == [1,-1]):
        return "forwardleftwalking"
    elif (tabDirection == [-1,0]):
        return "backwardwalking"
    elif (tabDirection == [-1,1]):
        return "backwardrightwalking"
    elif (tabDirection == [-1,-1]):
        return "backwardleftwalking"
    else :
        return None
    
def parseArduino(msg,symbole):
    msgsplited=msg.split(symbole)
    size=len(msgsplited)
    msgSplitedInt=[0 for i in range(size)]
    if(len(msgsplited)==size):
        for i in range(size):
            msgSplitedInt[i]=int(msgsplited[i])
        return msgSplitedInt
    return None
