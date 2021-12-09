# Pseudostates
# Section 4-6
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class PseudostateSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,150,150)
                self.setWindowTitle('Pseudo-state Sample')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.btn1=QPushButton(self)
                self.btn1.setText('Button 1')
                self.btn1.move(50,50)
                self.btn1.resize(80,25)

                self.btn2=QPushButton(self)
                self.btn2.setText('Button 2')
                self.btn2.move(50,80)
                self.btn2.resize(80,25)
                self.btn2.clicked.connect(self.button2)

        def button2(self):
                self.btn1.setEnabled(not self.btn1.isEnabled())


if __name__=='__main__':
        app=QApplication(sys.argv)
        style='QPushButton:disabled{color:red}'
        app.setStyleSheet(style)
        window=PseudostateSample()
        sys.exit(app.exec_())
   

    

