# Name Entry Window
# Section 2-5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class EntryWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(200,250,400,200)
                self.setWindowTitle('Name Entry Window')
                self.displayComponents()
                self.show()
        def displayComponents(self):
                QLabel('Please Enter Your Name',self).move(150,20)
                QLabel('First Name: ', self).move(70,50)
                QLabel('Last Name: ', self).move(70,80)

                #تعریف کادرهای متن
                self.fname_entry=QLineEdit(self)
                self.fname_entry.setAlignment(Qt.AlignLeft)
                self.fname_entry.move(130,50)
                self.fname_entry.resize(200,20)

                self.lname_entry=QLineEdit(self)
                self.lname_entry.setAlignment(Qt.AlignHCenter)
                self.lname_entry.move(130,80)
                self.lname_entry.resize(200,20)

                #تعریف دکمه پاک کردن ورودی
                self.clear_button=QPushButton('Clear',self)
                self.clear_button.clicked.connect(self.clearEntries)
                self.clear_button.move(160,130)
        def clearEntries(self):
                sender=self.sender()
                if sender.text()=='Clear':
                        self.fname_entry.clear()
                        self.lname_entry.clear()

#اجرای برنامه
if __name__=='__main__':
        app=QApplication(sys.argv)
        window= EntryWindow()
        sys.exit(app.exec_())
