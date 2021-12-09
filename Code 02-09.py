# List Box Sample
# Section 2-9
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QListWidget,QLabel

class ListBoxSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        
        def initUI(self):
             self.setGeometry(200,250,250,140)
             self.setWindowTitle('List Box Sample')
             self.displayComponents()
             self.show()

        def displayComponents(self):
                self.lbl=QLabel(self)
                self.lbl.setText('Select your favorite color:')
                self.lbl.move(60,10)
                self.lbl.resize(150,30)
                
                
                self.listbox=QListWidget(self)
                self.listbox.insertItem(0,'Red')
                self.listbox.insertItem(1,'Blue')
                self.listbox.insertItem(2,'Green')
                self.listbox.insertItem(3,'Yellow')
                self.listbox.insertItem(4,'Purple')
                self.listbox.insertItem(5,'Pink')
                self.listbox.setSelectionMode(2)
                
                self.listbox.move(65,40)
                self.listbox.resize(100,80)
                self.listbox.itemClicked.connect(self.printItemText)


        def printItemText(self):
                items = self.listbox.selectedItems()
                x = []
                for i in range(len(items)):
                        st=self.listbox.selectedItems()[i].text()
                        x.append(st)
                print (x)

if __name__=='__main__':
	app=QApplication(sys.argv)
	window= ListBoxSample()
	sys.exit(app.exec_())
