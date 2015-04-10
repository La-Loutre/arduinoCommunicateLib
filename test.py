from threadArduino import *
from arduinoParser import *
import traceback
import time

arduino_parser=ArduinoParser()
arduino_parser.setCutSymbole("#")
arduino_parser.setParseRules(["x","y","buttonJoystick","button_down","button_left","button_up","button_right","accx","accy","accz"],[int for i in range(10)])

thread=PollArduino()
thread.start()
time.sleep(2)
try:
    value = thread.getValue()
    print value
    print arduino_parser.parseArduino(value)
    thread.stop()
except Exception,err:
    print traceback.format_exc()
 #   print "Exited Anormally"
    thread.stop()
