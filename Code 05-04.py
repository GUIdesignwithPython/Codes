# ToolBar
# Secction 5-3
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class ToolbarWindow(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Window with a Toolbar')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):

                toolbar=QToolBar('New Toolbar', self)
                toolbar.setIconSize(QSize(30,30))
                self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                self.addToolBar(toolbar)


                btn1=QAction('Button 1', self)
                toolbar.addAction(btn1)
                toolbar.addSeparator()

                btn2=QAction('Button 2', self)
                btn2.setIcon(QIcon('python.png'))
                
                toolbar.addAction(btn2)
            
                
                toolbar.addSeparator()
                lbl=QLabel('Label 1', self)
                toolbar.addWidget(lbl)


                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=ToolbarWindow()
        sys.exit(app.exec_())
   

    

