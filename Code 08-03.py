# Persian Calendar and Time
# Section 8-4
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt5.QtCore import Qt, QDate, QTime, QTimer
from PyQt5.QtGui import QIcon
from persiantools.jdatetime import JalaliDate
import persian
from jcalendar import calendar

Style_Sheet='''
        QLabel{color: black; font: 20px b titr}
        QLabel#TimeLabel{border-color: black;
                        border-width: 4px;
                        border-style: solid;
                        border-radius: 7px;
                        font: 50px b koodak}
        QPushButton{font:30px consolas; font-weight: bold}
            '''

Persian_Months={
        1:'فروردين',
        2:'ارديبهشت',
        3:'خرداد',
        4:'تير',
        5:'مرداد',
        6:'شهريور',
        7:'مهر',
        8:'آبان',
        9:'آذر',
        10:'دي',
        11:'بهمن',
        12:'اسفند'
        }
Persian_Months_English={
        'Farvardin':'فروردين',
        'Ordibehesht':'ارديبهشت',
        'Khordad':'خرداد',
        'Tir':'تير',
        'Mordad':'مرداد',
        'Shahrivar':'شهريور',
        'Mehr':'مهر',
        'Aban':'آبان',
        'Azar':'آذر',
        'Dey':'دي',
        'Bahman':'بهمن',
        'Esfand':'اسفند'
        }


class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                self.initializeUI()
        def initializeUI(self):
                self.setGeometry(100, 100, 400, 100)
                self.setWindowTitle(persian.convert_ar_characters('تقويم و ساعت فارسي'))
                self.setWindowIcon(QIcon('clock.png'))
                self.setStyleSheet('background-color: skyblue')
                self.setupWidgets()

                timer = QTimer(self)
                timer.timeout.connect(self.updateDateTime)
                timer.start(1000)

                self.show()
        def setupWidgets(self):
                current_date=QDate.currentDate()
                self.jalali=JalaliDate.to_jalali(current_date.year(), current_date.month(), current_date.day())
                current_time = QTime.currentTime().toString('hh:mm:ss')
                self.today=QLabel('امروز')
                self.day=QLabel()
                self.day.setText(persian.convert_en_numbers(str(self.jalali.day)))
                self.month=QLabel()
                self.month.setText(persian.convert_ar_characters(Persian_Months[self.jalali.month]))
                self.year=QLabel()
                self.year.setText(persian.convert_en_numbers(str(self.jalali.year)))
                self.hejri=QLabel(persian.convert_ar_characters('هجري خورشيدي'))
                self.time=QLabel()
                self.time.setObjectName('TimeLabel')
                self.time.setText(persian.convert_en_numbers(current_time))

                self.cYear=self.jalali.year
                self.cMonth=self.jalali.month

                self.top_grid_row=QHBoxLayout()
                nyear=QPushButton('<<  ')
                nyear.setFlat(True)
                nyear.clicked.connect(self.nextYear)
                self.top_grid_row.addWidget(nyear,alignment=Qt.AlignCenter)
                nmonth=QPushButton('<  ')
                nmonth.setFlat(True)
                nmonth.clicked.connect(self.nextMonth)
                self.top_grid_row.addWidget(nmonth,alignment=Qt.AlignCenter)
                self.lbly=QLabel()
                self.top_grid_row.addWidget(self.lbly,alignment=Qt.AlignCenter)
                self.lblm=QLabel()
                self.top_grid_row.addWidget(self.lblm,alignment=Qt.AlignCenter)
                pmonth=QPushButton('  >')
                pmonth.setFlat(True)
                pmonth.clicked.connect(self.previousMonth)
                self.top_grid_row.addWidget(pmonth,alignment=Qt.AlignCenter)
                pyear=QPushButton('>>')
                pyear.setFlat(True)
                pyear.clicked.connect(self.previousYear)
                self.top_grid_row.addWidget(pyear,alignment=Qt.AlignCenter)

                self.grid=QGridLayout()
                for i in range(0,7):
                        for j in range(0,7):
                                lbl=QLabel()
                                self.grid.addWidget(lbl, i,j, Qt.AlignHCenter)
                self.showCalendar()

                hbox=QHBoxLayout()
                hbox.addWidget(self.hejri,alignment=Qt.AlignCenter)
                hbox.addWidget(self.year,alignment=Qt.AlignCenter)
                hbox.addWidget(self.month,alignment=Qt.AlignCenter)
                hbox.addWidget(self.day,alignment=Qt.AlignCenter)
                hbox.addWidget(self.today,alignment=Qt.AlignCenter)

                v_box = QVBoxLayout()
                v_box.addLayout(hbox)
                v_box.addWidget(self.time, alignment=Qt.AlignCenter)
                v_box.addLayout(self.top_grid_row)
                v_box.addLayout(self.grid)
                self.setLayout(v_box)

        def updateDateTime(self):
                date = QDate.currentDate()
                jalali=JalaliDate.to_jalali(date.year(), date.month(), date.day())
                time = QTime.currentTime().toString('hh:mm:ss')
                self.time.setText(persian.convert_en_numbers(time))
                self.day.setText(persian.convert_en_numbers(str(jalali.day)))
                self.month.setText(persian.convert_en_numbers(str(Persian_Months[jalali.month])))
                self.year.setText(persian.convert_en_numbers(str(jalali.year)))

        def showCalendar(self):
                cal=calendar.TextCalendar().formatmonth(self.cYear,self.cMonth)
                calendar_string=str(cal).replace('\n', ' ').strip()
                calendar_string=re.sub(r'   ',' --',calendar_string)
                calendar_string=re.sub(r'  ',' ',calendar_string)
                cal=calendar_string.split(' ')
                cal[2]='ش'
                cal[3]='ي'
                cal[4]='د'
                cal[5]='س'
                cal[6]='چ'
                cal[7]='پ'
                cal[8]='ج'
                self.lbly.setText(cal[1])
                self.lblm.setText(Persian_Months_English[cal[0]])
                for i in range(0,7):
                        for j in range(0,7):
                                lbl=self.grid.itemAtPosition(i,j).widget()
                                lbl.setStyleSheet('font:20px b koodak')
                                if j==0:
                                        lbl.setStyleSheet('font:20px b koodak; color:red')
                                if i*7+8-j<len(cal) and cal[i*7+8-j]!='--':
                                        lbl.setText(cal[i*7+8-j])
                                else:
                                        lbl.setText('  ')
        def nextYear(self):
                self.cYear=self.cYear+1
                self.showCalendar()
                
                
        def nextMonth(self):
                if self.cMonth==12:
                        self.cYear=self.cYear+1
                        self.cMonth=1
                else:
                        self.cMonth=self.cMonth+1
                self.showCalendar()
                        
                        
        def previousYear(self):
                if self.cYear>1:
                        self.cYear=self.cYear-1
                        self.showCalendar()
        
        def previousMonth(self):
                if self.cMonth==1:
                        self.cYear=self.cYear-1
                        self.cMonth=12
                else:
                        self.cMonth=self.cMonth-1
                self.showCalendar()

if __name__ == '__main__':
        app = QApplication(sys.argv)
        app.setStyleSheet(Style_Sheet)
        window = MainWindow()
        sys.exit(app.exec_())
