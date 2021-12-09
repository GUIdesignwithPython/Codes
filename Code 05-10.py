# Photo Editor
# Section 5-7
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QAction, QFileDialog, QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar, QDockWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class PhotoEditor(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setFixedSize(600, 500)
                self.setWindowTitle('Photo Editor')
                self.setWindowIcon(QIcon('photo_editor.png'))
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.MainWindow()
                self.ToolsDockWidget()
                self.Menu()
                self.ToolBar()
                self.Widgets()


        def MainWindow(self):
                 desktop = QDesktopWidget().screenGeometry()
                 screen_width = desktop.width()
                 screen_height = desktop.height()
                 x=int((screen_width - self.width()) / 2)
                 y=int((screen_height - self.height()) / 2)
                 self.move(x, y)

        def ToolsDockWidget(self):
                 self.dock_tools_view = QDockWidget()
                 self.dock_tools_view.setWindowTitle('Edit Image Tools')
                 self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

                 self.tools_contents = QWidget()

                 self.rotate90 = QPushButton('Rotate 90°')
                 self.rotate90.setMinimumSize(QSize(130, 40))
                 self.rotate90.setStatusTip('Rotate image 90° clockwise')
                 self.rotate90.clicked.connect(self.rotateImage90)
                 self.rotate180 = QPushButton('Rotate 180°')
                 self.rotate180.setMinimumSize(QSize(130, 40))
                 self.rotate180.setStatusTip('Rotate image 180° clockwise')
                 self.rotate180.clicked.connect(self.rotateImage180)
                 self.flip_horizontal = QPushButton('Flip Horizontal')
                 self.flip_horizontal.setMinimumSize(QSize(130, 40))
                 self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
                 self.flip_horizontal.clicked.connect(self.flipImageHorizontal)
                 self.flip_vertical = QPushButton('Flip Vertical')
                 self.flip_vertical.setMinimumSize(QSize(130, 40))
                 self.flip_vertical.setStatusTip('Flip image across vertical axis')
                 self.flip_vertical.clicked.connect(self.flipImageVertical)
                 self.resize = QPushButton('Resize')
                 self.resize.setMinimumSize(QSize(130, 40))
                 self.resize.setStatusTip('Resize image based on a percentage of the original size')
                 self.resize.clicked.connect(self.resizeImage)
                 self.r_h_lbl=QLabel('Horizontal')
                 self.resize_value_h=QLineEdit()
                 self.resize_value_h.setInputMask('000')
                 self.resize_value_h.setAlignment(Qt.AlignCenter)
                 self.resize_value_h.setText('100')
                 self.r_v_lbl=QLabel('Vertical')
                 self.resize_value_v=QLineEdit()
                 self.resize_value_v.setInputMask('000')
                 self.resize_value_v.setAlignment(Qt.AlignCenter)
                 self.resize_value_v.setText('100')

                 dock_v_box = QVBoxLayout()
                 dock_v_box.addWidget(self.rotate90)
                 dock_v_box.addWidget(self.rotate180)
                 dock_v_box.addStretch(1)
                 dock_v_box.addWidget(self.flip_horizontal)
                 dock_v_box.addWidget(self.flip_vertical)
                 dock_v_box.addStretch(1)
                 dock_v_box.addWidget(self.resize)
                 dock_v_box.addWidget(self.r_h_lbl)
                 dock_v_box.addWidget(self.resize_value_h)
                 dock_v_box.addWidget(self.r_v_lbl)
                 dock_v_box.addWidget(self.resize_value_v)
                 dock_v_box.addStretch(6)

                 self.tools_contents.setLayout(dock_v_box)
                 self.dock_tools_view.setWidget(self.tools_contents)

                 self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)

                 self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()                 


        def Menu(self):


                 self.open_act = QAction(QIcon('open_file.png'),'Open', self)
                 self.open_act.setShortcut('Ctrl+O')
                 self.open_act.setStatusTip('Open a new image')
                 self.open_act.triggered.connect(self.openImage)
                 self.save_act = QAction(QIcon('save_file.png'),'Save', self)
                 self.save_act.setShortcut('Ctrl+S')
                 self.save_act.setStatusTip('Save image')
                 self.save_act.triggered.connect(self.saveImage)
                 self.print_act = QAction(QIcon('print.png'), 'Print', self)
                 self.print_act.setShortcut('Ctrl+P')
                 self.print_act.setStatusTip('Print image')
                 self.print_act.triggered.connect(self.printImage)
                 self.print_act.setEnabled(False)
                 self.exit_act = QAction(QIcon('exit.png'), 'Exit', self)
                 self.exit_act.setShortcut('Ctrl+Q')
                 self.exit_act.setStatusTip('Quit program')
                 self.exit_act.triggered.connect(self.close)

                 self.rotate90_act = QAction('Rotate 90°', self)
                 self.rotate90_act.setStatusTip('Rotate image 90° clockwise')
                 self.rotate90_act.triggered.connect(self.rotateImage90)
                 self.rotate180_act = QAction('Rotate 180°', self)
                 self.rotate180_act.setStatusTip('Rotate image 180° clockwise')
                 self.rotate180_act.triggered.connect(self.rotateImage180)
                 self.flip_hor_act = QAction('Flip Horizontal', self)
                 self.flip_hor_act.setStatusTip('Flip image across horizontal axis')
                 self.flip_hor_act.triggered.connect(self.flipImageHorizontal)
                 self.flip_ver_act = QAction('Flip Vertical', self)
                 self.flip_ver_act.setStatusTip('Flip image across vertical axis')
                 self.flip_ver_act.triggered.connect(self.flipImageVertical)
                 self.resize_act = QAction('Resize', self)
                 self.resize_act.setStatusTip('Resize image based on a percentage of the original size')
                 self.resize_act.triggered.connect(self.resizeImage)
                 self.clear_act = QAction(QIcon('clear.png'), 'Clear Image', self)
                 self.clear_act.setShortcut('Ctrl+D')
                 self.clear_act.setStatusTip('Clear the current image')
                 self.clear_act.triggered.connect(self.clearImage)

                 menu_bar = self.menuBar()
                 file_menu = menu_bar.addMenu('File')
                 file_menu.addAction(self.open_act)
                 file_menu.addAction(self.save_act)
                 file_menu.addSeparator()
                 file_menu.addAction(self.print_act)
                 file_menu.addSeparator()
                 file_menu.addAction(self.exit_act)

                 edit_menu = menu_bar.addMenu('Edit')
                 edit_menu.addAction(self.rotate90_act)
                 edit_menu.addAction(self.rotate180_act)
                 edit_menu.addSeparator()
                 edit_menu.addAction(self.flip_hor_act)
                 edit_menu.addAction(self.flip_ver_act)
                 edit_menu.addSeparator()
                 edit_menu.addAction(self.resize_act)
                 edit_menu.addSeparator()
                 edit_menu.addAction(self.clear_act)

                 view_menu = menu_bar.addMenu('View')
                 view_menu.addAction(self.toggle_dock_tools_act)

                 self.setStatusBar(QStatusBar(self))


                 
        def ToolBar(self):
                 tool_bar = QToolBar('Photo Editor Toolbar')
                 tool_bar.setIconSize(QSize(24,24))
                 self.addToolBar(tool_bar)

                 tool_bar.addAction(self.open_act)
                 tool_bar.addAction(self.save_act)
                 tool_bar.addAction(self.print_act)
                 tool_bar.addAction(self.clear_act)
                 tool_bar.addSeparator()
                 tool_bar.addAction(self.exit_act)


        def Widgets(self):

                 self.image = QPixmap()
                 self.image_label = QLabel()
                 self.image_label.setAlignment(Qt.AlignCenter)

                 self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
                 self.setCentralWidget(self.image_label)

        def openImage(self):
                 image_file, _ = QFileDialog.getOpenFileName(self, 'Open Image', '','JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files(*.bmp);;GIF Files (*.gif)')
                 if image_file:
                         self.image = QPixmap(image_file)
                         self.image_label.setPixmap(self.image.scaled(self.image_label.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation))
                         self.print_act.setEnabled(True)

                 else:
                         QMessageBox.information(self, 'Error','Unable to open image.', QMessageBox.Ok)


        def saveImage(self):
                 image_file, _ = QFileDialog.getSaveFileName(self, 'Save Image', '','JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);; GIF Files (*.gif)')
                 if image_file and self.image.isNull() == False:
                         self.image.save(image_file)
                 else:
                         QMessageBox.information(self, 'Error', 'Unable to save image.', QMessageBox.Ok)

        def printImage(self):

                 printer = QPrinter()
                 printer.setOutputFormat(QPrinter.NativeFormat)
                 print_dialog = QPrintDialog(printer)
                 if (print_dialog.exec_() == QPrintDialog.Accepted):
                         painter = QPainter()
                         painter.begin(printer)
                         rect = QRect(painter.viewport())
                         size = QSize(self.image_label.pixmap().size())
                         size.scale(rect.size(), Qt.KeepAspectRatio)
                         painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
                         painter.setWindow(self.image_label.pixmap().rect())
                         painter.drawPixmap(0, 0, self.image_label.pixmap())
                         painter.end()

        def clearImage(self):
                 self.image_label.clear()
                 self.image = QPixmap() 

        def rotateImage90(self):
                 if self.image.isNull() == False:
                         transform90 = QTransform().rotate(90)
                         pixmap = QPixmap(self.image)
                         rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)
                         self.image_label.setPixmap(rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                         self.image = QPixmap(rotated)
                         self.image_label.repaint() 


        def rotateImage180(self):
                 if self.image.isNull() == False:
                         transform180 = QTransform().rotate(180)
                         pixmap = QPixmap(self.image)
                         rotated = pixmap.transformed(transform180, mode=Qt.SmoothTransformation)
                         self.image_label.setPixmap(rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                         self.image = QPixmap(rotated)
                         self.image_label.repaint() 


        def flipImageHorizontal(self):
                 if self.image.isNull() == False:
                         flip_h = QTransform().scale(-1, 1)
                         pixmap = QPixmap(self.image)
                         flipped = pixmap.transformed(flip_h)
                         self.image_label.setPixmap(flipped.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                         self.image = QPixmap(flipped)
                         self.image_label.repaint()


        def flipImageVertical(self):
                 if self.image.isNull() == False:
                         flip_v = QTransform().scale(1, -1)
                         pixmap = QPixmap(self.image)
                         flipped = pixmap.transformed(flip_v)
                         self.image_label.setPixmap(flipped.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                         self.image = QPixmap(flipped)
                         self.image_label.repaint()


        def resizeImage(self):
                h=int(self.resize_value_h.text())
                v=int(self.resize_value_v.text())
                if 0<h<=100 and 0<v<=100:
                        if self.image.isNull() == False:
                                resize = QTransform().scale(h/100, v/100)
                                pixmap = QPixmap(self.image)
                                resized = pixmap.transformed(resize)
                                self.image_label.setPixmap(resized.scaled(self.image_label.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation))
                                self.image = QPixmap(resized)
                                self.image_label.repaint()

         
if __name__=='__main__':
        app=QApplication(sys.argv)
        app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
        window=PhotoEditor()
        sys.exit(app.exec_())
   

    

