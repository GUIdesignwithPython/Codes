# Message Box Sample
# Section 2-8
import sys-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox

class MessageBoxSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,280,100)
             self.setWindowTitle('Message Box Sample')
             self.displayComponents()
             self.show()

        def displayComponents(self):
                #تعریف برچسب برای طرح پرسش
                lbl=QLabel(self)
                lbl.setText('Click on the button!')
                lbl.setWordWrap(True)
                lbl.move(100,10)
                lbl.resize(220,60)

                btn=QPushButton('Click!',self)
                btn.move(110,60)
                btn.resize(60,20)
                btn.clicked.connect(self.ShowMessageBox)

        def ShowMessageBox(self):
                msgBox=QMessageBox(self)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText('Message Box Sample')
                msgBox.setInformativeText('Additional Text ...')
                msgBox.setDetailedText('Detailed Text ...')
                msgBox.setWindowTitle('Message Box Title')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.buttonClicked.connect(self.msgBoxClick)
                msgBox.exec_()


        def msgBoxClick(self,msgboxbtn):
                print(msgboxbtn.text())
#اجرای برنامه
if __name__=='__main__':
	app=QApplication(sys.argv)
	window= MessageBoxSample()
	sys.exit(app.exec_())
