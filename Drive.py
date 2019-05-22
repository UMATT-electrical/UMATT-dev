import RPi.GPIO as GPIO
import time
from multiprocessing import  Queue
import math

p_clk = 23
p_mosi = 10
p_miso = 25
p_potSelect = 8
p_ADCSelect = 5
p_powerDown = 12
p_GPIO1Select = 24
p_GPIO2Select = 9
p_GPIO3Select = 11
p_GPIO4Select = 6
p_AccessoryPower = 16

accPwr = 1

bounceTimeThreshN = 1
bounceTimeThresh = 1

motorEnableSuccess = 0

acceptableJoystickMaps = [0]
accelMax = 1
accelMin = 1
diffMinTime = 0.5

def run(Quodi, Quido):
    initGPIO()
    initXPNDR()
    initPot()

    #internally calculated
    brake = 0
    clutch = 0
    throttle = 0
    enableMotor = 0
    forwards = 0
    reverse = 0
    neutral = 1
    gearlockout = [0, 0]
    fans = 0
    pump = 0
    LAExtend = 0
    LARetract = 0
    bounceTimer = 0
    diffSpeed = 0
    
    #externally set
    modeManeuverability = 1
    modePulling = 0
    diffLockRequest = 0
    joystickMapping = 0 #0 = linear
    Acceleration = 0 #0 = no limitation
    Deceleration = 0 #0 = no limitation
    interlockOverride = 0
    
    writeGPIOA(p_GPIO3Select, [1,1,1,1,1,1,1,1])
    writeGPIOA(p_GPIO3Select, [0,0,0,0,0,0,0,0])
    diffLastTime = time.time()
    
    
    while True:
        GPIO1AValues = readGPIOA(p_GPIO1Select)
        joystick = readADC(1)
        if neutral == 1:
            inching = 0
            brake = 0
            clutch = 0
            enableMotor = 0
            throttle = 0.
            fans = 0
            
            if GPIO1AValues[3] == 1 and GPIO1AValues[2] == 0 and (1 not in (gearlockout)) and bounceTimer != 0 and time.time()  > bounceTimer + bounceTimeThreshN:
                if joystick <= 548:
                    forwards = 1
                    reverse = 0
                    neutral = 0
                else:
                    gearlockout_001 = 1
            elif GPIO1AValues[2] == 1 and GPIO1AValues[3] == 0 and (1 not in (gearlockout)) and bounceTimer != 0 and time.time()  > bounceTimer + bounceTimeThreshN:
                if joystick <= 548:
                    forwards = 0
                    reverse = 1
                    neutral = 0
                else:
                    print('Pull Joystick back to switch to Reverse')
                    gearlockout_001 = 1
            
            if joystick <= 548 and GPIO1AValues[2] == 0 and GPIO1AValues[3] == 0:
                gearlockout[0] = 0
                gearlockout[1] = 0

            if (GPIO1AValues[3] == 1 or GPIO1AValues[2] == 1)  and bounceTimer == 0:
                bounceTimer = time.time()

            if bounceTimer != 0 and (GPIO1AValues[3] == 0 and GPIO1AValues[2] == 0):
                bounceTimer = 0
    
        if forwards == 1 and modePulling == 1:
            fans = 1
            inching = 0

            if joystick <= 548:
                brake = 1
            else:
                brake = 0
            if joystick >= 695:
                clutch = 1
            else:
                clutch = 0
            if joystick >= 843:
                throttle = (joystick - 843)/2507.
                enableMotor = 1
            else:
                throttle = 0.
                enableMotor = 0

            if GPIO1AValues[3] == 0 and bounceTimer != 0 and time.time()  > bounceTimer + bounceTimeThresh:
                forwards = 0
                reverse = 0
                neutral = 1
                enableMotor = 0
                throttle = 0.
                brake = 0
                clutch = 0
                fans = 0

            if GPIO1AValues[3] == 0 and bounceTimer == 0:
                bounceTimer = time.time()

            if bounceTimer != 0 and GPIO1AValues[3] == 1:
                bounceTimer = 0
        
        if forwards == 1 and modeManeuverability == 1:
            fans = 1
            brake = 1
            clutch = 0

            
            if joystick >= 548:
                throttle = ((joystick - 584)/2802.)#((joystick - 584)/2802.)**4
                enableMotor = 1
            else:
                throttle = 0.
                enableMotor = 0
            #if 548 <= joystick <= 695:
            #    inching = 1
            #else:
            #    inching = 0

            if GPIO1AValues[3] == 0 and bounceTimer != 0 and time.time()  > bounceTimer + bounceTimeThresh:
                forwards = 0
                reverse = 0
                neutral = 1
                enableMotor = 0
                throttle = 0.
                brake = 0
                clutch = 0
                fans = 0

            if GPIO1AValues[3] == 0 and bounceTimer == 0:
                bounceTimer = time.time()

            if bounceTimer != 0 and GPIO1AValues[3] == 1:
                bounceTimer = 0

        if reverse == 1:
            brake = 1
            clutch = 0
            fans  = 1
            inching = 0
            
            if joystick >= 695:
                enableMotor = 1
            else:
                enableMotor = 0
            if joystick >= 843:
                throttle = ((joystick - 843)/2507.)**2
            else:
                throttle = 0.

            if GPIO1AValues[2] == 0 and bounceTimer != 0 and time.time()  > bounceTimer + bounceTimeThresh:
                forwards = 0
                reverse = 0
                neutral = 1
                enableMotor = 0
                throttle = 0.
                brake = 0
                clutch = 0
                fans = 0

            if GPIO1AValues[2] == 0 and bounceTimer == 0:
                bounceTimer = time.time()

            if bounceTimer != 0 and GPIO1AValues[2] == 1:
                bounceTimer = 0

        if time.time() - diffLastTime > diffMinTime:
            diffPulseCount = binaryToDecimal(readGPIOB(p_GPIO3Select))
            diffSpeed = diffPulseCount/float(time.time() - diffLastTime)*3600/54.*25*math.pi/63360. #[mph]
            writeGPIOA(p_GPIO3Select, [1,1,1,1,1,1,1,1])
            writeGPIOA(p_GPIO3Select, [0,0,0,0,0,0,0,0])
            diffLastTime = time.time()

        #accPwr = GPIO.input(p_AccessoryPower)
        '''forwards = 1
        brake = 1
        clutch = 0
        enableMotor = 1
        if joystick >600:
            clutch =1
            brake = 0
        else:
            clutch = 0
            brake = 1
        '''        
        writeGPIOB(p_GPIO1Select, [brake,clutch,0,0,0,0,fans,fans])
        writeGPIOB(p_GPIO4Select, [0,inching,0,reverse,forwards,enableMotor,0,0])
        
        '''if joystic >600:
            clutch =1
            brake = 0
        else:
            clutch = 0
            brake = 1
        '''
        
        setPot(throttle)

        Quido.put((brake, clutch, throttle, enableMotor, forwards, reverse,
                    neutral, gearlockout, fans, pump, LAExtend, LARetract,
                    GPIO1AValues, modeManeuverability, modePulling, diffSpeed,
                   accPwr))
        try:
            data = Quodi.get(False)
        except:
            data = None

        if data:
            if data[0] == 1: #set to maneuverability
                if neutral == 1:
                    modeManeuverability = 1
                    modePulling = 0
            if data[0] == 2: #set to pulling
                if neutral == 1:
                    modeManeuverability = 0
                    modePulling = 1
            if data[0] == 3: #set/unset difflock
                if neutral == 1:
                    if data[1] == 1:
                        diffLockRequest = 1
                    elif data[1] == 0:
                        diffLockRequest = 0
            if data[0] == 4: #set joystickMapping
                if neutral == 1:
                    if data[1] in acceptableJoystickMaps:
                        joystickMapping = data[1]
            if data[0] == 5: #set Acceleration
                if neutral == 1:
                    if accelMin <= data[1] <= accelMax:
                        Acceleration = data[1]
            if data[0] == 6: #set Acceleration
                if neutral == 1:
                    if accelMin <= data[1] <= accelMax:
                        Deceleration = data[1]
            if data[0] == 7: #interlock override
                if data[1] == 1:
                    interlockOverride = 1
                elif data[1] == 0:
                    interlockOverride = 0

            if data[0] == 100: #powerdown
                if neutral == 1:
                    if GPIO.input(p_AccessoryPower) == 0:
                        #GPIO.output(p_powerDown, 1)
                        pass


