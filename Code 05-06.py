# Change label's font and color
# Section 5-4
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QStatusBar, QLabel, QColorDialog, QFontDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class LabelSettingsWindow(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,200)
                self.setWindowTitle('Label Setting')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                font_act=QAction('Font', self)
                font_act.setIcon(QIcon('font.png'))
                font_act.setStatusTip('Use this button to change font of label.')
                font_act.triggered.connect(self.changeFont)

                color_act=QAction('Color', self)
                color_act.setStatusTip('Use this button to change color of label.')
                color_act.triggered.connect(self.changeColor)
                color_act.setIcon(QIcon('color.jpg'))
                
                toolbar=QToolBar('New Toolbar', self)
                toolbar.setIconSize(QSize(30,30))
                self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
                toolbar.addAction(font_act)
                toolbar.addAction(color_act)
                self.addToolBar(toolbar)

                self.setStatusBar(QStatusBar(self))
                self.statusBar().showMessage('Welcome to label setting window!')

                self.lbl=QLabel('This is my sample label!')
                self.lbl.setAlignment(Qt.AlignCenter)
                self.setCentralWidget(self.lbl)

        def changeFont(self):
                font, ok = QFontDialog.getFont()
                self.lbl.setFont(font)

        def changeColor(self):
                color = QColorDialog.getColor()
                if color.isValid():
                        self.lbl.setStyleSheet('color:{}'.format(color.name()))

                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=LabelSettingsWindow()
        sys.exit(app.exec_())
   

    

