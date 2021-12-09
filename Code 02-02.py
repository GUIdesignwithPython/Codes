# Window With Labels
# Section 2-3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class LabelWindow(QWidget):
        def __init__(self):
                super().__init__()      
                self.initUI()           
        def initUI(self):
                self.setGeometry(200,250,300,250)
                self.setWindowTitle('Window with Labels')
                self.displayLabels()
                self.show()
        def displayLabels(self):
                lbl_text=QLabel(self)
                lbl_text.setText('Hello World!')
                lbl_text.move(135,35)

                image='python.png'
                try:
                        with open(image):
                                lbl_image=QLabel(self)
                                pix_image=QPixmap(image)
                                lbl_image.setPixmap(pix_image)
                                lbl_image.move(60,55)
                except FileNotFoundError:
                        print('Image not found.')

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=LabelWindow()
        sys.exit(app.exec_())

   

    

