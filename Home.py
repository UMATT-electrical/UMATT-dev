from PyQt4 import QtGui, QtCore
import compassWidget2 as CW
import barWidget as BW
import time
import os

from widgets import make_button

captureTime = 1

class HomeWindow(QtGui.QWidget):
    
    def __init__(self, parent = None):
        # initialize basic window function
        super(HomeWindow, self).__init__()

        self.ScreenTimer = time.time()
        
        self.initUI()


    def initUI(self):

        self.grid = QtGui.QGridLayout(self)

        self.grid.setSpacing(0)

        self.dialGauge_engineSpeed = CW.CompassWidget()
        self.dialGauge_engineSpeed.setAngle(225)
        self.dialGauge_engineSpeed.resize(168,168)
        self.dialGauge_engineSpeed._backText = 'Engine'
        self.dialGauge_engineSpeed._pointText = {0:'3', 45:'4', 90:'5', 135:'6', 225:'0', 270:'1', 315:'2'}
        #self.dialGauge_engineSpeed.move(67, 103)
        self.dialGauge_engineSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.grid.addWidget(self.dialGauge_engineSpeed, 1, 1,2,1)
        #self.grid.addWidget(self.dialGauge_engineSpeed, 4, 3,1,1)

        self.dialGauge_motorSpeed = CW.CompassWidget()
        self.dialGauge_motorSpeed.setAngle(225)
        self.dialGauge_motorSpeed.resize(168,168)
        self.dialGauge_motorSpeed._backText = 'Motor'
        self.dialGauge_motorSpeed._pointText = {0:'3', 45:'4', 90:'5', 135:'6', 225:'0', 270:'1', 315:'2'}
        #self.dialGauge_motorSpeed.move(67, 274)
        self.grid.addWidget(self.dialGauge_motorSpeed, 4,1,2,1)
        self.dialGauge_motorSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        #self.grid.addWidget(self.dialGauge_motorSpeed, 8,3,1,1)

        self.dialGauge_diffSpeed = CW.CompassWidget()
        self.dialGauge_diffSpeed.setAngle(225)
        self.dialGauge_diffSpeed.resize(300,300)
        self.dialGauge_diffSpeed._backImage = True
        self.dialGauge_diffSpeed._pointText = {0:'9', 45:'12', 90:'15', 135:'18', 225:'0', 270:'3', 315:'6'}
        #self.dialGauge_diffSpeed.move(267, 103)
        self.grid.addWidget(self.dialGauge_diffSpeed, 2, 3, 3,1)
        self.dialGauge_diffSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        #self.grid.addWidget(self.dialGauge_engineSpeed, 3, 8,2,2)

        '''pixmap = QtGui.QPixmap("UMATT_LOGO_BROWN.jpg")
        pixmap = pixmap.scaled(200,200)
        self.image_logo = QtGui.QLabel(self)
        self.image_logo.setPixmap(pixmap)
        #self.image_logo.move(567,167)
        self.grid.addWidget(self.image_logo, 2,3,3,1)'''

        rowHeights = (48,47,151,18,151,17,48)
        colWidths = (41,168,41,300,250)
        coordsTaken = ((1,1),(2,1),(4,1),(5,1),(2,3),(3,3),(4,3))

        for rr in range(len(rowHeights)):
            for cc in range(len(colWidths)):
                if (rr,cc) not in coordsTaken:
                    layout = QtGui.QSpacerItem(colWidths[cc], rowHeights[rr])
                    self.grid.addItem(layout, rr, cc, 1,1)              
        
        self.setLayout(self.grid)

        self.label_gear = QtGui.QLabel('', self)
        self.label_gear.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.label_gear.setFont(QtGui.QFont('Times',90,QtGui.QFont.Bold))
        self.label_gear.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gear.resize(133,133)
        self.label_gear.move(667,0)
        #self.grid.addWidget(self.label_gear, 0,9,3,2)

        font = QtGui.QFont('Times', 20, QtGui.QFont.Bold)

        self.button_menu = make_button(
            'Menu', self, font, (200, 69), (600, 411))
        #self.grid.addWidget(self.button_menu, 8,8,1,3)

        self.button_difflock = make_button(
            'Diff Lock', self, font, (200, 69), (600, 242))


        self.label_message = QtGui.QLabel('Engine Not On', self)
        self.label_message.setFont(QtGui.QFont('Times',14,QtGui.QFont.Bold))
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.resize(333, 69)
        self.label_message.move(233, 0)
        #self.grid.addWidget(self.label_message, 0,4,1,3)

        self.label_mode = QtGui.QLabel('', self)
        self.label_mode.setFont(QtGui.QFont('Times',14,QtGui.QFont.Bold))
        self.label_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mode.resize(267, 69)
        self.label_mode.move(267, 411)
        #self.grid.addWidget(self.label_mode, 8,5,1,1)      

        currentTime = time.ctime().split()[3].split(':')
        if int(currentTime[0])>12:
            self.label_time = QtGui.QLabel('%d:%s PM'%(int(currentTime[0])-12,currentTime[1]), self)
        else:
            self.label_time = QtGui.QLabel('%d:%s AM'%(int(currentTime[0]),currentTime[1]), self)

        self.label_time.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.label_time.setFont(QtGui.QFont('Times',20,QtGui.QFont.Bold))
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.resize(167, 69)
        #self.label_time.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.move(0,0)
        #self.grid.addWidget(self.label_message, 0,4,1,3)

        self.label_diffSpeed = QtGui.QLabel('0 MPH', self)
        self.label_diffSpeed.setFont(QtGui.QFont('Times',14))#,QtGui.QFont.Bold))
        self.label_diffSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_diffSpeed.resize(100, 69)    
        self.label_diffSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_diffSpeed.move(360, 330)

        self.label_engineSpeed = QtGui.QLabel('0 RPM', self)
        self.label_engineSpeed.setFont(QtGui.QFont('Times',14))#,QtGui.QFont.Bold))
        self.label_engineSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_engineSpeed.resize(100, 69)
        self.label_engineSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_engineSpeed.move(85, 185)

        self.label_motorSpeed = QtGui.QLabel('0 RPM', self)
        self.label_motorSpeed.setFont(QtGui.QFont('Times',14))#,QtGui.QFont.Bold))
        self.label_motorSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_motorSpeed.resize(100, 69)
        self.label_motorSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_motorSpeed.move(85, 400)

        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.update)
        self.updateTimer.start(10)

    def update(self):
        self.updateDiffDial()
        self.label_diffSpeed.setText('%.2f MPH'% self.parent().parent().value_diffSpeed)
        
        self.label_gear.setText(self.parent().parent().currentGear)
        '''
        currentTime = time.ctime().split()[3].split(':')
        if int(currentTime[0])>12:
            self.label_time.setText('%d:%s PM'%(int(currentTime[0])-12,currentTime[1]))
        else:
            self.label_time.setText('%d:%s AM'%(int(currentTime[0]),currentTime[1]))'''
        

        if self.parent().parent().value_modeManeuverability == 1:
            self.label_mode.setText('Mode: Maneuverability')
        elif self.parent().parent().value_modePull == 1:
            self.label_mode.setText('Mode: Pulling')
        else:
            self.label_mode.setText('Error: Unknown Mode')

        if self.parent().parent().warning_gearlockout[0] == 1:
            self.label_message.setText('Return Joystick to Neutral')
        elif self.parent().parent().warning_gearlockout[1] == 1:
            self.label_message.setText('Return Joystick to Neutral')
        else:
            self.label_message.setText('UMATT Pullers')

        
    def diffLockToggle(self):
        self.ScreenTimer = time.time()

            
    def Timer1(self):
        #self.label2.setText('Voltage: %.2f V'%(self.parent().parent().value_battery/1023.*15.4))
        self.label2.setText('%d.2 V'%(self.parent().parent().value_battery/1023.*15.4))
        #self.label3.setText('%.2f RPM'%(self.parent().parent().value_engineSpeed/captureTime))
        self.label3.setText('%d Hz'%(self.parent().parent().value_engineSpeed/captureTime))
        self.label4.setText('%d Hz'%(self.parent().parent().value_wheelSpeed/captureTime/2))
        self.label20.setText('IVT: %3d Hz'%(self.parent().parent().value_IVTSpeed/captureTime))
        try:
            self.label5.setText('%4.1f C'%((3984./(3984./298 - math.log(10.5/5.1*(0.0001+1024./self.parent().parent().value_temperature - 1)))-273)))
        except (ValueError, ZeroDivisionError):
            pass

    def getCurrentGear(self):
        return self.parent().parent().currentGear

    def Timer4(self):

        if self.parent().parent().output_hazardState == 1:
            if self.parent().parent().output_hazardStatetemp == 0:
                self.parent().parent().writeGPIO(p_peri1, 1)
                self.parent().parent().writeGPIO(p_peri2, 1)
                self.parent().parent().writeGPIO(p_peri3, 1)
                self.parent().parent().output_hazardStatetemp = 1
            else:
                self.parent().parent().writeGPIO(p_peri1, 0)
                self.parent().parent().writeGPIO(p_peri2, 0)
                self.parent().parent().writeGPIO(p_peri3, 0)
                self.parent().parent().output_hazardStatetemp = 0

        else:

            if self.parent().parent().output_headLightState == 1:
                    self.parent().parent().writeGPIO(p_peri1, 1)
                    self.parent().parent().writeGPIO(p_peri2, 1)

            
            
            if self.parent().parent().output_headLightLState == 1: #left
                if self.parent().parent().output_headlightLtemp == 0:
                    self.parent().parent().writeGPIO(p_peri2, 1)
                    self.parent().parent().output_headlightLtemp = 1
                else:
                    self.parent().parent().writeGPIO(p_peri2, 0)
                    self.parent().parent().output_headlightLtemp = 0

            if self.parent().parent().output_headLightRState == 1: #right
                if self.parent().parent().output_headlightRtemp == 0:
                    self.parent().parent().writeGPIO(p_peri1, 1)
                    self.parent().parent().output_headlightRtemp = 1
                else:
                    self.parent().parent().writeGPIO(p_peri1, 0)
                    self.parent().parent().output_headlightRtemp = 0

    def buttonPressed6(self):
        self.parent().parent().writeSPI((0,1,1,1,0,1,1,1),(0,0,0,0,1,0,1,0)) #0x77
        #0x10
        pass

    def buttonPressed7(self): #toggle brake
        if self.parent().parent().output_brakeState == 0:
            self.parent().parent().writeGPIO(p_peri3, 1)
            self.parent().parent().output_brakeState = 1
        else:
            self.parent().parent().writeGPIO(p_peri3, 0)
            self.parent().parent().output_brakeState = 0
        pass

    def buttonPressed10(self): #toggle left headlight
        if self.parent().parent().output_headLightLState == 0:
            self.parent().parent().output_headLightLState = 1
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().output_headLightRState = 0
        else:
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().output_headLightLState = 0

    def buttonPressed11(self): #toggle right headlight
        if self.parent().parent().output_headLightRState == 0:
            self.parent().parent().output_headLightRState = 1
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().output_headLightLState = 0
        else:
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().output_headLightRState = 0

    def buttonPressed12(self): #toggle headlights
        if self.parent().parent().output_headLightState == 0:
            self.parent().parent().output_headLightState = 1
        else:
            self.parent().parent().output_headLightState = 0
            self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().writeGPIO(p_peri2, 0)

    def buttonPressed13(self): #hazards
        if self.parent().parent().output_hazardState == 0:
            self.parent().parent().output_hazardState= 1
        else:
            self.parent().parent().output_hazardState = 0
            self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().writeGPIO(p_peri3, 0)
            

    def updateDiffDial(self):
        difference = self.parent().parent().value_diffSpeed/captureTime - self.parent().parent().last_diffSpeed
        if difference != 0:
            if difference > 0:
                self.parent().parent().last_diffSpeed += min(1,difference)
            else:
                self.parent().parent().last_diffSpeed += max(-1,difference)
            self.dialGauge_diffSpeed.setAngle(225+min(self.parent().parent().last_diffSpeed,18)*15)

    def updateEngineSpeedGauge(self):
        difference = self.parent().parent().value_engineSpeed/captureTime - self.parent().parent().lastEngineSpeed
        if difference != 0:
            if difference > 0:
                self.parent().parent().lastEngineSpeed += min(100,difference)
            else:
                self.parent().parent().lastEngineSpeed += max(-100,difference)
            self.engineSpeedGauge.setAngle(225+min(self.parent().parent().lastEngineSpeed,180)*9/4.)

    def updateTempGauge(self):
        try:
            self.bar.setValue((3984./(3984./298 - math.log(10.5/5.1*(0.0001+1024./self.parent().parent().value_temperature - 1)))-273))
        except (ValueError, ZeroDivisionError):
            pass