def writeGPIOB(slave, byte):
    message = [0,1,0,0,0,0,0,0, 0,0,0,1,0,0,1,1] + byte
    writeSPI(slave, message) #write GPIOB

def writeGPIOA(slave, byte):
    message = [0,1,0,0,0,0,0,0, 0,0,0,1,0,0,1,0] + byte
    writeSPI(slave, message) #write GPIOB

def readGPIOA(slave):
    message = [0,1,0,0,0,0,0,1, 0,0,0,1,0,0,1,0]
    return readGPIOSPI(slave, message) #write GPIOB

def readGPIOB(slave):
    message = [0,1,0,0,0,0,0,1, 0,0,0,1,0,0,1,1]
    return readGPIOSPI(slave, message) #write GPIOB

def setPot(value):
    value = max(0., min(1., 1. - value))
    message = [0,0,0,1,0,0,0,1] + int2Bin(int(value*255))
    
    writeSPI(p_potSelect, message)

def int2Bin(integer):
    binaryText = bin(integer)[2:]
    binary = []
    for ii in range(8-len(binaryText)):
        binary.append(0)
    for ii in range(len(binaryText)):
        binary.append(int(binaryText[ii]))
    return binary

def initXPNDR():
    #GPIO1
    writeSPI(p_GPIO1Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1)) #write IODIRA
    writeSPI(p_GPIO1Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,0)) #write IODIRB

    writeGPIOB(p_GPIO1Select, [0,0,0,0,0,0,0,0])
    
    writeSPI(p_GPIO2Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1)) #write IODIRA
    writeSPI(p_GPIO2Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1))#write IODIRB
    

    writeSPI(p_GPIO3Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0)) #write IODIRA
    writeSPI(p_GPIO3Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 1,1,1,1,1,1,1,1)) #write IODIRB
    
    writeSPI(p_GPIO4Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1)) #write IODIRA
    writeSPI(p_GPIO4Select, (0,1,0,0,0,0,0,0, 0,0,0,0,0,0,0,1, 0,0,0,0,0,0,0,1))


