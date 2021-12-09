# Meeting Submission
# Section 3-12
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout,QLineEdit,QFormLayout, QCalendarWidget, QComboBox, QRadioButton, QButtonGroup, QTextEdit, QPushButton,QMessageBox
from PyQt5.QtGui import QFont



class Meeting_Submission(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
                self.im=1
        def initUI(self):
                self.setGeometry(300,50,10,10)
                self.setWindowTitle('Meeting Management')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                titlelbl=QLabel('Meeting Submission Form')
                font=QFont('Times new roman',15,QFont.Bold)
                font.setUnderline(True)
                titlelbl.setFont(font)
                title_hbox=QHBoxLayout()
                title_hbox.addStretch()
                title_hbox.addWidget(titlelbl)
                title_hbox.addStretch()

                self.name=QLineEdit()
                self.add=QLineEdit()
                self.phone=QLineEdit()
                self.phone.setInputMask('9999-000-0000')
                self.email=QLineEdit()
                self.email.setInputMask('NNNNNNNNN@NNNNNNNN.NNN')
                self.calendar=QCalendarWidget()
                self.calendar.setGridVisible(True)
                hbox=QHBoxLayout()
                self.hour=QComboBox()
                self.hour.setEditable(True)
                for i in range(0,24):
                        self.hour.addItem(str(i))
                self.minute=QComboBox()
                self.minute.setEditable(True)
                mins=['00','15','30','45']
                for i in mins:
                        self.minute.addItem(i)
                hour_lbl=QLabel('Hour: ')
                minute_lbl=QLabel('Minute: ')
                hbox.addWidget(hour_lbl)
                hbox.addWidget(self.hour)
                hbox.addWidget(minute_lbl)
                hbox.addWidget(self.minute)

                types=['Virtual Meeting','Appointment','Web Conference']

                self.app_type=QComboBox()
                for i in types:
                        self.app_type.addItem(i)
                
                self.Rb1=QRadioButton('1 (Low)')
                self.Rb1.toggle()
                self.Rb2=QRadioButton('2')
                self.Rb3=QRadioButton('3')
                self.Rb4=QRadioButton('4')
                self.Rb5=QRadioButton('5 (High)')

                grp=QButtonGroup(self)
                grp.addButton(self.Rb1)
                grp.addButton(self.Rb2)
                grp.addButton(self.Rb3)
                grp.addButton(self.Rb4)
                grp.addButton(self.Rb5)
                grp.buttonClicked.connect(self.importance)

                hbox2=QHBoxLayout()
                hbox2.addWidget(self.Rb1)
                hbox2.addWidget(self.Rb2)
                hbox2.addWidget(self.Rb3)
                hbox2.addWidget(self.Rb4)
                hbox2.addWidget(self.Rb5)

                self.info=QTextEdit()

                submit=QPushButton('Submit')
                submit.clicked.connect(self.Submit)
                clear=QPushButton('Clear')
                clear.clicked.connect(self.clear)
                hbox3=QHBoxLayout()
                hbox3.addStretch()
                hbox3.addWidget(submit)
                hbox3.addWidget(clear)
                hbox3.addStretch()
               
                form=QFormLayout()
                form.addRow('Name: ',self.name)
                form.addRow('Address :', self.add)
                form.addRow('Mobile Number: ',self.phone)
                form.addRow('E-Mail Address: ',self.email)
                form.addRow('Date: ',self.calendar)
                form.addRow('Time: ',hbox)
                form.addRow('Meeting Type: ', self.app_type)
                form.addRow('Importance: ', hbox2)
                form.addRow('Information: ',self.info)
                form.addRow(hbox3)

                layout=QVBoxLayout()
                layout.setSpacing(10)
                layout.addLayout(title_hbox)
                layout.addLayout(form)
                self.setLayout(layout)

        def Submit(self):
                st='A meeting with '+self.name.text()+ ' on '+self.calendar.selectedDate().toString('MMMM d, yyyy')+ \
                    ' at ' + self.hour.currentText()+':'+self.minute.currentText()+' is submitted. \n' + \
                    'Meeting Type: '+self.app_type.currentText()+ '\n' + \
                    'Address: '+self.add.text() +'\n' + \
                    'Phone Number : '+self.phone.text()+ '\n' + \
                    'E-mail :'+self.email.text() + '\n' +\
                   'Meeting Importance: '+ str(self.im) + ' out of 5'
                st2='Information : ' +self.info.toPlainText()
                msg=QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setText(st)
                msg.setInformativeText(st2)
                msg.setWindowTitle('New Meeting Submitted')
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

        def importance(self, bt):
               self.im=bt.text()[0]

        def clear(self):
                self.name.clear()
                self.add.clear()
                self.phone.clear()
                self.email.clear()
                self.name.clear()
                self.info.clear()
               
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=Meeting_Submission()
        sys.exit(app.exec_())
   

    

