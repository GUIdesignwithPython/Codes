# Stacked Layout
# Section 3-9
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QStackedWidget, QListWidget,QFormLayout,QLineEdit,QHBoxLayout,QRadioButton,QLabel,QCheckBox,QStackedWidget



class StackedLayout(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(300,50,10,10)
                self.setWindowTitle('Stacked Layout')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.leftlist = QListWidget()
                self.leftlist.insertItem (0, 'Contact' )
                self.leftlist.insertItem (1, 'Personal' )
                self.leftlist.insertItem (2, 'Educational' )
                self.leftlist.currentRowChanged.connect(self.display)
                
                self.stack1 = QWidget()
                self.stack2 = QWidget()
                self.stack3 = QWidget()

                self.stack1UI()
                self.stack2UI()
                self.stack3UI()

                self.Stack = QStackedWidget(self)
                self.Stack.addWidget(self.stack1)
                self.Stack.addWidget(self.stack2)
                self.Stack.addWidget(self.stack3)

                self.hbox = QHBoxLayout(self)
                self.hbox.addWidget(self.leftlist)
                self.hbox.addWidget(self.Stack)

                self.setLayout(self.hbox)
                

        def stack1UI(self):
                layout = QFormLayout()
                layout.addRow('Name: ',QLineEdit())
                layout.addRow('Address: ',QLineEdit())
                self.stack1.setLayout(layout)

        def stack2UI(self):
                layout = QFormLayout()
                gender = QHBoxLayout()
                gender.addWidget(QRadioButton('Male'))
                gender.addWidget(QRadioButton('Female'))
                layout.addRow(QLabel('Gender: '),gender)
                layout.addRow('Date of Birth: ',QLineEdit())
                self.stack2.setLayout(layout)

        def stack3UI(self):
                layout = QHBoxLayout()
                layout.addWidget(QLabel('Subjects: '))
                layout.addWidget(QCheckBox('Physics'))
                layout.addWidget(QCheckBox('Maths'))
                layout.addWidget(QCheckBox('Science'))
                self.stack3.setLayout(layout)

        def display(self,i):
                self.Stack.setCurrentIndex(i)

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=StackedLayout()
        sys.exit(app.exec_())
   

    

