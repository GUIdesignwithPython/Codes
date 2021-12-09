# Programming Language Survey
# Section 3-10
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout,QVBoxLayout, QRadioButton,QPushButton,QButtonGroup
from PyQt5.QtGui import QFont



class Survey(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(300,50,10,10)
                self.setWindowTitle('Programming Language Survey')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                titlelbl=QLabel('Programming Language Survey')
                font=QFont('Times new roman',15,QFont.Bold)
                font.setUnderline(True)
                titlelbl.setFont(font)
                title_hbox=QHBoxLayout()
                title_hbox.addStretch()
                title_hbox.addWidget(titlelbl)
                title_hbox.addStretch()

                prg_lng=['Python', 'Java', 'C#', 'Others']

                question1=QLabel('1. Which programming language do you prefer for web application programming?')
                btn_group1=QButtonGroup(self)
                prg_hbox=QHBoxLayout()
                prg_hbox.setSpacing(80)
                for p in prg_lng:
                        prg=QRadioButton(p, self)
                        btn_group1.addButton(prg)
                        prg_hbox.addWidget(prg)
                question1_vbox=QVBoxLayout()
                question1_vbox.setSpacing(5)
                question1_vbox.addWidget(question1)
                question1_vbox.addLayout(prg_hbox)
                

                question2=QLabel('2. Which programming language do you prefer for desktop programming?')
                btn_group2=QButtonGroup(self)
                prg_hbox2=QHBoxLayout()
                prg_hbox2.setSpacing(80)
                for p in prg_lng:
                        prg=QRadioButton(p, self)
                        btn_group2.addButton(prg)
                        prg_hbox2.addWidget(prg)
                
                question2_vbox=QVBoxLayout()
                question2_vbox.setSpacing(5)
                question2_vbox.addWidget(question2)
                question2_vbox.addLayout(prg_hbox2)




                submit=QPushButton('Submit')

                btn_hbox=QHBoxLayout()
                btn_hbox.addStretch()
                btn_hbox.addWidget(submit)
                btn_hbox.addStretch()                

                

                layout=QVBoxLayout()
                layout.setSpacing(20)
                layout.addLayout(title_hbox)
                layout.addLayout(question1_vbox)
                layout.addLayout(question2_vbox)
                layout.addLayout(btn_hbox)
                self.setLayout(layout)


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=Survey()
        sys.exit(app.exec_())
   

    

