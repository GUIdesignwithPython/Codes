# Darw Points and Lines
# Section 7-2
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class DrawPointandLine(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,600,200)
                self.setWindowTitle('Drawing Points and Lines')
                self.show()
        def paintEvent(self, event):
                painter=QPainter()
                painter.setRenderHint(QPainter.Antialiasing)
                painter.begin(self)
                pen=QPen(QColor('#000000'))
                for i in range(1,9):
                        pen.setWidth(i*2)
                        painter.setPen(pen)
                        painter.drawPoint(i*20, i*20)

                pen2 = QPen(QColor('#000000'), 2)
                painter.setPen(pen2)
                painter.drawLine(230, 20, 230, 180)
                pen2.setStyle(Qt.DashLine)
                painter.setPen(pen2)
                painter.drawLine(260, 20, 260, 180)
                pen2.setStyle(Qt.DotLine)
                painter.setPen(pen2)
                painter.drawLine(290, 20, 290, 180)
                pen2.setStyle(Qt.DashDotLine)
                painter.setPen(pen2)
                painter.drawLine(320, 20, 320, 180)
                red_pen = QPen(QColor('#E00C0C'), 6)
                painter.setPen(red_pen)
                painter.drawLine(350, 20, 350, 180)
                red_pen.setStyle(Qt.DashDotDotLine)
                painter.setPen(red_pen)
                painter.drawLine(380, 20, 380, 180)

                pen3=QPen(QColor('#000000'))
                pen3.setCapStyle(Qt.RoundCap)
                for i in range(1,9):
                        pen3.setWidth((10-i)*2)
                        painter.setPen(pen3)
                        painter.drawPoint(420+(i*20), (9-i)*20)
                
                painter.end()
                

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=DrawPointandLine()
        sys.exit(app.exec_())
   

    

