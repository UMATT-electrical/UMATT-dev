from PyQt4 import QtGui, QtCore
import compassWidget2 as CW
import barWidget as BW
import time
import os

captureTime = 1

class DiagnosticsWindow(QtGui.QWidget):
    
    def __init__(self, parent = None):
        # initialize basic window function
        super(DiagnosticsWindow, self).__init__()

        self.initUI()


    def initUI(self):

        currentTime = time.ctime().split()[3].split(':')
        if int(currentTime[0])>12:
            self.label_time = QtGui.QLabel('%d:%s PM'%(int(currentTime[0])-12,currentTime[1]), self)
        else:
            self.label_time = QtGui.QLabel('%d:%s AM'%(int(currentTime[0]),currentTime[1]), self)
        self.label_time.setFont(QtGui.QFont('Times',20,QtGui.QFont.Bold))
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.resize(167, 69)
        self.label_time.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.move(0,0)

        self.button_home = QtGui.QPushButton('Home', self)
        self.button_home.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.button_home.setFont((QtGui.QFont('Times',20,QtGui.QFont.Bold)))
        self.button_home.resize(200,69)
        self.button_home.move(600, 411)

        self.button_menu = QtGui.QPushButton('Menu', self)
        self.button_menu.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.button_menu.setFont((QtGui.QFont('Times',20,QtGui.QFont.Bold)))
        self.button_menu.resize(200,69)
        self.button_menu.move(0, 411)

        self.label_throttle = QtGui.QLabel('Throttle: ', self)
        self.label_throttle.setFont(QtGui.QFont('Times',14,QtGui.QFont.Bold))
        #self.label_engineSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_throttle.resize(200, 69)
        self.label_throttle.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_throttle.move(10, 80)

        self.label_brake = QtGui.QLabel('Transmission Brake: ', self)
        self.label_brake.setFont(QtGui.QFont('Times',14,QtGui.QFont.Bold))
        #self.label_engineSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brake.resize(200, 69)
        self.label_brake.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_brake.move(10, 110)

        self.label_clutch = QtGui.QLabel('Clutch: ', self)
        self.label_clutch.setFont(QtGui.QFont('Times',14,QtGui.QFont.Bold))
        #self.label_engineSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clutch.resize(200, 69)
        self.label_clutch.setStyleSheet('background-color: rgba(0,0,0,0%)')
        self.label_clutch.move(10, 140)

        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.update)
        self.updateTimer.start(10)

    def pressed_quit(self):
        QtGui.qApp.quit()

    def update(self):
        if self.parent().parent().output_brake == 1:
            self.label_brake.setText('Transmission Brake: ON')
        else:
            self.label_brake.setText('Transmission Brake: OFF')

        if self.parent().parent().output_clutch == 1:
            self.label_clutch.setText('Clutch: ON')
        else:
            self.label_clutch.setText('Clutch: OFF')

        self.label_throttle.setText('Throttle: %.2f%%'%(self.parent().parent().sevcon_Throttle*100))

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


    def pressed_menu(self):
        self.parent().parent().value_diffSpeed += 4
        if self.parent().parent().value_diffSpeed >= 20:
            QtGui.qApp.quit()
        pass

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
