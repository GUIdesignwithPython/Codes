# Span Grid Layout
# Section 3-8
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class GridLayout(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,450,100)
                self.setWindowTitle('Span Grid Layout')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                grid = QGridLayout()
                button = QPushButton('1-3')
                grid.addWidget(button, 0, 0, 1, 3)
                
                button = QPushButton('4, 7')
                grid.addWidget(button, 1, 0, -1, 1)
                
                for i in range(1, 3):
                    for j in range(1, 3):
                        button = QPushButton(str(3*i+j+1))
                        grid.addWidget(button, i, j)
      
                self.setLayout(grid)


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=GridLayout()
        sys.exit(app.exec_())
   

    

