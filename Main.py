#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)

from constants import Gear

from multiprocessing import Process, Queue
# import SPImodule_002 as SPI
# import compassWidget as CW
import time
from subprocess import call
import os
import Drive

import Home as HomeWindow
import Menu as MenuWindow
import Settings as SettingsWindow
import Diagnostics as DiagnosticsWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        from constants import Gear

        super(MainWindow, self).__init__(parent)

        # INITIALIZE VARIABLES
        self.value_battery = 0
        self.value_engineSpeed = 0
        self.value_diffSpeed = 0
        self.value_motorSpeed = 0
        self.value_temperature = 0
        self.value_diffLock = 0
        self.value_airShockPressure = 0
        self.value_exhaustTemperature = 0
        self.value_engineOilPressure = 0
        self.value_engineTemperature = 0
        self.value_interlockBrake1 = 0
        self.value_interlockBrake2 = 0
        self.value_interlockSeat = 0
        self.value_maxSpeed = 0
        self.value_accessoryPower = 0
        self.value_joystick = 0.

        self.value_gearForwards = 0
        self.value_gearReverse = 0
        self.value_gearNeutral = 1
        self.value_modeManeuverability = 1
        self.value_modePull = 0

        self.last_diffSpeed = 0
        self.last_engineSpeed = 0
        self.last_motorSpeed = 0

        self.output_clutch = 0
        self.output_brake = 0
        self.output_fans = 0
        self.output_pump = 0
        self.output_interlock = 0
        self.output_powerOff = 0
        self.output_LAExtend = 0
        self.output_LARetract = 0

        self.sevcon_Throttle = 0
        self.sevcon_Forwards = 0
        self.sevcon_Reverse = 0
        self.sevcon_MotorEnable = 0
        self.sevcon_MotorBrake = 0
        self.sevcon_AltProfile = 0
        self.warning_gearlockout = [0, 0]

        self.currentGear = Gear.NEUTRAL

        self.initDrive()

        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.homeWindowWidget = HomeWindow.HomeWindow(self)
        self.central_widget.addWidget(self.homeWindowWidget)

        self.menuWindowWidget = MenuWindow.MenuWindow(self)
        self.central_widget.addWidget(self.menuWindowWidget)

        self.settingsWindowWidget = SettingsWindow.SettingsWindow(self)
        self.central_widget.addWidget(self.settingsWindowWidget)

        self.diagnosticsWindowWidget = DiagnosticsWindow.DiagnosticsWindow(self)
        self.central_widget.addWidget(self.diagnosticsWindowWidget)

        self.homeWindowWidget.button_menu.clicked.connect(self.gotoMenu)

        self.menuWindowWidget.button_home.clicked.connect(self.gotoHome)
        self.menuWindowWidget.button_settings.clicked.connect(self.gotoSettings)
        self.menuWindowWidget.button_diagnostics.clicked.connect(self.gotoDiagnostics)
        self.menuWindowWidget.button_quit.clicked.connect(self.quitProgram)

        self.settingsWindowWidget.button_menu.clicked.connect(self.gotoMenu)
        self.settingsWindowWidget.button_home.clicked.connect(self.gotoHome)
        self.settingsWindowWidget.button_modeManeuver.clicked.connect(self.setModeManeuver)
        self.settingsWindowWidget.button_modePull.clicked.connect(self.setModePulling)
        self.homeWindowWidget.button_mode.clicked.connect(self.button_wrapper(self.homeWindowWidget.button_mode, self.set_mode))

        self.diagnosticsWindowWidget.button_home.clicked.connect(self.gotoHome)
        self.diagnosticsWindowWidget.button_menu.clicked.connect(self.gotoMenu)
        self.central_widget.setCurrentWidget(self.homeWindowWidget)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Update)
        self.timer.start(100)

        self.setStyleSheet("background-color: white")
        # self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.showFullScreen()

    def Update(self):
        leave = 0
        while (not self.Quido.empty()) and (leave == 0):
            try:
                data = self.Quido.get(False)
            except:
                data = None
                leave = 1
            if data:
                self.output_brake = data[0]
                self.output_clutch = data[1]
                self.sevcon_Throttle = data[2]
                self.sevcon_MotorEnable = data[3]
                self.sevcon_Forwards = data[4]
                self.sevcon_Reverse = data[5]

                self.warning_gearlockout = data[7]
                self.output_fans = data[8]
                self.output_pump = data[9]
                self.output_LAExtend = data[10]
                self.output_LARetract = data[11]
                self.value_modeManeuverability = data[13]
                self.value_modePull = data[14]
                self.value_diffSpeed = data[15]
                self.value_accessoryPower = data[16]

                if self.sevcon_Forwards == 1:
                    self.currentGear = Gear.FORWARD
                elif self.sevcon_Reverse == 1:
                    self.currentGear = Gear.REVERSE
                else:
                    self.currentGear = Gear.NEUTRAL

    def gotoMenu(self):
        self.central_widget.setCurrentWidget(self.menuWindowWidget)

    def gotoHome(self):
        self.central_widget.setCurrentWidget(self.homeWindowWidget)

    def gotoSettings(self):
        self.central_widget.setCurrentWidget(self.settingsWindowWidget)

    def gotoDiagnostics(self):
        self.central_widget.setCurrentWidget(self.diagnosticsWindowWidget)

    def setModeManeuver(self):
        if self.currentGear == Gear.NEUTRAL:
            self.Quodi.put((1, 1))

    def setModePulling(self):
        if self.currentGear == Gear.NEUTRAL:
            self.Quodi.put((2, 1))

    def quitProgram(self):
        QtGui.qApp.quit()
        print('TRY')
        if self.currentGear == Gear.NEUTRAL:
            if self.value_accessoryPower == 0:
                print('PWR Down')
                self.Quodi.put((100, 1))

    def initDrive(self):
        self.Quido = Queue()
        self.Quodi = Queue()
        proc = Process(target=Drive.run, args=(self.Quodi, self.Quido))
        proc.start()

    def set_mode(self, button):
        from constants import Mode
        from Home import mode
        mode += 1
        mode %= 3
        button.setText("value")

    @staticmethod
    def button_wrapper(button, func):
        return lambda: func(button)





def binaryToDecimal(message):
    number = 0
    for ii in range(len(message)):
        number += message[len(message) - 1 - ii] * (2 ** ii)
    return number


def int2Bin(integer):
    binaryText = bin(integer)[2:]
    binary = []
    for ii in range(8 - len(binaryText)):
        binary.append(0)
    for ii in range(len(binaryText)):
        binary.append(int(binaryText[ii]))
    return binary


def main():

    w = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    time.sleep(5)
    main()
