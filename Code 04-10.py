# Widgets Icons
# Section 4-10
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize



class WidgetIcon(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Widgets Icon')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                btn=QPushButton(self)
                btn.setText('Click')
                btn.setIcon(QIcon('python.png'))
                btn.setIconSize(QSize(30,30))
                btn.move(75,50)


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=WidgetIcon()
        sys.exit(app.exec_())
   

    

