# Event Handling 2
# Section 4-9
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class EventHandling2(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,150,150)
                self.setWindowTitle('Event Handling 2')
                self.show()

        def keyPressEvent(self, event):
                if event.key()==Qt.Key_Escape:
                        self.close()


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=EventHandling2()
        sys.exit(app.exec_())
   

    

