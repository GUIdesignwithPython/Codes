# Word Processor
# Section 8-2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QStatusBar, QMessageBox, QTextEdit, QFileDialog, QInputDialog, QFontDialog,QColorDialog, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt, QSize
class WordProcessor(QMainWindow):
        def __init__(self):
                super().__init__()
                self.initializeUI()
        def initializeUI(self):
                self.setGeometry(100, 100, 700, 600)
                self.setWindowTitle('Simple Word Processor')
                self.setWindowIcon(QIcon('word.png'))
                self.createWordProcessingWidget()
                self.createMenu()
                self.createStatusBar()
                self.createToolBar()
                self.show()
        def createWordProcessingWidget(self):
                self.text_field = QTextEdit()
                self.text_field.textChanged.connect(self.textChanged)
                self.setCentralWidget(self.text_field)

        def createMenu(self):
                self.new_act = QAction(QIcon('new.png'), 'New', self)
                self.new_act.setShortcut('Ctrl+N')
                self.new_act.setToolTip('New Blank Document')
                self.new_act.triggered.connect(self.clearText)
                self.open_act = QAction(QIcon('open_file.png'), 'Open', self)
                self.open_act.setToolTip('Open Old Document')
                self.open_act.setShortcut('Ctrl+O')
                self.open_act.triggered.connect(self.openFile)
                self.save_act = QAction(QIcon('save_file.png'), 'Save', self)
                self.save_act.setToolTip('Save Document')
                self.save_act.setShortcut('Ctrl+S')
                self.save_act.triggered.connect(self.saveToFile)
                self.exit_act = QAction(QIcon('exit.png'), 'Exit', self)
                self.exit_act.setShortcut('Ctrl+Q')
                self.exit_act.triggered.connect(self.close)
                self.undo_act = QAction(QIcon('undo.png'),'Undo', self)
                self.undo_act.setToolTip('Undo')
                self.undo_act.setShortcut('Ctrl+Z')
                self.undo_act.triggered.connect(self.text_field.undo)
                self.redo_act = QAction(QIcon('redo.png'),'Redo', self)
                self.redo_act.setToolTip('Redo')
                self.redo_act.setShortcut('Ctrl+Shift+Z')
                self.redo_act.triggered.connect(self.text_field.redo)
                self.cut_act = QAction(QIcon('cut.png'),'Cut', self)
                self.cut_act.setToolTip('Cut')
                self.cut_act.setShortcut('Ctrl+X')
                self.cut_act.triggered.connect(self.text_field.cut)
                self.copy_act = QAction(QIcon('copy.png'),'Copy', self)
                self.copy_act.setToolTip('Copy')
                self.copy_act.setShortcut('Ctrl+C')
                self.copy_act.triggered.connect(self.text_field.copy)
                self.paste_act = QAction(QIcon('paste.png'),'Paste', self)
                self.paste_act.setToolTip('Paste')
                self.paste_act.setShortcut('Ctrl+V')
                self.paste_act.triggered.connect(self.text_field.paste)
                self.find_act = QAction(QIcon('find.png'), 'Find', self)
                self.find_act.setShortcut('Ctrl+F')
                self.find_act.triggered.connect(self.findTextDialog)
                self.font_act = QAction(QIcon('font.png'), 'Font', self)
                self.font_act.setToolTip('Choose Font')
                self.font_act.setShortcut('Ctrl+T')
                self.font_act.triggered.connect(self.chooseFont)
                self.color_act = QAction(QIcon('colors.png'), 'Color', self)
                self.color_act.setToolTip('Choose Color')
                self.color_act.setShortcut('Ctrl+Shift+C')
                self.color_act.triggered.connect(self.chooseFontColor)
                self.highlight_act = QAction(QIcon('highlight.png'), 'Highlight', self)
                self.highlight_act.setToolTip('Choose Highlight Color')
                self.highlight_act.setShortcut('Ctrl+Shift+H')
                self.highlight_act.triggered.connect(self.chooseFontBackgroundColor)
                self.about_act = QAction(QIcon('about.png'),'About', self)
                self.about_act.triggered.connect(self.aboutDialog)
                menu_bar = self.menuBar()
                menu_bar.setStyleSheet('font-size:15px')
                menu_bar.setNativeMenuBar(False)
                file_menu = menu_bar.addMenu('File')
                file_menu.addAction(self.new_act)
                file_menu.addSeparator()
                file_menu.addAction(self.open_act)
                file_menu.addAction(self.save_act)
                file_menu.addSeparator()
                file_menu.addAction(self.exit_act)
                edit_menu = menu_bar.addMenu('Edit')
                edit_menu.addAction(self.undo_act)
                edit_menu.addAction(self.redo_act)
                edit_menu.addSeparator()
                edit_menu.addAction(self.cut_act)
                edit_menu.addAction(self.copy_act)
                edit_menu.addAction(self.paste_act)
                edit_menu.addSeparator()
                edit_menu.addAction(self.find_act)
                settings_menu = menu_bar.addMenu('Settings')
                settings_menu.addAction(self.font_act)
                settings_menu.addAction(self.color_act)
                settings_menu.addAction(self.highlight_act)
                help_menu = menu_bar.addMenu('Help')
                help_menu.addAction(self.about_act)

        def createStatusBar(self):
                self.status_bar_message=QLabel()
                self.status_bar_message.setStyleSheet('border:1px solid gray; border-radius:2px; color:red')
                self.counts=QLabel()
                self.status_bar=QStatusBar()
                self.setStatusBar(self.status_bar)

        def createToolBar(self):
                tool_bar=QToolBar(self)
                tool_bar.setStyleSheet('font-size: 17px; padding:5px')
                tool_bar.setIconSize(QSize(24, 24))

                self.addToolBar(Qt.TopToolBarArea, tool_bar)
                tool_bar.setMovable(False)

                self.findtext=QLineEdit(self)

                tool_bar.addAction(self.new_act)
                tool_bar.addAction(self.open_act)
                tool_bar.addAction(self.save_act)
                tool_bar.addSeparator()
                tool_bar.addAction(self.undo_act)
                tool_bar.addAction(self.redo_act)
                tool_bar.addSeparator()
                tool_bar.addAction(self.cut_act)
                tool_bar.addAction(self.copy_act)
                tool_bar.addAction(self.paste_act)
                tool_bar.addSeparator()
                tool_bar.addAction(self.font_act)
                tool_bar.addAction(self.color_act)
                tool_bar.addAction(self.highlight_act)
                tool_bar.addSeparator()
                tool_bar.addWidget(QLabel('Find:'))
                tool_bar.addWidget(self.findtext)
                tool_bar.addAction(self.find_act)
                tool_bar.addSeparator()
                tool_bar.addAction(self.about_act)

        def openFile(self):
                file_name, _ = QFileDialog.getOpenFileName(self, 'Open File','', 'HTML Files (*.html);;Text Files (*.txt)')
                if file_name:
                        with open(file_name, 'r') as f:
                                notepad_text = f.read()
                        self.text_field.setText(notepad_text)
                else:
                        QMessageBox.information(self, 'Error','Unable to open file.', QMessageBox.Ok)
        def saveToFile(self):
                file_name, _ = QFileDialog.getSaveFileName(self, 'Save File','','HTML Files (*.html);;Text Files (*.txt)')
                
                if file_name.endswith('.txt'):
                        notepad_text = self.text_field.toPlainText()
                        with open(file_name, 'w') as f:
                                f.write(notepad_text)
                        self.status_bar_message.setText('File is saved.')
                        self.status_bar.addWidget(self.status_bar_message)
                elif file_name.endswith('.html'):
                        notepad_richtext = self.text_field.toHtml()
                        with open(file_name, 'w') as f:
                                f.write(notepad_richtext)
                        self.status_bar_message.setText('File is saved.')
                        self.status_bar.addWidget(self.status_bar_message)
                else:
                        QMessageBox.information(self, 'Error','Unable to save file.', QMessageBox.Ok)
                        
        def clearText(self):
                answer = QMessageBox.question(self, 'Clear Text','Do you want to clear the text?', QMessageBox.No | QMessageBox.Yes,QMessageBox.Yes)
                if answer == QMessageBox.Yes:
                        self.text_field.clear()


        def findTextDialog(self):
                if self.findtext.text()=='':
                        find_text, ok = QInputDialog.getText(self, 'Search Text', 'Find:')
                else:
                        find_text=self.findtext.text()
                        ok=True
                extra_selections = []
                if ok and not self.text_field.isReadOnly():
                        self.text_field.moveCursor(QTextCursor.Start)
                        color = QColor(Qt.yellow)
                        while(self.text_field.find(find_text)):
                                selection = QTextEdit.ExtraSelection()
                                selection.format.setBackground(color)
                                selection.cursor = self.text_field.textCursor()
                                extra_selections.append(selection)
                for i in extra_selections:
                                self.text_field.setExtraSelections(extra_selections)
                
        def textChanged(self):
                text=self.text_field.toPlainText()
                words=len(text.split())
                self.counts.setText('Number of Words: '+str(words) + '  -  Number of Characters: '+str(len(text))+'      ')
                self.status_bar_message.setText('File is not saved.')
                self.status_bar.addWidget(self.counts)
                self.status_bar.addWidget(self.status_bar_message)
                        
        def chooseFont(self):
                current = self.text_field.currentFont()
                font, ok = QFontDialog.getFont(current, self, options=QFontDialog.DontUseNativeDialog)
                if ok:
                        self.text_field.setCurrentFont(font) 


        def chooseFontColor(self):
                color = QColorDialog.getColor()
                if color.isValid():
                        self.text_field.setTextColor(color)

        def chooseFontBackgroundColor(self):
                color = QColorDialog.getColor()
                if color.isValid():
                        self.text_field.setTextBackgroundColor(color)

        def aboutDialog(self):

                QMessageBox.information(self, 'About', 'Simple Word Processor Software \n\n with Python and PyQt5')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = WordProcessor()
        sys.exit(app.exec_())
