# Context Menu
# Section 5-2
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,QMenu

class ContextMenu(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,300)
                self.setWindowTitle('Context Menu Example')
                self.show()

        def contextMenuEvent(self, event):
                contextMenu = QMenu(self)
                newAct = contextMenu.addAction('New')
                openAct = contextMenu.addAction('Open')
                exitAct = contextMenu.addAction('Exit')
                action = contextMenu.exec_(self.mapToGlobal(event.pos()))
                if action == exitAct:
                    self.close()



if __name__=='__main__':
        app=QApplication(sys.argv)
        window=ContextMenu()
        sys.exit(app.exec_())
   

    

