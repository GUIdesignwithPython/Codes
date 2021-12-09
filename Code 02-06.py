# Window with 3 Check Boxes
# Section 2-6
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QCheckBox
from PyQt5.QtCore import Qt

class CheckBoxWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,320,160)
             self.setWindowTitle('Window with 3 Check Boxes')
             self.displayComponents()
             self.show()

        def displayComponents(self):
                #تعریف برچسب برای طرح پرسش
                lbl=QLabel(self)
                lbl.setText('Which programming language do you prefer? (You can choose all of them)')
                lbl.setWordWrap(True)
                lbl.move(50,10)
                lbl.resize(220,60)

                #تعریف سه کادر انتخاب
                py=QCheckBox('Python', self)
                py.move(50,80)
                py.toggle()
                py.stateChanged.connect(self.printtoTerminal)

                ja=QCheckBox('Java', self)
                ja.move(50,100)
                #ja.toggle()
                ja.stateChanged.connect(self.printtoTerminal)

                cs=QCheckBox('C#', self)
                cs.move(50,120)
                #cs.toggle()
                cs.stateChanged.connect(self.printtoTerminal)

        def printtoTerminal(self, state):
                sender=self.sender()
                # بررسی وضعیت انتخاب یا عدم انتخاب کادر ارسال کننده سیگنال
                if state==Qt.Checked:
                        print('{} Selected.'.format(sender.text()))
                else:
                        print('{} Deselected.'.format(sender.text()))

#اجرای برنامه
if __name__=='__main__':
	app=QApplication(sys.argv)
	window= CheckBoxWindow()
	sys.exit(app.exec_())
