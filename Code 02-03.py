# Window with Label and Button
# Section 2-4
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton

class LabelButtonWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        
        def initUI(self):
                self.setGeometry(200,250,350,150)
                self.setWindowTitle('Window with Label and Button')
                self.displayComponents()
                self.show()
        def displayComponents(self):
                lbl=QLabel(self)
                lbl.setText('Click the Button to Exit')
                lbl.move(125,30)

                button=QPushButton('Click Me!',self)
                button.clicked.connect(self.buttonClicked)
                button.setText('new')
                button.move(140,70)
                

        def buttonClicked(self):
                print('The Window has been Closed.')
                self.close()

#اجرای برنامه
if __name__=='__main__':
        app=QApplication(sys.argv)
        window= LabelButtonWindow()
        sys.exit(app.exec_())

   

    

