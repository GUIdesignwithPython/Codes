# New Email Message
# Section 4-11
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QLineEdit,QFormLayout,QCheckBox,QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize

Style_Sheet='''
        QWidget{
                background:#F8B4A5
               }
        QWidget:focus{
                border:1px dashed red
               }
        QPushButton{
                background:#E16449
               }
        QPushButton#sendbtn{
                background:#EFC2B8
               }
        QLineEdit{
                background:white;
                border-radius:2px;
                border:1px solid black
               }
        QLineEdit:disabled{
                background:gray;
               }
        QTextEdit{
                background:white;
                border:1px solid black;
                border-radius:5px
               }
        QLabel#titlelbl{
                border:2px dashed black;
                border-radius:6px
               }
        QChechBox{
                border-radius:2px
               }
            '''

class SendEmail(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,300)
                self.setWindowTitle('Send Email')
                self.setWindowIcon(QIcon('email.png'))
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                titlelbl=QLabel('New Message')
                titlelbl.setObjectName('titlelbl')
                font=QFont('Times new roman',15,QFont.Bold)
                titlelbl.setFont(font)
                title_hbox=QHBoxLayout()
                title_hbox.addStretch()
                title_hbox.addWidget(titlelbl)
                title_hbox.addStretch()

                totext=QLineEdit(self)
                check_cc=QCheckBox(self)
                check_cc.setText('CC: ')
                check_cc.stateChanged.connect(self.ccStateChange)
                check_bcc=QCheckBox(self)
                check_bcc.setText('BCC: ')
                check_bcc.stateChanged.connect(self.bccStateChange)
                self.cctext=QLineEdit(self)
                self.cctext.setEnabled(False)
                self.bcctext=QLineEdit(self)
                self.bcctext.setEnabled(False)
                subjecttext=QLineEdit(self)


                to_form=QFormLayout()
                to_form.addRow('To: ',totext)
                to_form.addRow(check_cc,self.cctext)
                to_form.addRow(check_bcc,self.bcctext)
                to_form.addRow('Subject: ',subjecttext)

                messagelbl=QLabel(self)
                messagelbl.setText('Message: ')

                savebtn=QPushButton(self)
                savebtn.setText('Save as Draft')
                savebtn.setIcon(QIcon('draft.png'))
                savebtn.setIconSize(QSize(20,20))

                attachbtn=QPushButton(self)
                attachbtn.setText('Attach')
                attachbtn.setIcon(QIcon('attach.png'))
                attachbtn.setIconSize(QSize(20,20))

                hbox1=QHBoxLayout()
                hbox1.addWidget(messagelbl)

                hbox2=QHBoxLayout()
                hbox2.addWidget(savebtn)
                hbox2.addWidget(attachbtn)

                hbox3=QHBoxLayout()
                hbox3.addLayout(hbox1)
                hbox3.addLayout(hbox2)
                


                message=QTextEdit()
                hbox4=QHBoxLayout()
                hbox4.addWidget(message)

                sendbtn=QPushButton(self)
                sendbtn.setObjectName('sendbtn')
                sendbtn.setText('Send')
                sendbtn.setIcon(QIcon('send.png'))
                sendbtn.setIconSize(QSize(20,20))
                resetbtn=QPushButton(self)
                resetbtn.setText('Reset')
                resetbtn.setIcon(QIcon('reset.jpg'))
                resetbtn.setIconSize(QSize(20,20))

                hbox5=QHBoxLayout()
                hbox5.addStretch()
                hbox5.addWidget(sendbtn)
                hbox5.addWidget(resetbtn)
                
                layout=QVBoxLayout()
                layout.setSpacing(5)
                layout.addLayout(title_hbox)
                layout.addLayout(to_form)
                layout.addLayout(hbox3)
                layout.addLayout(hbox4)
                layout.addLayout(hbox5)
                self.setLayout(layout)

        def ccStateChange(self,state):
                if state==Qt.Checked:
                        self.cctext.setEnabled(True)
                else:
                        self.cctext.setEnabled(False)
                
        def bccStateChange(self,state):
                if state==Qt.Checked:
                        self.bcctext.setEnabled(True)
                else:
                        self.bcctext.setEnabled(False)



if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setStyleSheet(Style_Sheet)
        window=SendEmail()
        sys.exit(app.exec_())
   

    

