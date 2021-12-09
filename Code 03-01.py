# Simple Notepad
# Section 3-2
import sys      
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QFileDialog, QMessageBox

class Notepad(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,340,380)
                self.setWindowTitle('Simple Notepad')
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.new_button=QPushButton('New',self)
                self.new_button.move(20,20)
                self.new_button.clicked.connect(self.cleartext)

                self.save_button=QPushButton('Save',self)
                self.save_button.move(100,20)
                self.save_button.clicked.connect(self.savetext)

                self.text=QTextEdit(self)
                self.text.move(20,50)
                self.text.resize(300,300)


        def cleartext(self):
                result=QMessageBox.question(self,'New Note','Are you sure to clear the text?',QMessageBox.No | QMessageBox.Yes,QMessageBox.Yes)
                if result==QMessageBox.Yes:
                        self.text.clear()


        def savetext(self):
                #opts=QFileDialog.Options()
                opts=QFileDialog.DontUseNativeDialog                
                plaintext=self.text.toPlainText()
                #file_name=QFileDialog.getOpenFileName(self, 'Open File','c:\\GUI Python','Image Fie111ls (*.png);;Text Files (*.txt)')
                file, _ =QFileDialog.getSaveFileName(self,'Save File','', 'All Files(*);;Text Files (*.txt)',options=opts)
                if file:
                        with open(file,'w') as f:
                                f.write(plaintext)
                
if __name__=='__main__':
        app=QApplication(sys.argv)
        window=Notepad()
        sys.exit(app.exec_())
   

    

