# Body Mass Index
# Section 3-11
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QHBoxLayout, QVBoxLayout, QFormLayout, QSpinBox, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QIntValidator



class BMI(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(300,50,10,10)
                self.setWindowTitle('Body Mass Index Calculation')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                titlelbl=QLabel('Body Mass Index')
                font=QFont('Times new roman',15,QFont.Bold)
                font.setUnderline(True)
                titlelbl.setFont(font)
                title_hbox=QHBoxLayout()
                title_hbox.addStretch()
                title_hbox.addWidget(titlelbl)
                title_hbox.addStretch()

                self.age=QSpinBox()
                self.age.setRange(17,120)
                self.height=QLineEdit()
                self.height.setPlaceholderText('cm')
                valid_height=QIntValidator(1,250,self)
                self.height.setValidator(valid_height)
                self.mass=QLineEdit()
                self.mass.setPlaceholderText('kg')
                valid_mass=QIntValidator(1,200,self)
                self.mass.setValidator(valid_mass)
                calc_btn=QPushButton('Calculate!')
                calc_btn.clicked.connect(self.calc_bmi)
                self.result1=QLabel('Result:')
                self.result2=QLabel('')
                self.result3=QLabel('')
                self.result4=QLabel('')

                
                form=QFormLayout()
                form.addRow('Age =',self.age)
                form.addRow('Height = ',self.height)
                form.addRow('Mass = ',self.mass)
                form.addRow(calc_btn)
                form.addRow(self.result1)
                form.addRow(self.result2)
                form.addRow(self.result3)
                form.addRow(self.result4)
                

                layout=QVBoxLayout()
                layout.setSpacing(10)
                layout.addLayout(title_hbox)
                layout.addLayout(form)
                self.setLayout(layout)

        def calc_bmi(self):
                self.result2.setText('')
                self.result3.setText('')
                self.result4.setText('')
                int_age=int(self.age.text())
                if self.height.text()!='' and self.mass.text()!='':
                        h=int(self.height.text())/100
                        m=int(self.mass.text())
                        bmi=m/(h*h)
                        self.result2.setText(str('Your BMI is = {:.2f} '.format(bmi)))
                        if bmi<=18.4:
                                res='You are underweight.'
                        elif bmi<=24.9:
                                res='You are in normal range.'
                        else:
                                res='You are overweight.'
                        self.result3.setText(res)
                        if 17<=int_age<24:
                                re='Your preferred BMI is 21.'
                        elif 24<=int_age<44:
                                re='Your preferred BMI is 24.'
                        elif 44<=int_age<54:
                                re='Your preferred BMI is 25.'
                        else:
                                re='Your preferred BMI is 27.'
                        self.result4.setText(re)
                else:
                        self.result2.setText('Enter height and mass correctly!')

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=BMI()
        sys.exit(app.exec_())
   

    

