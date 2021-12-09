# Sub-Control
# Section 4-5
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox


class SubControlSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,150,150)
                self.setWindowTitle('Sub-Control Sample')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                combo=QComboBox(self)
                combo.move(50,50)
                combo.resize(70,20)
                combo.addItem('Item 1')
                combo.addItem('Item 2')
                combo.addItem('Item 3')


if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setStyleSheet('''QComboBox::drop-down{image: url(python.png)}
                         ''')
        window=SubControlSample()
        sys.exit(app.exec_())
   

    

