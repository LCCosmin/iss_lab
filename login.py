from PyQt5 import QtCore, QtWidgets
from controller import Controller
from error import Ui_error_window
from boss import Ui_BossUI
from employee import Ui_EmployeeWindow


class Ui_LoginWindow(object):
    def __init__(self):
        self.ctrl = Controller()
        self.error_window = QtWidgets.QMainWindow()
        self.user_window = QtWidgets.QMainWindow()
        self.boss_window = QtWidgets.QMainWindow()
        
        self.ew = Ui_error_window()
        self.ew.setupUi(self.error_window)
        
        self.uw = Ui_EmployeeWindow()
        self.uw.setupUi(self.user_window)
        
        self.bw = Ui_BossUI()
        self.bw.setupUi(self.boss_window)
    
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(482, 406)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_data = QtWidgets.QTextEdit(self.centralwidget)
        self.username_data.setGeometry(QtCore.QRect(210, 10, 241, 31))
        self.username_data.setReadOnly(False)
        self.username_data.setObjectName("username_data")
        self.password_data = QtWidgets.QTextEdit(self.centralwidget)
        self.password_data.setGeometry(QtCore.QRect(210, 50, 241, 31))
        self.password_data.setReadOnly(False)
        self.password_data.setObjectName("password_data")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(40, 90, 411, 51))
        self.login_button.setObjectName("login_button")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(90, 150, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lcd_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_time.setGeometry(QtCore.QRect(140, 350, 201, 23))
        self.lcd_time.setObjectName("lcd_time")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 10, 91, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(110, 50, 91, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        
        self.login_button.clicked.connect(self.login)
        
        self.window = LoginWindow
        
    def close_window(self):
        self.window.close()

    def login(self):
        username = self.username_data.toPlainText()
        password = self.password_data.toPlainText()
        
        if username == "" or password == "":
            self.ew.set_text_error("Password or Username cannot be empty!")
            self.error_window.show()
        else:
            res = self.ctrl.try_login(username, password)
            
            if res is False:
                self.ew.set_text_error("User does not exist!")
                self.error_window.show()
            else:
                if res == 'EMPLOYEE':
                    self.uw.set_basic_data(username, password)
                    self.user_window.show()
                else:
                    self.bw.set_basic_data(username, password)
                    self.boss_window.show()
                
                self.close_window()

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.login_button.setText(_translate("LoginWindow", "Login"))
        self.textBrowser.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">username</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">password</span></p></body></html>"))
