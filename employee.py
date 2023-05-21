from controller import Controller
from error import Ui_error_window
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeeWindow(object):
    def __init__(self) -> None:
        self.ctrl = Controller()
        self.error_window = QtWidgets.QMainWindow()
        
        self.ew = Ui_error_window()
        self.ew.setupUi(self.error_window)

    def set_basic_data(self, username: str, password: str) -> None:
        _translate = QtCore.QCoreApplication.translate
        
        user_data = self.ctrl.get_user_data(username, password)
        self.employee_name.setText(_translate("EmployeeWindow", user_data.username))
        self.employee_email.setText(_translate("EmployeeWindow", user_data.email))
        self.employee_department.setText(_translate("EmployeeWindow", user_data.department))
        self.employee_status.setText(_translate("EmployeeWindow", "Not Active"))
        
        assigned_tasks = self.ctrl.get_assigned_tasks(user_data.id)
        self.user_id = user_data.id
        model = QtGui.QStandardItemModel()
        if assigned_tasks is not []:
            for task in assigned_tasks:
                item = QtGui.QStandardItem(task.task_title)
                model.appendRow(item)
        
        self.task_list.setModel(model)
        
    def setupUi(self, EmployeeWindow):
        EmployeeWindow.setObjectName("EmployeeWindow")
        EmployeeWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EmployeeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clock_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.clock_in_button.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.clock_in_button.setObjectName("clock_in_button")
        self.clock_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.clock_out_button.setGeometry(QtCore.QRect(10, 70, 191, 51))
        self.clock_out_button.setObjectName("clock_out_button")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(260, 10, 51, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(260, 50, 51, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(520, 50, 91, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.employee_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.employee_name.setGeometry(QtCore.QRect(320, 10, 181, 31))
        self.employee_name.setObjectName("employee_name")
        self.employee_email = QtWidgets.QTextBrowser(self.centralwidget)
        self.employee_email.setGeometry(QtCore.QRect(320, 50, 181, 31))
        self.employee_email.setObjectName("employee_email")
        self.employee_department = QtWidgets.QTextBrowser(self.centralwidget)
        self.employee_department.setGeometry(QtCore.QRect(620, 50, 171, 31))
        self.employee_department.setObjectName("employee_department")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(520, 10, 91, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.current_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.current_time.setGeometry(QtCore.QRect(620, 10, 171, 31))
        self.current_time.setObjectName("current_time")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(10, 150, 181, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(190, 150, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(520, 90, 91, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.employee_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.employee_status.setGeometry(QtCore.QRect(620, 90, 171, 31))
        self.employee_status.setObjectName("employee_status")
        self.task_list = QtWidgets.QListView(self.centralwidget)
        self.task_list.setGeometry(QtCore.QRect(10, 190, 181, 401))
        self.task_list.setObjectName("task_list")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_12.setGeometry(QtCore.QRect(210, 150, 81, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.task_title = QtWidgets.QTextBrowser(self.centralwidget)
        self.task_title.setGeometry(QtCore.QRect(300, 150, 211, 31))
        self.task_title.setObjectName("task_title")
        self.task_title.setReadOnly(False)
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_14.setGeometry(QtCore.QRect(520, 150, 91, 31))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.task_story_points = QtWidgets.QTextBrowser(self.centralwidget)
        self.task_story_points.setGeometry(QtCore.QRect(620, 150, 171, 31))
        self.task_story_points.setObjectName("task_story_points")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_16.setGeometry(QtCore.QRect(210, 190, 111, 31))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.task_description = QtWidgets.QTextBrowser(self.centralwidget)
        self.task_description.setGeometry(QtCore.QRect(210, 230, 581, 291))
        self.task_description.setObjectName("task_description")
        self.move_next_step = QtWidgets.QPushButton(self.centralwidget)
        self.move_next_step.setGeometry(QtCore.QRect(210, 530, 281, 61))
        self.move_next_step.setObjectName("move_next_step")
        self.move_step_back = QtWidgets.QPushButton(self.centralwidget)
        self.move_step_back.setGeometry(QtCore.QRect(500, 530, 291, 61))
        self.move_step_back.setObjectName("move_step_back")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(323, 190, 20, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_18.setGeometry(QtCore.QRect(350, 190, 121, 31))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.task_current_step = QtWidgets.QTextBrowser(self.centralwidget)
        self.task_current_step.setGeometry(QtCore.QRect(480, 190, 141, 31))
        self.task_current_step.setObjectName("task_current_step")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(260, 90, 241, 31))
        self.log_out.setObjectName("log_out")
        self.get_task_details = QtWidgets.QPushButton(self.centralwidget)
        self.get_task_details.setGeometry(QtCore.QRect(630, 190, 161, 31))
        self.get_task_details.setObjectName("get_task_details")
        EmployeeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmployeeWindow)
        QtCore.QMetaObject.connectSlotsByName(EmployeeWindow)
        
        self.get_task_details.clicked.connect(self.generate_details_task)
        self.move_next_step.clicked.connect(self.move_task_next)
        self.move_step_back.clicked.connect(self.move_task_back)

    def generate_details_task(self):
        task_title = self.task_title.toPlainText()
        _translate = QtCore.QCoreApplication.translate
        
        if task_title == "":
            self.ew.set_text_error("Task Title cannot be empty!")
            self.error_window.show()
        else:
            result = self.ctrl.get_task_data(task_title)
            if result is None:
                self.ew.set_text_error("Task does not exist!")
                self.error_window.show()
            else:
                self.task_story_points.setText(_translate("EmployeeWindow", str(result.story_points)))
                self.task_description.setText(_translate("EmployeeWindow", result.task_description))
                self.task_current_step.setText(_translate("EmployeeWindow", result.status))

    def move_task_next(self):
        task_title = self.task_title.toPlainText()
        
        if task_title == "":
            self.ew.set_text_error("Task Title cannot be empty!")
            self.error_window.show()
        else:
            result = self.ctrl.get_task_data(task_title)
            if result is None:
                self.ew.set_text_error("Task does not exist!")
                self.error_window.show()
            else:
                self.ctrl.move_task_next_step(result.id, result.status)
                
                assigned_tasks = self.ctrl.get_assigned_tasks(self.user_id)
                model = QtGui.QStandardItemModel()
                if assigned_tasks is not []:
                    for task in assigned_tasks:
                        item = QtGui.QStandardItem(task.task_title)
                        model.appendRow(item)
                
                self.task_list.setModel(model)
                
                self.ew.set_text_error("Task moved to next step with success!")
                self.error_window.show()

    def move_task_back(self):
        task_title = self.task_title.toPlainText()
        
        if task_title == "":
            self.ew.set_text_error("Task Title cannot be empty!")
            self.error_window.show()
        else:
            result = self.ctrl.get_task_data(task_title)
            if result is None:
                self.ew.set_text_error("Task does not exist!")
                self.error_window.show()
            else:
                self.ctrl.move_task_prev_step(result.id, result.status)
                
                assigned_tasks = self.ctrl.get_assigned_tasks(self.user_id)
                model = QtGui.QStandardItemModel()
                if assigned_tasks is not []:
                    for task in assigned_tasks:
                        item = QtGui.QStandardItem(task.task_title)
                        model.appendRow(item)
                
                self.task_list.setModel(model)
                
                self.ew.set_text_error("Task moved to previous step with success!")
                self.error_window.show()

    def retranslateUi(self, EmployeeWindow):
        _translate = QtCore.QCoreApplication.translate
        EmployeeWindow.setWindowTitle(_translate("EmployeeWindow", "Employee UI"))
        self.clock_in_button.setText(_translate("EmployeeWindow", "Clock IN"))
        self.clock_out_button.setText(_translate("EmployeeWindow", "Clock OUT"))
        self.textBrowser_2.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Name: </span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Email: </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Department: </span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Current Time: </span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Current Assigned Tasks:</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Status: </span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Task Title:</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Story Points:</span></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Task Description:</span></p></body></html>"))
        self.move_next_step.setText(_translate("EmployeeWindow", "Move Task Next Step"))
        self.move_step_back.setText(_translate("EmployeeWindow", "Move Task Step Back"))
        self.textBrowser_18.setHtml(_translate("EmployeeWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Current Step Task:</span></p></body></html>"))
        self.log_out.setText(_translate("EmployeeWindow", "Log OUT"))
        self.get_task_details.setText(_translate("EmployeeWindow", "Get Task Details"))
