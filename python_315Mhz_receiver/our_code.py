#!/usr/bin/env python3

from datetime import datetime
from time import sleep

OK = 0
USER_COMMAND_RECEIVED = 1

def waitForLongPause( ):
    print (">> waitForLongPause")

    last_read =

    sleep(0.5)
    return "B"



last_read = micros();

while(1) {

unsigned long time_since_last_read = micros() - last_read;          //how long has it been since we last read a byte?
bool clock = digitalRead(clkPin);

if (!clock && time_since_last_read >= 2000) {
return OK;
} else if (clock) {
last_read = micros();
}

delayMicroseconds(2);

char inByte = this->handleUserCommand();
if (inByte != EMPTY_CHAR) {
userCmdReceived = inByte;
return USER_COMMAND_RECEIVED;
}
}





def waitForPacketStart( ):
    print (">> waitForPacketStart")
    sleep(0.5)
    return "C"

def waitForPacketEnd( ):
    print (">> waitForPacketEnd")
    sleep(0.5)
    return "D"

def readPacket( ):
    print (">> readPacket")
    sleep(0.5)
    return "E"

def processPacket( ):
    print (">> processPacket")
    sleep(0.5)
    return "F"

if __name__ == '__main__':
    while True:
        iPhase = 0
        iStatus = OK

        packetProcessingPhase = {
            0 : waitForLongPause,
            1 : waitForPacketStart,
            2 : waitForPacketEnd,
            3 : waitForPacketStart,
            4 : readPacket,
            5 : processPacket
        }

        while (iStatus == OK and iPhase <= 5):
            iStatus = packetProcessingPhase[iPhase]()
            print (">> " + iStatus)
            iPhase = iPhase + 1

        # if (iStatus == USER_COMMAND_RECEIVED and userCmdReceived != EMPTY_CHAR):
        #     return USER_COMMAND_RECEIVED

