# Message Entry Window
# Section 2-5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtWidgets import QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class MessageEntryWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(200,250,400,200)
                self.setWindowTitle('Message Entry Window')
                self.displayComponents()
                self.show()
        def displayComponents(self):
                QLabel('Enter Your Message',self).move(150,20)
                QLabel('Message: ', self).move(70,50)

                #تعریف کادرهای متن
                self.message_entry=QTextEdit(self)
                self.message_entry.move(130,50)
                self.message_entry.resize(200,60)


                #تعریف دکمه پاک کردن ورودی
                self.clear_button=QPushButton('Clear',self)
                self.clear_button.clicked.connect(self.clearEntries)
                self.clear_button.move(160,130)
        def clearEntries(self):
                sender=self.sender()
                if sender.text()=='Clear':
                        self.message_entry.clear()

#اجرای برنامه
if __name__=='__main__':
        app=QApplication(sys.argv)
        window= MessageEntryWindow()
        sys.exit(app.exec_())
