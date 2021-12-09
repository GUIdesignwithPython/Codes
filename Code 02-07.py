# Window with Radio Buttons
# Section 2-7
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QRadioButton
from PyQt5.QtCore import Qt

class RadioButtonWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,320,160)
             self.setWindowTitle('Window with Radio Buttons')
             self.displayComponents()
             self.show()

        def displayComponents(self):
                #تعریف برچسب برای طرح پرسش
                lbl=QLabel(self)
                lbl.setText('Which programming language do you prefer? (You can choose one of them)')
                lbl.setWordWrap(True)
                lbl.move(50,10)
                lbl.resize(220,60)

                #تعریف سه کادر انتخاب
                py=QRadioButton('Python', self)
                py.move(50,80)
                py.toggle()
                py.clicked.connect(self.printtoTerminal)

                ja=QRadioButton('Java', self)
                ja.move(50,100)
                #ja.toggle()
                ja.clicked.connect(self.printtoTerminal)

                cs=QRadioButton('C#', self)
                cs.move(50,120)
                #cs.toggle()
                cs.clicked.connect(self.printtoTerminal)

        def printtoTerminal(self):
                sender=self.sender()
                # بررسی وضعیت انتخاب یا عدم انتخاب کادر ارسال کننده سیگنال
                #if sender.isChecked()==True:
                #        print('{} Selectd.'.format(sender.text()))
                #else:
                #        print('{} Deselected.'.format(sender.text()))
                print('{} Selected.'.format(sender.text()))

#اجرای برنامه
if __name__=='__main__':
	app=QApplication(sys.argv)
	window= RadioButtonWindow()
	sys.exit(app.exec_())
