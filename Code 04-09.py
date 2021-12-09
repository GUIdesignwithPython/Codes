# Set Window Icon
# Section 4-10
import sys      
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon



class IconWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Window with a new Icon')
                self.setWindowIcon(QIcon('python.png'))
                self.show()

                


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=IconWindow()
        sys.exit(app.exec_())
   

    

