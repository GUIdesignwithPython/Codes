# Widget StyleSheet Sample
# Section 4-3
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt



class StyleSheetSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
                self.im=1
        def initUI(self):
                self.setGeometry(300,50,200,200)
                self.setWindowTitle('Style Sheet Sample')
                self.displaycomponents()
                self.show()


        def displaycomponents(self):
                lbl=QLabel(self)
                lbl.setText('Hello, World!')
                lbl.setStyleSheet('''background-color: red;
                                     color: white; border: 4px solid black;
                                     border-radius:5px;
                                     font: bold 24px 'Times New Roman' ''')
                lbl.setAlignment(Qt.AlignCenter)
                lbl.move(50,50)
                lbl.resize(150,150)
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=StyleSheetSample()
        sys.exit(app.exec_())
   

    

