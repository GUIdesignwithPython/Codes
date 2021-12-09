# Box Layout
# Section 3-6
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QBoxLayout

class BoxLayout(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,0,0)
                self.setWindowTitle('Box Layout')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                button1 = QPushButton('One')
                button2 = QPushButton('Two')
                button3 = QPushButton('Three')
                button4 = QPushButton('Four')

                layout = QBoxLayout(QBoxLayout.RightToLeft)
                #layout.setDirection(QBoxLayout.RightToLeft)
                layout.addWidget(button1)
                layout.addWidget(button2)
                layout.addWidget(button3)
                layout.addWidget(button4)


                self.setLayout(layout)
                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=BoxLayout()
        sys.exit(app.exec_())
   

    