def writeSPI(slave, message):
    GPIO.output(slave, 0)
    #time.sleep(0.005)
    for entry in message:
        GPIO.output(p_mosi, entry)
        GPIO.output(p_clk, 1)
        #time.sleep(0.005)
        GPIO.output(p_clk, 0)
        #time.sleep(0.005)
    GPIO.output(p_mosi, 0)
    GPIO.output(slave, 1)
    #time.sleep(0.005)

def readADC(channel):
    read = []
    message = [0,1,1]
    binChannel = int2Bin(channel)[-3:]
    message += binChannel
    GPIO.output(p_ADCSelect, 0)
    message = (0,1,1,0,0,1)
    for entry in message:
        GPIO.output(p_mosi, entry)
        GPIO.output(p_clk, 1)
        GPIO.output(p_clk, 0)
    GPIO.output(p_mosi, entry)
    GPIO.output(p_clk, 1)
    GPIO.output(p_clk, 0)
    for xx in range(12):
        GPIO.output(p_clk, 1)
        GPIO.output(p_clk, 0)
        read.append(GPIO.input(p_miso))
        
    GPIO.output(p_ADCSelect, 1)
    return binaryToDecimal(read)

def readGPIOSPI(slave, message):
    GPIO.output(slave, 0)
    #time.sleep(0.005)
    read = []
    for entry in message:
        GPIO.output(p_mosi, entry)
        GPIO.output(p_clk, 1)
        #time.sleep(0.005)
        GPIO.output(p_clk, 0)
        #time.sleep(0.005)
    for entry in range(8):
        GPIO.output(p_clk, 1)
        #time.sleep(0.005)
        read.append(GPIO.input(p_miso))
        GPIO.output(p_clk, 0)
        #time.sleep(0.005)
    GPIO.output(slave, 1)
    #time.sleep(0.005)
    return read
    
def initGPIO():
    #GPIO.init()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(p_clk, GPIO.OUT)
    GPIO.setup(p_mosi, GPIO.OUT)
    GPIO.setup(p_miso, GPIO.IN)
    GPIO.setup(p_potSelect, GPIO.OUT)
    GPIO.setup(p_ADCSelect, GPIO.OUT)
    GPIO.setup(p_powerDown, GPIO.OUT)
    GPIO.setup(p_GPIO1Select, GPIO.OUT)
    GPIO.setup(p_GPIO2Select, GPIO.OUT)
    GPIO.setup(p_GPIO3Select, GPIO.OUT)
    GPIO.setup(p_GPIO4Select, GPIO.OUT)
    GPIO.setup(p_AccessoryPower, GPIO.IN)

    GPIO.output(p_clk, 0)
    GPIO.output(p_mosi, 0)
    GPIO.output(p_potSelect, 1)
    GPIO.output(p_ADCSelect, 1)
    GPIO.output(p_GPIO1Select, 1)
    GPIO.output(p_GPIO2Select, 1)
    GPIO.output(p_GPIO3Select, 1)
    GPIO.output(p_GPIO4Select, 1)
    GPIO.output(p_powerDown,0)

def initPot():
    value = 1.0
    message = [0,0,0,1,0,0,0,1] + int2Bin(int(value*255))
    writeSPI(p_potSelect, message)

def binaryToDecimal(message):
    number = 0
    for ii in range(len(message)):
        number += message[len(message)-1-ii]*(2**ii)
    return number
from multiprocessing import Process, Queue
'''Q1 = Queue()
Q2 = Queue()
run(Q1, Q2)'''
