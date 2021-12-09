# Keypad
# Section 6-14
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator
from KeyPad_Gui import Ui_KeyPad

class KeypadGUI(QtWidgets.QWidget):
        def __init__(self):
                super(KeypadGUI, self).__init__()
                self.ui = Ui_KeyPad()
                self.ui.setupUi(self)
                self.initializeUI()
                self.show()
                
        def initializeUI(self):

                self.ui.in1.setMaxLength(1) 
                self.ui.in1.setValidator(QIntValidator(0, 9)) 
                self.ui.in1.setFocusPolicy(QtCore.Qt.NoFocus) 
                self.ui.in2.setMaxLength(1)
                self.ui.in2.setValidator(QIntValidator(0, 9))
                self.ui.in2.setFocusPolicy(QtCore.Qt.NoFocus)
                self.ui.in3.setMaxLength(1)
                self.ui.in3.setValidator(QIntValidator(0, 9))
                self.ui.in3.setFocusPolicy(QtCore.Qt.NoFocus)
                self.ui.in4.setMaxLength(1)
                self.ui.in4.setValidator(QIntValidator(0, 9))
                self.ui.in4.setFocusPolicy(QtCore.Qt.NoFocus)

                self.passcode = 8894

                self.ui.P0.clicked.connect(lambda: self.numberClicked(self.ui.P0.text()))
                self.ui.P1.clicked.connect(lambda: self.numberClicked(self.ui.P1.text()))
                self.ui.P2.clicked.connect(lambda: self.numberClicked(self.ui.P2.text()))
                self.ui.P3.clicked.connect(lambda: self.numberClicked(self.ui.P3.text()))
                self.ui.P4.clicked.connect(lambda: self.numberClicked(self.ui.P4.text()))
                self.ui.P5.clicked.connect(lambda: self.numberClicked(self.ui.P5.text()))
                self.ui.P6.clicked.connect(lambda: self.numberClicked(self.ui.P6.text()))
                self.ui.P7.clicked.connect(lambda: self.numberClicked(self.ui.P7.text()))
                self.ui.P8.clicked.connect(lambda: self.numberClicked(self.ui.P8.text()))
                self.ui.P9.clicked.connect(lambda: self.numberClicked(self.ui.P9.text()))
                self.ui.PE.clicked.connect(self.checkPasscode)

        def numberClicked(self, text_value):
                if self.ui.in1.text() == '':
                        self.ui.in1.setFocus()
                        self.ui.in1.setText(text_value)
                        self.ui.in1.repaint()
                elif (self.ui.in1.text() != '') and (self.ui.in2.text() == ''):
                        self.ui.in2.setFocus()
                        self.ui.in2.setText(text_value)
                        self.ui.in2.repaint()
                elif (self.ui.in1.text() != '') and (self.ui.in2.text() != '') and (self.ui.in3.text() == ''):
                        self.ui.in3.setFocus()
                        self.ui.in3.setText(text_value)
                        self.ui.in3.repaint()
                elif (self.ui.in1.text() != '') and (self.ui.in2.text() != '') and (self.ui.in3.text() != '') and (self.ui.in4.text() == ''):
                        self.ui.in4.setFocus()
                        self.ui.in4.setText(text_value)
                        self.ui.in4.repaint()
        def checkPasscode(self):

                entered_passcode = self.ui.in1.text() + self.ui.in2.text() + self.ui.in3.text() + self.ui.in4.text()
                if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
                        QMessageBox.information(self, 'Message', 'Valid Passcode!', QMessageBox.Ok, QMessageBox.Ok)
                        self.close()
                else:
                        QMessageBox.warning(self, 'Message', 'Invalid Passcode.', QMessageBox.Close, QMessageBox.Close)
                        self.ui.in1.clear()
                        self.ui.in2.clear()
                        self.ui.in3.clear()
                        self.ui.in4.clear()
                        self.ui.in1.setFocus()


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Keypad = KeypadGUI()
        sys.exit(app.exec_())
