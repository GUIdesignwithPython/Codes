# Form Layout
# Section 3-7
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout
from PyQt5.QtWidgets import QLineEdit,QSpinBox

class FormLayout(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,250,100)
                self.setWindowTitle('Form Layout')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                name=QLineEdit()
                email=QLineEdit()
                age=QSpinBox()
                button=QPushButton('Click')
                formLayout = QFormLayout()
                formLayout.addRow('Name:', name)
                formLayout.addRow('Email:', email)
                formLayout.addRow('Age:', age)
                formLayout.addRow(button)
                self.setLayout(formLayout)
                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=FormLayout()
        sys.exit(app.exec_())
   

    

