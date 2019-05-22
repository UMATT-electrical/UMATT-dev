import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import math

size = 120.0

class CompassWidget(QWidget):
    
    angleChanged = pyqtSignal(float)

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        self._angle = 0.0
        self._margins = 10
        self._pointText = {0:'90', 45:'120', 90:'150', 135:'180', 225:'0', 270:'30', 315:'60'}
        self._backText = ''
        self._backImage = False

    def paintEvent(self, event):

        font = QFont(self.font())
        font.setPixelSize(10)
        metrics = QFontMetricsF(font)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(event.rect(), self.palette().brush(QPalette.Window))
        if self._backImage == True:
            image = QImage("UMATT_LOGO_BROWN.jpg")
            factor = 0.6
            target = QRectF((self.width())*(1-factor)/2.,self.height()*(1-factor)/2.,self.width()*factor,self.height()*factor)
            source = QRectF(0,0,image.width(),image.height())
            painter.drawImage(target, image, source)
        painter.drawText((self.width() - metrics.width(self._backText))/2,self.height()/2.4 - metrics.height()/2, self._backText)
        self.drawMarkings(painter)
        self.drawNeedle(painter)

        painter.end()

    def drawMarkings(self, painter):

        painter.save()
        painter.translate(self.width()/2, self.height()/2)
        scale = min((self.width() - self._margins)/size, (self.height() - self._margins)/size)
        painter.scale(scale, scale)

        font = QFont(self.font())
        font.setPixelSize(10)
        metrics = QFontMetricsF(font)

        painter.setFont(font)
        painter.setPen(self.palette().color(QPalette.Shadow))

        i = 0
        while i < 359:
            painter.setPen(QColor('black'))
            painter.setBrush(QColor('black'))
            if not(224 > i > 136):
                if (i % 15 == 0):
                    if i % 45 == 0:
                        painter.drawLine(0,-35, 0,-45)
                        painter.rotate(-i)
                        #painter.drawText(-metrics.width(self._pointText[i])/2.0, -54, self._pointText[i])
                        painter.drawText(-(57)*math.cos((i+90)*math.pi/180.)-metrics.width(self._pointText[i])/2.0, -(57)*math.sin((i+90)*math.pi/180.)+metrics.height()/2.0, self._pointText[i])
                        painter.rotate(i)
                    else:
                        painter.drawLine(0, -45, 0, -40)
                painter.drawPolygon(QPolygon([QPoint(0, -45), QPoint(-1, -45), QPoint(-1, -47), QPoint(0, -47), QPoint(0, -45)]))

            painter.rotate(1)
            i += 1
            #painter.drawPolygon(QPolygon([QPoint(0, 3), QPoint(-1, 3), QPoint(-1, -10), QPoint(0, -10), QPoint(0, 3)]))
            painter.setBrush(QColor('red'))
            painter.setPen(QColor('red'))
            painter.drawPolygon(QPolygon([QPoint(0, 0), QPoint(0, 0), QPoint(0, -3), QPoint(0, -3), QPoint(0, 0)]))
            
            

            '''painter.drawLine(0, -50, -1, -50)
            painter.drawLine(0, -51, -1, -51)
            painter.drawLine(0, -52, -1, -52)'''

        painter.restore()

    def drawNeedle(self, painter):

        painter.save()
        painter.translate(self.width()/2., self.height()/2.)
        painter.rotate(self._angle)
        scale = min((self.width() - self._margins)/size, (self.height() - self._margins)/size)
        painter.scale(scale, scale)

        painter.setPen(QColor('red'))#QPen(Qt.NoPen))
        #painter.setBrush(self.palette().brush(QPalette.Shadow))
        painter.setBrush(QColor('red'))
        #painter.drawPolygon(QPolygon([QPoint(-5, -25), QPoint(0, -45), QPoint(5, -25), QPoint(0, -30), QPoint(-5, -25)]))
        painter.drawPolygon(QPolygon([QPoint(-3, 0), QPoint(0, -50), QPoint(3, 0), QPoint(-3, 0)]))

        painter.restore()

    def sizeHint(self):

        return QSize(150, 150)

    def angle(self):

        return self._angle

    @pyqtSlot(float)
    def setAngle(self, angle):

        if angle != self._angle:
            self._angle = angle
            self.angleChanged.emit(angle)
            self.update()

    angle = pyqtProperty(float, angle, setAngle)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    compass = CompassWidget()
    spinBox = QSpinBox()
    spinBox.setRange(0,359)
    spinBox.valueChanged.connect(compass.setAngle)

    layout = QVBoxLayout()
    layout.addWidget(compass)
    layout.addWidget(spinBox)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())
