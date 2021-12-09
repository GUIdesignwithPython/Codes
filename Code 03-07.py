# Stretch Grid Layout
# Section 3-8
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout


class GridLayout(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,450,100)
                self.setWindowTitle('Stretch Grid Layout')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                grid = QGridLayout()
                for i in range(0,3):
                        for j in range(0,3):
                                grid.addWidget(QPushButton('B'+str(i)+str(j)),i,j)
                        grid.setColumnStretch(i ,i+1)      
                self.setLayout(grid)


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=GridLayout()
        sys.exit(app.exec_())
   

    

