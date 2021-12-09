# Darw Circle and Curve
# Section 7-4
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QPainterPath
from PyQt5.QtCore import Qt, QPoint

class DrawCircleCurve(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,400,270)
                self.setWindowTitle('Drawing Circle and Curve')
                self.show()
        def paintEvent(self, event):
                painter=QPainter()
                painter.setRenderHint(QPainter.Antialiasing)
                painter.begin(self)
                point=QPoint(60,90)
                painter.drawEllipse(point,50,50)
                pen=QPen()
                pen.setWidth(3)
                painter.setPen(pen)
                point=QPoint(180,90)
                painter.drawEllipse(point,20,70)
                brush=QBrush(Qt.red, Qt.Dense5Pattern)
                painter.setBrush(brush)
                point=QPoint(300,90)
                painter.drawEllipse(point,70,20)


                pen = QPen(Qt.black, 3)
                brush = QBrush(Qt.green, Qt.CrossPattern)

                path = QPainterPath()
                path.moveTo(70, 160)
                path.cubicTo(70, 230, 110, 170, 160, 230)
                path.cubicTo(170, 230, 210, 280, 290, 230)
                path.lineTo(290,160)
                path.cubicTo(290, 160, 210, 220, 70, 160)
                path.closeSubpath()
                painter.setPen(pen)
                painter.setBrush(brush)
                painter.drawPath(path)
                
                painter.end()                

if __name__=='__main__':
        app=QApplication(sys.argv)
        window= DrawCircleCurve()
        sys.exit(app.exec_())
   

    

