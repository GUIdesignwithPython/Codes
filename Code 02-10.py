# Combo Box Sample
# Section 2-10
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QComboBox, QLabel

class ComboBoxSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,260,140)
             self.setWindowTitle('Combo Box Sample')
             self.displayComponents()
             self.show()

        def displayComponents(self):
                self.lbl=QLabel(self)
                self.lbl.setText('Select your favorite fruit:')
                self.lbl.move(60,10)
                self.lbl.resize(150,30)
                
                self.combo=QComboBox(self)
                self.combo.addItem('Apple')
                self.combo.addItem('Orange')
                self.combo.addItem('Lemon')
                self.combo.addItem('Watermelon')
                self.combo.setEditable(True)
                self.combo.move(65,40)
                self.combo.resize(100,20)
                self.combo.activated[str].connect(self.onChanged)

                self.selectlbl=QLabel(self)
                self.selectlbl.move(60,100)

        def onChanged(self,text):
                self.selectlbl.setText('Your favorite fruit is '+str(text)+'.')
                self.selectlbl.adjustSize()



#اجرای برنامه
if __name__=='__main__':
	app=QApplication(sys.argv)
	window= ComboBoxSample()
	sys.exit(app.exec_())
