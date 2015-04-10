from threading import Thread,Lock
import time
import serial

class PollArduino(Thread):
    def __init__(self,port="/dev/ttyACM0"):
        Thread.__init__(self)
        self.ser=serial.Serial(port,9600)
        self.shared=""
        self.notStopping=True
        self.started=False
    def stop(self):
        self.notStopping=False
    def run(self):
        self.started=True
        while(self.notStopping):
            self.shared=self.ser.readline()
            
            
    def getValue(self):
        if self.started:
            s=self.shared
            return s
        else:
            print "Thread not started !\n"
            return None




