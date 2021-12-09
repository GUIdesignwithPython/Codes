# Application StyleSheet Sample 2
# Section 4-4
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QVBoxLayout


class AppStyleSheetSample2(QWidget):
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

                lbl3=QLabel(self)
                lbl3.setObjectName('label3')
                lbl3.setText('Label 3')

                btn1=QPushButton(self)
                btn1.setText('Button 1')

                btn2=QPushButton(self)
                btn2.setText('Button 2')

                btn3=QPushButton(self)
                btn3.setObjectName('button3')
                btn3.setText('Button 3')

                layout=QVBoxLayout()
                layout.addWidget(lbl1)
                layout.addWidget(lbl2)
                layout.addWidget(lbl3)
                layout.addWidget(btn1)
                layout.addWidget(btn2)
                layout.addWidget(btn3)

                self.setLayout(layout)


if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setStyleSheet('''QPushButton{color:white;
                             background-color:red; border:2px solid black;
                             border-radius:3px}
                             QPushButton#button3{background-color:skyblue}
                             QLabel{color:white; background-color:black;
                             font: Bold 14px 'Tahoma';
                             qproperty-alignment: AlignCenter}
                             QLabel#label3{background-color:white;
                                           color:black;
                                           border: 1px dashed black}
                             ''')
        window=AppStyleSheetSample2()
        sys.exit(app.exec_())
   

    

