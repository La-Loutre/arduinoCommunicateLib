class ArduinoParser:
    def __init__(self,cutSymbole="#"):
        self.cutSymbole=cutSymbole
        self.tabNames=[]
        self.tabFunction=[]
        self.splitedNumber=0

    def setCutSymbole(self,cutSymbole):
        self.cutSymbole=cutSymbole

    def parseArduino(self,msg):
        msgsplited=msg.split(self.cutSymbole)
        size=len(msgsplited)
        msgSplitedTab={}
        if(self.splitedNumber == size):
            for i in range(size):
                msgSplitedTab[self.tabNames[i]]=self.tabFunction[i](msgsplited[i])
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
