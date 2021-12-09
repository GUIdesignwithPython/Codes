# Application StyleSheet Sample
# Section 4-4
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QVBoxLayout


class AppStyleSheetSample(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,50,50)
                self.setWindowTitle('App Style Sheet Sample')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                lbl1=QLabel(self)
                lbl1.setText('Label 1')

                lbl2=QLabel(self)
                lbl2.setText('Label 2')

                btn1=QPushButton(self)
                btn1.setText('Button 1')

                btn2=QPushButton(self)
                btn2.setText('Button 2')

                layout=QVBoxLayout()
                layout.addWidget(lbl1)
                layout.addWidget(lbl2)
                layout.addWidget(btn1)
                layout.addWidget(btn2)

                self.setLayout(layout)


if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setStyleSheet('''QPushButton{color:white;
                             background-color:red; border:2px solid black;
                             border-radius:3px}
                             QLabel{color:white; background-color:black;
                             font: Bold 14px 'Tahoma';
                             qproperty-alignment: AlignCenter}
                             ''')
        window=AppStyleSheetSample()
        sys.exit(app.exec_())
   

    

