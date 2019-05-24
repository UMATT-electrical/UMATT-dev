import math

from PyQt4 import QtGui, QtCore
import compassWidget2 as CW
import barWidget as BW
import time
import os

from widgets import make_button, make_compass_widget, make_label, LabelWithImage, make_pixmap

captureTime = 1
mode = 0


class HomeWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        from constants import SCREEN, HEIGHT, WIDTH, RGBStrings
        # initialize basic window function
        super(HomeWindow, self).__init__()

        self.ScreenTimer = time.time()

        self.make_button = lambda *args, **kwargs: make_button(self, *args, **kwargs)
        self.make_label = lambda *args, **kwargs: make_label(self, *args, **kwargs)

        self.grid = QtGui.QGridLayout(self)

        self.grid.setSpacing(0)

        # self.dial_gauge_engine_speed = make_compass_widget(
        #     'Engine',
        #     {0: '3', 45: '4', 90: '5', 135: '6', 225: '0', 270: '1', 315: '2'},
        #     (168, 168),
        #     225,
        #     'background-color: rgba(0,0,0,0%)')
        # self.grid.addWidget(self.dial_gauge_engine_speed, 1, 1, 2, 1)
        #
        # self.dialGauge_motorSpeed = CW.CompassWidget()
        # self.dialGauge_motorSpeed.setAngle(225)
        # self.dialGauge_motorSpeed.resize(168, 168)
        # self.dialGauge_motorSpeed._backText = 'Motor'
        # self.dialGauge_motorSpeed._pointText = {0: '3', 45: '4', 90: '5', 135: '6', 225: '0', 270: '1', 315: '2'}
        # # self.dialGauge_motorSpeed.move(67, 274)
        # self.grid.addWidget(self.dialGauge_motorSpeed, 4, 1, 2, 1)
        # self.dialGauge_motorSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        # # self.grid.addWidget(self.dialGauge_motorSpeed, 8,3,1,1)
        #
        # self.dialGauge_diffSpeed = CW.CompassWidget()
        # self.dialGauge_diffSpeed.setAngle(225)
        # self.dialGauge_diffSpeed.resize(300, 300)
        # self.dialGauge_diffSpeed._backImage = True
        # self.dialGauge_diffSpeed._pointText = {0: '9', 45: '12', 90: '15', 135: '18', 225: '0', 270: '3', 315: '6'}
        # # self.dialGauge_diffSpeed.move(267, 103)
        # self.grid.addWidget(self.dialGauge_diffSpeed, 2, 3, 3, 1)
        # self.dialGauge_diffSpeed.setStyleSheet('background-color: rgba(0,0,0,0%)')
        # # self.grid.addWidget(self.dialGauge_engineSpeed, 3, 8,2,2)

        '''pixmap = QtGui.QPixmap("UMATT_LOGO_BROWN.jpg")
        pixmap = pixmap.scaled(200,200)
        self.image_logo = QtGui.QLabel(self)
        self.image_logo.setPixmap(pixmap)
        #self.image_logo.move(567,167)
        self.grid.addWidget(self.image_logo, 2,3,3,1)'''

        rowHeights = (48, 47, 151, 18, 151, 17, 48)
        colWidths = (41, 168, 41, 300, 250)
        coordsTaken = ((1, 1), (2, 1), (4, 1), (5, 1), (2, 3), (3, 3), (4, 3))

        for rr in range(len(rowHeights)):
            for cc in range(len(colWidths)):
                if (rr, cc) not in coordsTaken:
                    layout = QtGui.QSpacerItem(colWidths[cc], rowHeights[rr])
                    self.grid.addItem(layout, rr, cc, 1, 1)

        self.setLayout(self.grid)

        currentTime = time.ctime().split()[3].split(':')
        time_label = ('%d:%s PM' % (int(currentTime[0]) - 12, currentTime[1]) if
                      int(currentTime[0]) > 12 else
                      '%d:%s AM' % (int(currentTime[0]), currentTime[1]))
        self.label_time = self.make_label(time_label, (167, 69), (0, 0), QtGui.QFont('Times', 14, QtGui.QFont.Bold))

        main_menu_item_size = (HEIGHT / 4 * 19) / 20

        self.label_gear = self.make_label(
            '',
            size=(main_menu_item_size, main_menu_item_size),
            position=(WIDTH - main_menu_item_size - HEIGHT/160, HEIGHT/160),
            font=QtGui.QFont('Times', 70, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.DARK_BROWN.background_string, RGBStrings.GOLD.colour_string)
        )

        self.button_difflock = self.make_button(
            'Diff Lock',
            size=(main_menu_item_size, main_menu_item_size),
            position=(WIDTH - main_menu_item_size - HEIGHT/160, main_menu_item_size + HEIGHT/80 + HEIGHT/160),
            font=QtGui.QFont('Times', 30, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.DARK_BROWN.background_string, RGBStrings.GOLD.colour_string)
        )

        self.button_mode = self.make_button(
            'Pull',
            size=(main_menu_item_size, main_menu_item_size),
            position=(WIDTH - main_menu_item_size - HEIGHT/160, 2*(main_menu_item_size + HEIGHT/80) + HEIGHT/160),
            font=QtGui.QFont('Times', 30, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.DARK_BROWN.background_string, RGBStrings.GOLD.colour_string)
        )

        self.button_menu = self.make_button(
            'Menu',
            size=(main_menu_item_size, main_menu_item_size),
            position=(WIDTH - main_menu_item_size - HEIGHT/160, 3*(main_menu_item_size + HEIGHT/80)  + HEIGHT/160),
            font=QtGui.QFont('Times', 30, QtGui.QFont.Bold),
            style_sheet='%s; %s'%(RGBStrings.DARK_BROWN.background_string, RGBStrings.GOLD.colour_string)
        )

        left_label_font = QtGui.QFont('Times', 30, QtGui.QFont.Bold)
        total_height = HEIGHT/6
        box_height = int(HEIGHT / 6 *.95)
        spacing = total_height - box_height
        left_label_size = (WIDTH / 4 - 10, box_height)
        left_label_positions = [
            (spacing, (idx * left_label_size[1]) + spacing * (idx + .5)) for idx in range(7)
        ]

        self.temperature_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[0],
            'temperature.png',
            '00.0 C',
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT/60
        )

        self.pressure_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[1],
            'pressure.png',
            '00.0 PSI',
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT/60
        )

        self.voltage_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[2],
            'voltage.png',
            '00.0 Volts',
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT/60
        )

        self.diff_rpm_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[3],
            'rpm.png',
            '0000 RPM',
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT/60
        )

        self.time_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[4],
            'time.png',
            '00:00 Hours',
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT / 60
        )

        self.clock_label = LabelWithImage(
            self,
            left_label_size,
            left_label_positions[5],
            'clock.png',
            time_label,
            RGBStrings.DARK_BROWN.background_string,
            left_label_font,
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT / 60
        )

        get_center_position = lambda width: int((WIDTH + left_label_size[0] + left_label_positions[0][0] - WIDTH/160 - main_menu_item_size - width)/2)

        self.label_title = self.make_label(
            'UMATT 2019',
            size=(WIDTH - 4 * main_menu_item_size, main_menu_item_size),
            position=(get_center_position(WIDTH - 4 * main_menu_item_size), HEIGHT/160),
            font=QtGui.QFont('Times', 60, QtGui.QFont.Bold),
            style_sheet='%s; %s' % (RGBStrings.TRANSPARENT.background_string, RGBStrings.BLACK.colour_string)
        )

        self.label_speed = LabelWithImage(
            self,
            (WIDTH - 4 * main_menu_item_size, main_menu_item_size),
            (get_center_position(WIDTH - 4 * main_menu_item_size), main_menu_item_size + HEIGHT/80 + HEIGHT/160),
            'tractorWireFrame.png',
            '00 KM/H',
            RGBStrings.DARK_BROWN.background_string,
            QtGui.QFont('Times', 30, QtGui.QFont.Bold),
            RGBStrings.TRANSPARENT.background_string,
            margin_width=HEIGHT/50
        )

        self.label_rpm = self.make_label(
            '0000 RPM',
            size=(main_menu_item_size * 3, main_menu_item_size),
            position=(get_center_position(main_menu_item_size * 3), 2*(main_menu_item_size + HEIGHT/80) + HEIGHT/160),
            font=QtGui.QFont('Times', 30, QtGui.QFont.Bold),
            style_sheet='%s; %s' % (RGBStrings.GOLD.background_string, RGBStrings.BLACK.colour_string)
        )

        self.label_logo = make_pixmap(
            self, 'wheat.png',
            size=(main_menu_item_size, main_menu_item_size),
            position=(get_center_position(main_menu_item_size)+WIDTH/160, 3*(main_menu_item_size + HEIGHT/80) + HEIGHT/160),
            scale_to_fit=False
        )

        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect(self.update)
        self.updateTimer.start(1)

    def update(self):
        # self.updateDiffDial()

        currentTime = time.ctime().split()[3].split(':')
        time_label = ('%d:%s PM' % (int(currentTime[0]) - 12, currentTime[1]) if
                      int(currentTime[0]) > 12 else
                      '%d:%s AM' % (int(currentTime[0]), currentTime[1]))

        self.temperature_label.text.setText('%s C' % self.parent().parent().value_engineTemperature)

        self.pressure_label.text.setText("%s PSI" % self.parent().parent().value_engineOilPressure)

        self.voltage_label.text.setText("%s Volts" % self.parent().parent().value_battery)

        # TODO Engine RPM
        self.diff_rpm_label.text.setText('%.2f RPM' % self.parent().parent().value_diffSpeed)

        runtime = self.parent().parent().runtime
        runtime_hours = int(math.floor(runtime/60))
        runtime_minutes = runtime % 60
        self.time_label.text.setText("%s:%s hours" % (runtime_hours, runtime_minutes))

        self.clock_label.text.setText(time_label)

        if self.parent().parent().warning_gearlockout[0] == 1:
            self.label_title.setText('Return Joystick to Neutral')
        elif self.parent().parent().warning_gearlockout[1] == 1:
            self.label_title.setText('Return Joystick to Neutral')
        else:
            self.label_title.setText('UMATT 2019')

        self.label_speed.text.setText("%s KM/H" % self.parent().parent().value_diffSpeed)

        self.label_gear.setText(self.parent().parent().currentGear.value)

    def diffLockToggle(self):
        self.ScreenTimer = time.time()

    def Timer1(self):
        # self.label2.setText('Voltage: %.2f V'%(self.parent().parent().value_battery/1023.*15.4))
        self.label2.setText('%d.2 V' % (self.parent().parent().value_battery / 1023. * 15.4))
        # self.label3.setText('%.2f RPM'%(self.parent().parent().value_engineSpeed/captureTime))
        self.label3.setText('%d Hz' % (self.parent().parent().value_engineSpeed / captureTime))
        self.label4.setText('%d Hz' % (self.parent().parent().value_wheelSpeed / captureTime / 2))
        self.label20.setText('IVT: %3d Hz' % (self.parent().parent().value_IVTSpeed / captureTime))
        try:
            self.label5.setText('%4.1f C' % ((3984. / (3984. / 298 - math.log(
                10.5 / 5.1 * (0.0001 + 1024. / self.parent().parent().value_temperature - 1))) - 273)))
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

            if self.parent().parent().output_headLightLState == 1:  # left
                if self.parent().parent().output_headlightLtemp == 0:
                    self.parent().parent().writeGPIO(p_peri2, 1)
                    self.parent().parent().output_headlightLtemp = 1
                else:
                    self.parent().parent().writeGPIO(p_peri2, 0)
                    self.parent().parent().output_headlightLtemp = 0

            if self.parent().parent().output_headLightRState == 1:  # right
                if self.parent().parent().output_headlightRtemp == 0:
                    self.parent().parent().writeGPIO(p_peri1, 1)
                    self.parent().parent().output_headlightRtemp = 1
                else:
                    self.parent().parent().writeGPIO(p_peri1, 0)
                    self.parent().parent().output_headlightRtemp = 0

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
