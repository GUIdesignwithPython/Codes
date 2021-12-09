# Darw Rectangles
# Section 7-3
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush,  QLinearGradient
from PyQt5.QtCore import Qt

class DrawRects(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,580,250)
                self.setWindowTitle('Drawing Rectangles')
                self.show()
        def paintEvent(self, event):
                painter=QPainter()
                painter.setRenderHint(QPainter.Antialiasing)
                painter.begin(self)
                pen=QPen(QColor('#000000'))
                painter.setPen(pen)
                painter.drawRect(20,20,100,100)
                pen.setWidth(4)
                painter.setPen(pen)
                painter.drawRect(130,20,100,100)
                brush=QBrush(QColor('#E00C0C'))
                pen.setStyle(Qt.DashDotLine)
                painter.setPen(pen)
                painter.setBrush(brush)
                painter.drawRect(240,20,100,100)
                brush.setStyle(Qt.CrossPattern)
                
                color=QColor(32,85,230,150)
                brush.setColor(color)
                brush.setStyle(Qt.SolidPattern)
                pen.setStyle(Qt.SolidLine)
                pen.setWidth(1)
                painter.setPen(pen)
                painter.setBrush(brush)
                painter.drawRect(350,20,100,100)


                pen.setColor(QColor('#000000'))
                painter.setPen(pen)
                gradient = QLinearGradient(460, 20, 560, 120)

                gradient.setColorAt(0.0, Qt.red)
                gradient.setColorAt(0.5, Qt.yellow)
                gradient.setColorAt(1.0, Qt.cyan)
                brush2=QBrush(gradient)
                painter.setBrush(brush2)
                painter.drawRect(460,20,100,100)

                pen=QPen(QColor('#000000'))
                painter.setPen(pen)
                painter.setBrush(QBrush())
                painter.drawRoundedRect(20,130,100,100,8,8)
                brush3 = QBrush(QColor('#000000'))

                brush3.setStyle(Qt.Dense1Pattern)
                painter.setBrush(brush3)

                painter.drawRoundedRect(130,130,100,100,8,8)

                brush3.setStyle(Qt.Dense3Pattern)
                painter.setBrush(brush3)

                painter.drawRoundedRect(240,130,100,100,8,8)
                
                brush3.setStyle(Qt.BDiagPattern)
                painter.setBrush(brush3)

                painter.drawRoundedRect(350,130,100,100,8,8)


                brush3.setStyle(Qt.CrossPattern)
                painter.setBrush(brush3)

                painter.drawRoundedRect(460,130,100,100,8,8)

                painter.end()                

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=DrawRects()
        sys.exit(app.exec_())
   

    

