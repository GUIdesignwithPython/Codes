# Simple Paint Software
# Section 7-6
import os, sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QToolBar, QStatusBar, QToolTip, QColorDialog, QFileDialog, QComboBox, QMessageBox, QSlider
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QIcon, QFont
from PyQt5.QtCore import  Qt, QSize, QPoint, QRect

class Canvas(QLabel):
        def __init__(self, parent):
                super().__init__(parent)
                width, height = 900, 600
                self.parent = parent
                self.parent.setFixedSize(width, height)
                pixmap = QPixmap(width, height) 
                pixmap.fill(Qt.white)
                self.setPixmap(pixmap)
                self.mouse_track_label = QLabel()
                self.setMouseTracking(True)

                self.antialiasing_status = False
                self.eraser_selected = False
                self.last_mouse_pos = QPoint()  
                self.drawing = False
                self.pen_color = Qt.black
                self.pen_width = 2
                self.pen_cap=Qt.SquareCap
                self.pen_style=Qt.SolidLine
        def selectDrawingTool(self, tool):

                if tool == 'square':
                        self.eraser_selected = False
                        self.pen_cap=Qt.SquareCap
                elif tool == 'round':
                        self.eraser_selected = False
                        self.pen_cap=Qt.RoundCap
                elif tool == 'eraser':
                        self.eraser_selected = True

                elif tool == 'color':
                        self.eraser_selected = False
                        color = QColorDialog.getColor()
                        if color.isValid():
                                self.pen_color = color
        def mouseMoveEvent(self, event):
      
                mouse_pos = event.pos()
                if (event.buttons() and Qt.LeftButton) and self.drawing:
                        self.mouse_pos = event.pos()
                        self.drawOnCanvas(mouse_pos)
                self.mouse_track_label.setVisible(True)
                sb_text = 'Mouse Coordinates: ({}, {})'.format(mouse_pos.x(),mouse_pos.y())
                self.mouse_track_label.setText(sb_text)
                self.parent.status_bar.addWidget(self.mouse_track_label)

        def drawOnCanvas(self, points):

                painter = QPainter(self.pixmap())
                if self.antialiasing_status:
                        painter.setRenderHint(QPainter.Antialiasing)
                if self.eraser_selected == False:
                        pen = QPen(QColor(self.pen_color), self.pen_width)
                        pen.setCapStyle(self.pen_cap)
                        pen.setStyle(self.pen_style)
                        painter.setPen(pen)
                        painter.drawLine(self.last_mouse_pos, points)
                        self.last_mouse_pos = points
                elif self.eraser_selected == True:
                        eraser = QRect(points.x(), points.y(), self.pen_width, self.pen_width)
                        painter.eraseRect(eraser)
                        painter.end()
                self.update()

        def newCanvas(self):

                self.pixmap().fill(Qt.white)
                self.update()
        def saveFile(self):

                file_format = 'png'
                default_name = os.path.curdir + '/untitled.' + file_format
                file_name, _ = QFileDialog.getSaveFileName(self, 'Save As',default_name, 'PNG Format (*.png)')
                if file_name:
                        self.pixmap().save(file_name, file_format)
        def mousePressEvent(self, event):

                if event.button() == Qt.LeftButton:
                        self.last_mouse_pos = event.pos()
                        self.drawing = True
        def mouseReleaseEvent(self, event):

                if event.button() == Qt.LeftButton:
                        self.drawing = False
                elif self.eraser_selected == True:
                        self.eraser_selected = False
        def paintEvent(self, event):

                painter = QPainter(self)
                target_rect = QRect()
                target_rect = event.rect()
                painter.drawPixmap(target_rect, self.pixmap(), target_rect)

