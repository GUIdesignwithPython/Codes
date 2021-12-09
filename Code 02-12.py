# Sign-Up New User
# Section 2-13
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QLineEdit,QRadioButton,QCheckBox,QComboBox,QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__() 
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 330, 380)
        self.setWindowTitle('Sign-Up New User')
        self.displaycomponents()
        self.show()

    def displaycomponents(self):
        self.titlelbl=QLabel(self)
        self.titlelbl.setText('Create New Account')
        self.titlelbl.move(55,10)
        self.titlelbl.setFont(QFont('Times New Roman',20))
        image='signup.png'
        pixmap=QPixmap(image)
        pixmap.scaled(50,50)
        self.iconlbl=QLabel(self)
        self.iconlbl.setPixmap(pixmap)
        self.iconlbl.setScaledContents(True)
        self.iconlbl.move(140,35)
        self.iconlbl.resize(50,50)
        

        self.namelbl=QLabel(self)
        self.namelbl.setText('Name: ')
        self.namelbl.move(50,100)

        self.name=QLineEdit(self)
        self.name.move(120,100)
        self.name.resize(165,20)

        self.bdlbl=QLabel(self)
        self.bdlbl.setText('Birthday: ')
        self.bdlbl.move(50,135)


        self.day=QComboBox(self)
        self.day.move(120,135)
        for i in range(1,32):
            self.day.addItem(str(i))

        self.month=QComboBox(self)
        self.month.move(170,135)
        for i in range(1,13):
            self.month.addItem(str(i))

        self.year=QComboBox(self)
        self.year.move(220,135)
        for i in range(1300,1401):
            self.year.addItem(str(i))

        
        self.genderlbl=QLabel(self)
        self.genderlbl.setText('Gender: ')
        self.genderlbl.move(50,170)

        self.male=QRadioButton(self)
        self.male.setText('Male')
        self.male.move(120,170)
        self.male.toggle()
        self.female=QRadioButton(self)
        self.female.setText('Female')
        self.female.move(190,170)
        

        self.usrlbl=QLabel(self)
        self.usrlbl.setText('Username : ')
        self.usrlbl.move(50,205)

        self.usr=QLineEdit(self)
        self.usr.move(120,205)
        self.usr.resize(165,20)
        
        self.passlbl=QLabel(self)
        self.passlbl.setText('Password : ')
        self.passlbl.move(50,240)

        self.passconflbl=QLabel(self)
        self.passconflbl.setText('Confirm : ')
        self.passconflbl.move(50,270)

        self.passw=QLineEdit(self)
        self.passw.setEchoMode(QLineEdit.Password)
        self.passw.move(120,240)
        self.passw.resize(165,20)

        self.passwconf=QLineEdit(self)
        self.passwconf.setEchoMode(QLineEdit.Password)
        self.passwconf.move(120,270)
        self.passwconf.resize(165,20)
        
        self.showpass=QCheckBox(self)
        self.showpass.setText('Show Password')
        self.showpass.stateChanged.connect(self.ShowPassword)
        self.showpass.move(120,290)

        self.signupbtn=QPushButton(self)
        self.signupbtn.setText('Sign Up')
        self.signupbtn.move(75,330)
        self.signupbtn.resize(170,30)
        self.signupbtn.clicked.connect(self.SignUp)

    def ShowPassword(self, state):
        if state==Qt.Checked:
            self.passw.setEchoMode(QLineEdit.Normal)
            self.passwconf.setEchoMode(QLineEdit.Normal)
        else:
            self.passw.setEchoMode(QLineEdit.Password)
            self.passwconf.setEchoMode(QLineEdit.Password)

    def SignUp(self):
        if self.passw.text()!=self.passwconf.text():
            msgbox=QMessageBox(self)
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText('The passwords do not match. Please try again.')
            msgbox.setWindowTitle('Error Message')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()
        elif self.usr.text().strip()=='' or self.name.text().strip()=='':
            msgbox=QMessageBox(self)
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText('Please enter name and username correctly!')
            msgbox.setWindowTitle('Error Message')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()
        else:
            msgbox=QMessageBox(self)
            msgbox.setIcon(QMessageBox.Information)
            msgbox.setText('The new account has been created successfully.')
            msgbox.setWindowTitle('Congradulation!')
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.exec_()

            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUpWindow()
    sys.exit(app.exec_())
