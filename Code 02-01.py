# Empty Window
# Section 2-2
import sys	
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
	def __init__(self):
		super().__init__()      
		self.initUI()           
	def initUI(self):
		self.setGeometry(200,250,500,380)
		self.setWindowTitle('Empty Window')
		self.show()

if __name__=='__main__':
	app=QApplication(sys.argv)
	window=EmptyWindow()
	sys.exit(app.exec_())
   

    