class PainterWindow(QMainWindow):
        def __init__(self):
                super().__init__()
                self.initializeUI()
        def initializeUI(self):
                 self.setWindowTitle('Simple Paint')
                 QToolTip.setFont(QFont('Helvetica', 12))
                 self.setWindowIcon(QIcon('paint.png'))
                 self.createCanvas()
                 self.createMenu()
                 self.createToolbar()
                 self.show()

        def createCanvas(self):

                self.canvas = Canvas(self)
                self.setCentralWidget(self.canvas)

        def createMenu(self):

                self.new_act = QAction(QIcon('new.png'),'New', self)
                self.new_act.setShortcut('Ctrl+N')
                self.new_act.triggered.connect(self.canvas.newCanvas)
                self.save_file_act = QAction(QIcon('save_file.png'),'Save File', self)
                self.save_file_act.setShortcut('Ctrl+S')
                self.save_file_act.triggered.connect(self.canvas.saveFile)
                quit_act = QAction('Quit', self)
                quit_act.setShortcut('Ctrl+Q')
                quit_act.triggered.connect(self.close)

                anti_al_act = QAction('AntiAliasing', self, checkable=True)
                anti_al_act.triggered.connect(self.turnAntialiasingOn)

                menu_bar = self.menuBar()
                menu_bar.setStyleSheet('font-size:15px')
                menu_bar.setNativeMenuBar(False)

                file_menu = menu_bar.addMenu('File')
                file_menu.addAction(self.new_act)
                file_menu.addAction(self.save_file_act)
                file_menu.addSeparator()
                file_menu.addAction(quit_act)

                setting_menu = menu_bar.addMenu('Settings')
                setting_menu.addAction(anti_al_act)

                about_menu=menu_bar.addMenu('About')
                about_act=QAction('About Paint', self)
                about_act.triggered.connect(self.About)
                about_menu.addAction(about_act)
                
                self.status_bar = QStatusBar()
                self.setStatusBar(self.status_bar)
        def createToolbar(self):

                tool_bar = QToolBar('Painting Toolbar')
                tool_bar.setStyleSheet('font-size: 17px; padding:5px')
                tool_bar.setIconSize(QSize(24, 24))

                self.addToolBar(Qt.TopToolBarArea, tool_bar)
                tool_bar.setMovable(False)

                pencil_act = QAction(QIcon('square.png'), 'Square Pen', tool_bar)
                pencil_act.setToolTip('<b>Square Pen</b>')
                pencil_act.triggered.connect(lambda: self.canvas.selectDrawingTool('square'))
                marker_act = QAction(QIcon('round.png'), 'Round Pen', tool_bar)
                marker_act.setToolTip('<b>Round Pen</b>')
                marker_act.triggered.connect(lambda: self.canvas.selectDrawingTool('round'))
                eraser_act = QAction(QIcon('eraser.png'), 'Eraser', tool_bar)
                eraser_act.setToolTip('<b>Eraser</b>')
                eraser_act.triggered.connect(lambda: self.canvas.selectDrawingTool('eraser'))

                color_act = QAction(QIcon('colors.png'), 'Colors', tool_bar)
                color_act.setToolTip('Choose a <b>Color</b> from the Color dialog.')
                color_act.triggered.connect(lambda: self.canvas.selectDrawingTool('color'))

                self.current_pen_size=QLabel(self)
                self.current_pen_size.setText('2')

                pen_size=QSlider(Qt.Horizontal,self)
                pen_size.setStyleSheet('height:5px;border-radius:4px')              
                pen_size.setToolTip('Select Pen Size')
                pen_size.setTickInterval(1)
                pen_size.setMinimum(1)
                pen_size.setMaximum(20)
                pen_size.valueChanged['int'].connect(self.PenSizeChange)
                
                pen_style=QComboBox(self)
                pen_style.setToolTip('Select Line Style')
                pen_style.setIconSize(QSize(120,30))
                pen_style.addItem('Solid')
                pen_style.setItemIcon(0,QIcon('solid.png'))
                pen_style.addItem('Dash')
                pen_style.setItemIcon(1,QIcon('dash.png'))
                pen_style.addItem('Dot')
                pen_style.setItemIcon(2,QIcon('dot.png'))
                pen_style.addItem('DashDot')
                pen_style.setItemIcon(3,QIcon('dashdot.png'))

                pen_style.activated[str].connect(self.PenStyleChange)
                
                tool_bar.addAction(self.new_act)
                tool_bar.addAction(self.save_file_act)
                tool_bar.addSeparator()
                tool_bar.addAction(pencil_act)
                tool_bar.addAction(marker_act)
                tool_bar.addAction(eraser_act)
                tool_bar.addAction(color_act)
                tool_bar.addSeparator()
                tool_bar.addWidget(QLabel('Style:'))
                tool_bar.addWidget(pen_style)
                tool_bar.addSeparator()
                tool_bar.addWidget(QLabel('Size:'))
                tool_bar.addWidget(self.current_pen_size)
                tool_bar.addWidget(pen_size)
                
        def PenSizeChange(self, text):
                self.canvas.pen_width=int(text)
                self.current_pen_size.setText(str(text))
                
        def PenStyleChange(self, text):
                if text=='Solid':
                        self.canvas.pen_style=Qt.SolidLine
                elif text=='Dash':
                        self.canvas.pen_style=Qt.DashLine
                elif text=='Dot':
                        self.canvas.pen_style=Qt.DotLine
                elif text=='DashDot':
                        self.canvas.pen_style=Qt.DashDotLine

        def About(self):
                QMessageBox.information(self, 'Simple Paint', 'Simple Paint with Python and PyQt5', QMessageBox.Ok, QMessageBox.Ok)

                
        def turnAntialiasingOn(self, state):

                if state:
                        self.canvas.antialiasing_status = True
                else:
                        self.canvas.antialiasing_status = False
        def leaveEvent(self, event):
                self.canvas.mouse_track_label.setVisible(False)

if __name__ == '__main__':
                app = QApplication(sys.argv)
                app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
                window = PainterWindow()
                sys.exit(app.exec_())
