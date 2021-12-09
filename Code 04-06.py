# Event Handling
# Section 4-9
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class EventHandling(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,150,150)
                self.setWindowTitle('Event Handling')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.btn2=QPushButton(self)
                self.btn2.setText('Close')
                self.btn2.move(50,80)
                self.btn2.resize(80,25)
                self.btn2.clicked.connect(self.btn_click)

        def btn_click(self):
                self.close()


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=EventHandling()
        sys.exit(app.exec_())
   

    

