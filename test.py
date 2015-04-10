from threadArduino import *
from arduinoParser import *
import traceback
import time


arduino_parser=ArduinoParser()
arduino_parser.setCutSymbole("#")
arduino_parser.setParseRules(["x","y"]+ArduinoParser.esploraButtonsNames+["accx","accy","accz"],[ArduinoParser.defaultParse,ArduinoParser.defaultParse,ArduinoParser.esploraButtonParse,ArduinoParser.esploraButtonParse,ArduinoParser.esploraButtonParse,ArduinoParser.esploraButtonParse,ArduinoParser.esploraButtonParse,ArduinoParser.defaultParse,ArduinoParser.defaultParse,ArduinoParser.defaultParse])

thread=PollArduino("/dev/ttyACM1")
thread.start()
time.sleep(2)
try:
    value = thread.getValue()
    print value
    parse=arduino_parser.parseArduino(value)
   
    print parse["buttonJoystick"]
    thread.stop()
except Exception,err:
    print traceback.format_exc()
 #   print "Exited Anormally"
    thread.stop()
