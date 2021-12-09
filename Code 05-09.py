# Dock Widget
# Section 5-6
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QListWidget, QTextEdit, QVBoxLayout, QLabel, QWidget, QPushButton
from PyQt5.QtCore import Qt

class InformationForm(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,500,500)
                self.setWindowTitle('Dock Widget Sample')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.dockwindow=QDockWidget('Dock', self)
                self.dockwindow.setGeometry(50,50,70,80)
                self.dockwindow.setFloating(False)


                widget=QWidget()
                widget.layout=QVBoxLayout(self)
                textbox=QTextEdit(self)
                lbl=QLabel('Label 1', self)
                widget.layout.addWidget(lbl)
                widget.layout.addWidget(textbox)
                widget.setLayout(widget.layout)

                widget2=QWidget()
                widget2.layout=QVBoxLayout(self)
                self.btn=QPushButton('Button')
                self.listWidget=QListWidget()
                self.listWidget.addItem('Item1')
                self.listWidget.addItem('Item2')
                self.listWidget.addItem('Item3')
                self.listWidget.addItem('Item4')
                widget2.layout.addWidget(self.listWidget)
                widget2.layout.addWidget(self.btn)
                widget2.setLayout(widget2.layout)

                
                self.setCentralWidget(widget)
                self.dockwindow.setWidget(widget2)
                self.addDockWidget(Qt.RightDockWidgetArea, self.dockwindow)
                self.dockwindow.setAllowedAreas(Qt.RightDockWidgetArea)


if __name__=='__main__':
        app=QApplication(sys.argv)
        window=InformationForm()
        sys.exit(app.exec_())
   

    

