# Window with two TABs
# Section 5-5
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTabWidget, QWidget,QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon

class TabWindow(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Window with two TABs')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.tab_bar=QTabWidget(self)
                self.tab_bar.resize(300,200)

                self.tab1=QWidget()
                self.tab_bar.addTab(self.tab1,QIcon('python.png'), 'First Tab')
                self.tab2=QWidget()
                self.tab_bar.addTab(self.tab2, 'Second Tab')

                self.lbl=QLabel('Label 1')
                self.tab1.layout=QVBoxLayout(self)
                self.tab1.layout.addWidget(self.lbl)
                self.tab1.setLayout(self.tab1.layout)

                self.btn=QPushButton('Button 1')
                self.tab2.layout=QVBoxLayout(self)
                self.tab2.layout.addWidget(self.btn)
                self.tab2.setLayout(self.tab2.layout)

                self.vbox=QVBoxLayout(self)
                self.vbox.addWidget(self.tab_bar)

                self.setLayout(self.vbox)

                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=TabWindow()
        sys.exit(app.exec_())
   

    

