# Input Dialog Sample
# Section 2-11
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QInputDialog, QMessageBox

class InputDialogSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,260,80)
             self.setWindowTitle('Input Dialog Sample')
             self.displayComponent()
             self.show()

        def displayComponent(self):
                self.btn=QPushButton(self)
                self.btn.setText('Click to START!')
                self.btn.resize(100,30)
                self.btn.move(80,25)
                self.btn.clicked.connect(self.showInputDialog)
                
        def showInputDialog(self):
                self.inputdlg=QInputDialog(self)
                text,ok=self.inputdlg.getText(self,'Input Dialog Title','Enter Your Name:')
                if ok and text:
                        msgBox=QMessageBox(self)
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setText('Hello, '+text+'!')
                        msgBox.setWindowTitle('Greeting')
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        msgBox.exec_()
                      



#اجرای برنامه
if __name__=='__main__':
	app=QApplication(sys.argv)
	window= InputDialogSample()
	sys.exit(app.exec_())
