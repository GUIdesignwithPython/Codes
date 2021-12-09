# Custom Signals
# Section 4-9
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt,pyqtSignal, QObject

class SendSignal(QObject):
        changeStyle=pyqtSignal()

class CustomSignal(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Custom Signal')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.index=0
                self.direction=''
                self.colorsList=['red','orange','yellow','green','blue','purple']

                self.lbl=QLabel(self)
                self.lbl.setStyleSheet('background-color:{}'.format(self.colorsList[self.index]))
                self.lbl.move(50,50)
                self.lbl.resize(80,30)

                self.sig=SendSignal()
                self.sig.changeStyle.connect(self.BackgroundColor)

        def keyPressEvent(self, event):
                if event.key()==Qt.Key_Up:
                        self.direction='up'
                        self.sig.changeStyle.emit()
                elif event.key()==Qt.Key_Down:
                        self.direction='down'
                        self.sig.changeStyle.emit()

        def BackgroundColor(self):
                if self.direction=='up' and self.index<len(self.colorsList)-1:
                        self.index=self.index+1
                        self.lbl.setStyleSheet('background-color:{}'.format(self.colorsList[self.index]))
                elif self.direction=='down' and self.index>0:
                        self.index=self.index-1
                        self.lbl.setStyleSheet('background-color:{}'.format(self.colorsList[self.index]))
                                                
                


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=CustomSignal()
        sys.exit(app.exec_())
   

    

