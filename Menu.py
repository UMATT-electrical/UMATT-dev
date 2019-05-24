from PyQt4 import QtGui, QtCore
import compassWidget2 as CW
import barWidget as BW
import time
from widgets import make_button, make_label
import os

captureTime = 1


class MenuWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        # initialize basic window function
        super(MenuWindow, self).__init__()
        from constants import SCREEN, HEIGHT, WIDTH, RGBStrings

        '''pixmap = QtGui.QPixmap("UMATT_LOGO_BROWN.jpg")
        pixmap = pixmap.scaled(260,260)
        self.image_logo = QtGui.QLabel(self)
        self.image_logo.setPixmap(pixmap)
        self.image_logo.move(10,110)'''

        self.make_button = lambda *args, **kwargs: make_button(self, *args, **kwargs)
        self.make_label = lambda *args, **kwargs: make_label(self, *args, **kwargs)

        # pixmap2 = QtGui.QPixmap("Full Tractor.PNG")
        # pixmap2 = pixmap2.scaled(500, 300)
        # self.image_logo2 = QtGui.QLabel(self)
        # self.image_logo2.setPixmap(pixmap2)
        # self.image_logo2.move(300, 90)

        # currentTime = time.ctime().split()[3].split(':')
        # time_label = ('%d:%s PM' % (int(currentTime[0]) - 12, currentTime[1]) if
        #               int(currentTime[0]) > 12 else
        #               '%d:%s AM' % (int(currentTime[0]), currentTime[1]))
        # self.label_time = self.make_label(time_label, (167, 69), (0, 0), QtGui.QFont('Times', 20, QtGui.QFont.Bold))
        # # self.grid.addWidget(self.label_message, 0,4,1,3)

        self.button_home = self.make_button('Home', size=(200, 69), position=(600, 411))

        self.button_quit = self.make_button('Quit', size=(60, 30), position=(740, 0))

        self.button_settings = self.make_button('Settings', size=(240, 69), position=(30, 120))

        main_menu_item_size = (HEIGHT / 4 * 19) / 20

        relative_width = 26*WIDTH / 30
        box_margin = WIDTH / 30
        relative_height = HEIGHT - 5 * box_margin;

        self.label_title = self.make_label(
            'MENU',
            size=(4 * relative_width / 10, main_menu_item_size),
            position=(4 * relative_width / 10 + 2*box_margin, HEIGHT/160),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.TRANSPARENT.background_string, RGBStrings.BLACK.colour_string)
        )

        self.diagnostics_box = self.make_label(
            '',
            size=(4*relative_width/10, HEIGHT - 2*box_margin),
            position=(box_margin, box_margin),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.DARK_BROWN.background_string, RGBStrings.BLACK.colour_string)
        )

        self.label_limit_box = self.make_label(
            '',
            size=(4 * relative_width / 10, HEIGHT - box_margin - main_menu_item_size),
            position=(4 * relative_width / 10 + 2*box_margin, main_menu_item_size),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.time_box = self.make_label(
            '',
            size=(2 * relative_width / 10, 2*relative_height/5),
            position=(8 * relative_width / 10 + 3*box_margin, box_margin),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.brightness_box = self.make_label(
            '',
            size=(2 * relative_width / 10, relative_height/5),
            position=(8 * relative_width / 10 + 3*box_margin, 2*box_margin + 2* relative_height / 5),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.logger_box = self.make_label(
            '',
            size=(2 * relative_width / 10, relative_height/5),
            position=(8 * relative_width / 10 + 3*box_margin, 3*box_margin + 3* relative_height / 5),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.label_logo = self.make_label(
            'wheat here',
            size=(relative_width / 10 - box_margin/2, relative_height/5),
            position=(8 * relative_width / 10 + 3*box_margin, 4*box_margin + 4* relative_height / 5),
            font=QtGui.QFont('Times', 14, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.button_home_unique = self.make_button(
            'home',
            size=(relative_width / 10 - box_margin/2, relative_height/5),
            position=(9 * relative_width / 10 + 7*box_margin/2, 4*box_margin + 4* relative_height / 5),
            font=QtGui.QFont('Times', 14, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )


        '''self.button_information = QtGui.QPushButton('Info', self)
        self.button_information.setStyleSheet('background-color: rgb(43,21,0); color: rgb(255,184,0)')
        self.button_information.setFont((QtGui.QFont('Times',20,QtGui.QFont.Bold)))
        self.button_information.resize(240,69)
        self.button_information.move(30, 240)'''

        self.button_diagnostics = self.make_button('Diagnostics', size=(240, 69), position=(30, 360))

        '''self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.updateDiffDial)
        self.updateTimer.start(10)'''

    def pressed_quit(self):
        '''if self.parent().parent().currentGear == 'N':
            if self.parent().parent().value_accessoryPower == 0:
                
        QtGui.qApp.quit()'''
        pass

    # def Timer1(self):
    #     # self.label2.setText('Voltage: %.2f V'%(self.parent().parent().value_battery/1023.*15.4))
    #     self.label2.setText('%d.2 V' % (self.parent().parent().value_battery / 1023. * 15.4))
    #     # self.label3.setText('%.2f RPM'%(self.parent().parent().value_engineSpeed/captureTime))
    #     self.label3.setText('%d Hz' % (self.parent().parent().value_engineSpeed / captureTime))
    #     self.label4.setText('%d Hz' % (self.parent().parent().value_wheelSpeed / captureTime / 2))
    #     self.label20.setText('IVT: %3d Hz' % (self.parent().parent().value_IVTSpeed / captureTime))
    #     try:
    #         self.label5.setText('%4.1f C' % ((3984. / (3984. / 298 - math.log(
    #             10.5 / 5.1 * (0.0001 + 1024. / self.parent().parent().value_temperature - 1))) - 273)))
    #     except (ValueError, ZeroDivisionError):
    #         pass

    # def Timer4(self):
    #
    #     if self.parent().parent().output_hazardState == 1:
    #         if self.parent().parent().output_hazardStatetemp == 0:
    #             self.parent().parent().writeGPIO(p_peri1, 1)
    #             self.parent().parent().writeGPIO(p_peri2, 1)
    #             self.parent().parent().writeGPIO(p_peri3, 1)
    #             self.parent().parent().output_hazardStatetemp = 1
    #         else:
    #             self.parent().parent().writeGPIO(p_peri1, 0)
    #             self.parent().parent().writeGPIO(p_peri2, 0)
    #             self.parent().parent().writeGPIO(p_peri3, 0)
    #             self.parent().parent().output_hazardStatetemp = 0
    #
    #     else:
    #
    #         if self.parent().parent().output_headLightState == 1:
    #             self.parent().parent().writeGPIO(p_peri1, 1)
    #             self.parent().parent().writeGPIO(p_peri2, 1)
    #
    #         if self.parent().parent().output_headLightLState == 1:  # left
    #             if self.parent().parent().output_headlightLtemp == 0:
    #                 self.parent().parent().writeGPIO(p_peri2, 1)
    #                 self.parent().parent().output_headlightLtemp = 1
    #             else:
    #                 self.parent().parent().writeGPIO(p_peri2, 0)
    #                 self.parent().parent().output_headlightLtemp = 0
    #
    #         if self.parent().parent().output_headLightRState == 1:  # right
    #             if self.parent().parent().output_headlightRtemp == 0:
    #                 self.parent().parent().writeGPIO(p_peri1, 1)
    #                 self.parent().parent().output_headlightRtemp = 1
    #             else:
    #                 self.parent().parent().writeGPIO(p_peri1, 0)
    #                 self.parent().parent().output_headlightRtemp = 0

    def pressed_menu(self):
        self.parent().parent().value_diffSpeed += 4
        if self.parent().parent().value_diffSpeed >= 20:
            QtGui.qApp.quit()
        pass

    def buttonPressed6(self):
        self.parent().parent().writeSPI((0, 1, 1, 1, 0, 1, 1, 1), (0, 0, 0, 0, 1, 0, 1, 0))  # 0x77
        # 0x10
        pass

    def buttonPressed7(self):  # toggle brake
        if self.parent().parent().output_brakeState == 0:
            self.parent().parent().writeGPIO(p_peri3, 1)
            self.parent().parent().output_brakeState = 1
        else:
            self.parent().parent().writeGPIO(p_peri3, 0)
            self.parent().parent().output_brakeState = 0
        pass

    def buttonPressed10(self):  # toggle left headlight
        if self.parent().parent().output_headLightLState == 0:
            self.parent().parent().output_headLightLState = 1
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().output_headLightRState = 0
        else:
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().output_headLightLState = 0

    def buttonPressed11(self):  # toggle right headlight
        if self.parent().parent().output_headLightRState == 0:
            self.parent().parent().output_headLightRState = 1
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().output_headLightLState = 0
        else:
            if self.parent().parent().output_headLightState == 0:
                self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().output_headLightRState = 0

    def buttonPressed12(self):  # toggle headlights
        if self.parent().parent().output_headLightState == 0:
            self.parent().parent().output_headLightState = 1
        else:
            self.parent().parent().output_headLightState = 0
            self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().writeGPIO(p_peri2, 0)

    def buttonPressed13(self):  # hazards
        if self.parent().parent().output_hazardState == 0:
            self.parent().parent().output_hazardState = 1
        else:
            self.parent().parent().output_hazardState = 0
            self.parent().parent().writeGPIO(p_peri1, 0)
            self.parent().parent().writeGPIO(p_peri2, 0)
            self.parent().parent().writeGPIO(p_peri3, 0)

    def updateDiffDial(self):
        difference = self.parent().parent().value_diffSpeed / captureTime - self.parent().parent().last_diffSpeed
        if difference != 0:
            if difference > 0:
                self.parent().parent().last_diffSpeed += min(1, difference)
            else:
                self.parent().parent().last_diffSpeed += max(-1, difference)
            self.dialGauge_diffSpeed.setAngle(225 + min(self.parent().parent().last_diffSpeed, 18) * 15)

    def updateEngineSpeedGauge(self):
        difference = self.parent().parent().value_engineSpeed / captureTime - self.parent().parent().lastEngineSpeed
        if difference != 0:
            if difference > 0:
                self.parent().parent().lastEngineSpeed += min(100, difference)
            else:
                self.parent().parent().lastEngineSpeed += max(-100, difference)
            self.engineSpeedGauge.setAngle(225 + min(self.parent().parent().lastEngineSpeed, 180) * 9 / 4.)

    def updateTempGauge(self):
        try:
            self.bar.setValue((3984. / (3984. / 298 - math.log(
                10.5 / 5.1 * (0.0001 + 1024. / self.parent().parent().value_temperature - 1))) - 273))
        except (ValueError, ZeroDivisionError):
            pass
