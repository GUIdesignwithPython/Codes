# Simple Calculator
# Section 3-13
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt



class Calculator(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,10,10)
                self.setWindowTitle('Simple Calculator')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.label = QLabel(self)
                self.label.setWordWrap(True)
                self.label.setText('')
                self.label.setAlignment(Qt.AlignRight)
                self.label.setStyleSheet('border: 3px solid red')
                self.label.setFont(QFont('Arial', 15))

                push1 = QPushButton('1', self)
                push2 = QPushButton('2', self)
                push3 = QPushButton('3', self)
                push4 = QPushButton('4', self)
                push5 = QPushButton('5', self)
                push6 = QPushButton('6', self)
                push7 = QPushButton('7', self)
                push8 = QPushButton('8', self)
                push9 = QPushButton('9', self)
                push0 = QPushButton('0', self)
                push_equal = QPushButton('=', self)
                push_plus = QPushButton('+', self)
                push_minus = QPushButton('-', self)
                push_mul = QPushButton('*', self)
                push_div = QPushButton('/', self)
                push_point = QPushButton('.', self)
                push_clear = QPushButton('C', self)
                push_del = QPushButton('Del', self)
                push0.clicked.connect(self.action0)
                push1.clicked.connect(self.action1)
                push2.clicked.connect(self.action2)
                push3.clicked.connect(self.action3)
                push4.clicked.connect(self.action4)
                push5.clicked.connect(self.action5)
                push6.clicked.connect(self.action6)
                push7.clicked.connect(self.action7)
                push8.clicked.connect(self.action8)
                push9.clicked.connect(self.action9)
                push_div.clicked.connect(self.action_div)
                push_mul.clicked.connect(self.action_mul)
                push_plus.clicked.connect(self.action_plus)
                push_minus.clicked.connect(self.action_minus)
                push_equal.clicked.connect(self.action_equal)
                push_point.clicked.connect(self.action_point)
                push_clear.clicked.connect(self.action_clear)
                push_del.clicked.connect(self.action_del)

                push_plus.setMinimumHeight(57)
                push_equal.setMinimumHeight(30)

                grid=QGridLayout()
                grid.addWidget(self.label,0,0,1,4)
                grid.addWidget(push_clear,1,0,1,2)
                grid.addWidget(push_del,1,2,1,2)
                grid.addWidget(push1,2,0)
                grid.addWidget(push2,2,1)
                grid.addWidget(push3,2,2)
                grid.addWidget(push_mul,2,3)
                grid.addWidget(push4,3,0)
                grid.addWidget(push5,3,1)
                grid.addWidget(push6,3,2)
                grid.addWidget(push_div,3,3)
                grid.addWidget(push7,4,0)
                grid.addWidget(push8,4,1)
                grid.addWidget(push9,4,2)
                grid.addWidget(push_minus,4,3)
                grid.addWidget(push_point,5,0)
                grid.addWidget(push0,5,1,1,2)
                grid.addWidget(push_plus,5,3,2,1)
                grid.addWidget(push_equal,6,0,1,3)
                self.setLayout(grid)

        def action_equal(self):
                equation = self.label.text()
                try:
                    ans = eval(equation)
                    self.label.setText(str(ans))
                except:
                    self.label.setText('Wrong Input')
          
        def action_plus(self):
                text = self.label.text()
                self.label.setText(text + '+')
          
        def action_minus(self):
                text = self.label.text()
                self.label.setText(text + '-')
          
        def action_div(self):
                text = self.label.text()
                self.label.setText(text + '/')
          
        def action_mul(self):
                text = self.label.text()
                self.label.setText(text + '*')
          
        def action_point(self):
                text = self.label.text()
                self.label.setText(text + '.')
          
        def action0(self):
                text = self.label.text()
                self.label.setText(text + '0')
          
        def action1(self):
                text = self.label.text()
                self.label.setText(text + '1')
          
        def action2(self):
                text = self.label.text()
                self.label.setText(text + '2')
          
        def action3(self):
                text = self.label.text()
                self.label.setText(text + '3')
          
        def action4(self):
                text = self.label.text()
                self.label.setText(text + '4')
          
        def action5(self):
                text = self.label.text()
                self.label.setText(text + '5')
          
        def action6(self):
                text = self.label.text()
                self.label.setText(text + '6')
          
        def action7(self):
                text = self.label.text()
                self.label.setText(text + '7')
          
        def action8(self):
                text = self.label.text()
                self.label.setText(text + '8')
          
        def action9(self):
                text = self.label.text()
                self.label.setText(text + '9')
          
        def action_clear(self):
                self.label.setText('')
          
        def action_del(self):
                text = self.label.text()
                self.label.setText(text[:len(text)-1])
               
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=Calculator()
        sys.exit(app.exec_())
   

    

