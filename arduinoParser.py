class ArduinoParser:
    esploraButtonsNames=["buttonJoystick","button_down","button_left","button_up","button_right"]
    
    esploraButtonsPressed={esploraButtonsNames[0]:False,esploraButtonsNames[1]:False,esploraButtonsNames[2]:False,esploraButtonsNames[3]:False,esploraButtonsNames[4]:False}

    def __init__(self,cutSymbole="#"):
        self.cutSymbole=cutSymbole
        self.tabNames=[]
        self.tabFunction=[]
        self.splitedNumber=0

    def setCutSymbole(self,cutSymbole):
        self.cutSymbole=cutSymbole

    @staticmethod
    def esploraButtonParse(value,name):
        value=int(value)
        value=(value+1)%2
        if not ArduinoParser.esploraButtonsPressed[name] and value == 1:
            ArduinoParser.esploraButtonsPressed[name]=True
            return True
        elif value==0 :
            ArduinoParser.esploraButtonsPressed[name]=False
        return False

    @staticmethod
    def defaultParse(a,b):
        return a
    def parseArduino(self,msg):
        msgsplited=msg.split(self.cutSymbole)
        size=len(msgsplited)
        msgSplitedTab={}
        if(self.splitedNumber == size):
            for i in range(size):
                msgSplitedTab[self.tabNames[i]]=self.tabFunction[i](msgsplited[i],self.tabNames[i])
            return msgSplitedTab
        print self.splitedNumber 
        print size
        return None

    def setParseRules(self,tabNames,tabFunction):
        if(len(tabNames) == len(tabFunction)):
            self.tabNames=tabNames
            self.tabFunction=tabFunction
            self.splitedNumber=len(tabNames)
        else:
            print "Error , len(tabNames) != len(tabFunction) \nNot updated"
