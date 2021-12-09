# Darw Other Objects
# Section 7-5
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QPolygon, QFont, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRectF

class DrawObjects(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,400,270)
                self.setWindowTitle('Drawing Other Objects')
                self.show()
        def paintEvent(self, event):
                painter=QPainter()
                painter.setRenderHint(QPainter.Antialiasing)
                painter.begin(self)
                pen = QPen(QColor(Qt.black),2)
                painter.setPen(pen)
                painter.drawPolygon(QPoint(50,10),QPoint(10,85),QPoint(90,85))
                text='This is a sample text drawing!'
                painter.setFont(QFont('Helvetica', 10))
                painter.drawText(100, 50, text)                

                rectangle=QRectF(10,100,80,190)
                painter.drawArc(rectangle,30*16,120*16)
                rectangle=QRectF(90,100,80,190)
                painter.drawPie(rectangle,30*16,120*16)
                rectangle=QRectF(170,100,80,190)
                painter.drawChord(rectangle,30*16,120*16)
                
                points = QPolygon([QPoint(140, 220), QPoint(280, 230), QPoint(130, 360), QPoint(270, 340)])
                painter.drawPolygon(points)

                points = QPolygon([QPoint(10, 250), QPoint(20, 180), QPoint(80, 210), QPoint(90, 250)])
                painter.drawConvexPolygon(points)                

                painter.drawPixmap(10,275,QPixmap('python2.png'))
                
                painter.end()                

if __name__=='__main__':
        app=QApplication(sys.argv)
        window= DrawObjects()
        sys.exit(app.exec_())
   

    

