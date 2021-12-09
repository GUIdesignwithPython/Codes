# Information Form (Using Tabs)
# Section 5-5
import sys      
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTabWidget, QWidget,QHBoxLayout, QVBoxLayout,QLineEdit, QGroupBox, QRadioButton, QFormLayout, QTextEdit
from PyQt5.QtGui import QIcon

class InformationForm(QMainWindow):
        def __init__(self):
                super().__init__()      
                self.initUI()
        def initUI(self):
                self.setGeometry(300,50,300,300)
                self.setWindowTitle('Information Form')
                
                self.displaycomponents()
                self.show()

        def displaycomponents(self):
                self.tab_bar = QTabWidget(self)
                self.tab_bar.resize(300,300)
                self.contact_tab = QWidget()
                self.personal_tab=QWidget()
                self.education_tab = QWidget()
                self.tab_bar.addTab(self.contact_tab, QIcon('contact.png'), 'Contact')
                self.tab_bar.addTab(self.personal_tab,QIcon('personalinfo.png'), 'Personal')
                self.tab_bar.addTab(self.education_tab,QIcon('Education.png'), 'Education')
                self.ContactTab()
                self.PersonalTab()
                self.EducationTab()

                main_v_box = QVBoxLayout()
                main_v_box.addWidget(self.tab_bar)
                self.setLayout(main_v_box)

        def ContactTab(self):
                 fname_entry = QLineEdit()
                 lname_entry = QLineEdit()
                 address_entry = QLineEdit()
                 email_entry = QLineEdit()
                 phone_entry = QLineEdit()
                 frmlayout = QFormLayout()
                 other_info=QTextEdit()
                 frmlayout.addRow('First Name: ',fname_entry)
                 frmlayout.addRow('Last Name: ',lname_entry)
                 frmlayout.addRow('Address: ',address_entry)
                 frmlayout.addRow('Email: ',email_entry)
                 frmlayout.addRow('Phone Number: ',phone_entry)
                 frmlayout.addRow('Other Info: ',other_info)
                 self.contact_tab.setLayout(frmlayout)

        def PersonalTab(self):
                 self.marital_gb = QGroupBox('Marital Status')
                 self.marital_gb.setCheckable(True)
                 married_rb = QRadioButton('Married')
                 single_rb = QRadioButton('Single')
                 divorced_rb = QRadioButton('Divorced')
                 
                 marital_h_box = QHBoxLayout()
                 marital_h_box.addWidget(married_rb)
                 marital_h_box.addWidget(single_rb)
                 marital_h_box.addWidget(divorced_rb)
                 self.marital_gb.setLayout(marital_h_box)

                 self.gender_gb = QGroupBox('Gender')
                 male_rb = QRadioButton('Male')
                 female_rb = QRadioButton('Female')
                 gender_h_box = QHBoxLayout()
                 gender_h_box.addWidget(male_rb)
                 gender_h_box.addWidget(female_rb)
                 self.gender_gb.setLayout(gender_h_box)

                 date_of_birth=QLineEdit()       
                 place_of_birth=QLineEdit()       
                 other_info=QTextEdit()
                 frmlayout = QFormLayout()
                 frmlayout.addRow('Date of Birth: ',date_of_birth)
                 frmlayout.addRow('Place of Birth: ',place_of_birth)
                 frmlayout.addRow(self.gender_gb)
                 frmlayout.addRow(self.marital_gb)
                 frmlayout.addRow('Other Info: ',other_info)
                 self.personal_tab.setLayout(frmlayout)

        def EducationTab(self):
                 self.education_subject = QGroupBox('Education Subject')
                 ed_v_box = QVBoxLayout()
                 education_list = ['Math', 'Computer', 'Physics', 'Civil']
                 for ed in education_list:
                         self.education_rb = QRadioButton(ed)
                         ed_v_box.addWidget(self.education_rb)
                 self.education_subject.setLayout(ed_v_box)

                 self.education_gb = QGroupBox('Highest Level of Education')
                 ed_v_box = QVBoxLayout()
                 education_list = ['Associate Degree','Bachelor Degree', 'Master Degree', 'Doctorate or Higher']
                 for ed in education_list:
                         self.education_rb = QRadioButton(ed)
                         ed_v_box.addWidget(self.education_rb)
                 self.education_gb.setLayout(ed_v_box)

                 tab_v_box = QVBoxLayout()
                 tab_v_box.addWidget(self.education_subject)
                 tab_v_box.addWidget(self.education_gb)

                 self.education_tab.setLayout(tab_v_box)

if __name__=='__main__':
        app=QApplication(sys.argv)
        window=InformationForm()
        sys.exit(app.exec_())
   

    

