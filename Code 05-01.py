# Simple Menu
# Section 5-2
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class SimpleMenu(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,300)
                self.setWindowTitle('Simple Menu Example')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                menu_bar=self.menuBar()

                exit_menu=QAction('E&xit', self)
                exit_menu.setShortcut('Ctrl+Q')
                exit_menu.triggered.connect(self.close)

                file_menu=menu_bar.addMenu('&File')
                file_menu.addAction(exit_menu)



if __name__=='__main__':
        app=QApplication(sys.argv)
        window=SimpleMenu()
        sys.exit(app.exec_())
   

    

