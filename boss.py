from PyQt5 import QtCore, QtGui, QtWidgets
from error import Ui_error_window
from controller import Controller


class Ui_BossUI(object):
    def __init__(self):
        self.ctrl = Controller()
        self.error_window = QtWidgets.QMainWindow()
        
        self.ew = Ui_error_window()
        self.ew.setupUi(self.error_window)

    def set_basic_data(self, username: str, password: str) -> None:
        _translate = QtCore.QCoreApplication.translate
        
        user_data = self.ctrl.get_user_data(username, password)
        self.boss_name.setText(_translate("BossUI", user_data.username))
        self.boss_email.setText(_translate("BossUI", user_data.email))
        
        active_list_employees = self.ctrl.get_active_employees()
        
        model = QtGui.QStandardItemModel()
        if active_list_employees is not []:
            for employee in active_list_employees:
                item = QtGui.QStandardItem(employee.username)
                model.appendRow(item)
        
        self.active_employees.setModel(model)

    def generate_task(self):
        task_name = self.task_name.toPlainText()
        task_description = self.task_description.toPlainText()
        task_story_points = self.task_story_points.toPlainText()
        assign_to_list = self.assign_to_list.toPlainText()
        
        if (
            task_name == "" or
            task_description == "" or
            task_story_points == "" or
            assign_to_list == ""
        ):
            self.ew.set_text_error("Task Name, Task Description, Story points, Assign list cannot be empty!")
            self.error_window.show()
        else:
            self.ctrl.generate_new_task(
                task_name=task_name,
                task_description=task_description,
                task_story_points=int(task_story_points),
                assign_to_list=assign_to_list,
                boss_name=self.boss_name.toPlainText()
            )
            
            self.ew.set_text_error("Task Generated with Success!")
            self.error_window.show()

    def setupUi(self, BossUI):
        BossUI.setObjectName("BossUI")
        BossUI.resize(800, 560)
        self.centralwidget = QtWidgets.QWidget(BossUI)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(520, 10, 91, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.log_out = QtWidgets.QPushButton(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(520, 50, 271, 31))
        self.log_out.setObjectName("log_out")
        self.boss_email = QtWidgets.QTextBrowser(self.centralwidget)
        self.boss_email.setGeometry(QtCore.QRect(320, 50, 181, 31))
        self.boss_email.setObjectName("boss_email")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(260, 10, 51, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.current_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.current_time.setGeometry(QtCore.QRect(620, 10, 171, 31))
        self.current_time.setObjectName("current_time")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(260, 50, 51, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.boss_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.boss_name.setGeometry(QtCore.QRect(320, 10, 181, 31))
        self.boss_name.setObjectName("boss_name")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 10, 20, 541))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 90, 531, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.active_employees = QtWidgets.QListView(self.centralwidget)
        self.active_employees.setGeometry(QtCore.QRect(10, 50, 231, 501))
        self.active_employees.setObjectName("active_employees")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(260, 150, 91, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(260, 110, 81, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(430, 150, 71, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.assign_to_list = QtWidgets.QTextBrowser(self.centralwidget)
        self.assign_to_list.setGeometry(QtCore.QRect(510, 150, 281, 31))
        self.assign_to_list.setObjectName("assign_to_list")
        self.assign_to_list.setReadOnly(False)
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(260, 190, 111, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.task_description = QtWidgets.QTextEdit(self.centralwidget)
        self.task_description.setGeometry(QtCore.QRect(260, 230, 531, 251))
        self.task_description.setObjectName("task_description")
        self.task_name = QtWidgets.QTextEdit(self.centralwidget)
        self.task_name.setGeometry(QtCore.QRect(350, 110, 441, 31))
        self.task_name.setObjectName("task_name")
        self.task_story_points = QtWidgets.QTextEdit(self.centralwidget)
        self.task_story_points.setGeometry(QtCore.QRect(360, 150, 61, 31))
        self.task_story_points.setObjectName("task_story_points")
        self.create_task = QtWidgets.QPushButton(self.centralwidget)
        self.create_task.setGeometry(QtCore.QRect(260, 490, 531, 61))
        self.create_task.setObjectName("create_task")
        BossUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(BossUI)
        QtCore.QMetaObject.connectSlotsByName(BossUI)
        
        self.create_task.clicked.connect(self.generate_task)
        
        self.window = BossUI

    def retranslateUi(self, BossUI):
        _translate = QtCore.QCoreApplication.translate
        BossUI.setWindowTitle(_translate("BossUI", "Boss UI"))
        self.textBrowser_8.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Current Time: </span></p></body></html>"))
        self.log_out.setText(_translate("BossUI", "Log OUT"))
        self.textBrowser_2.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Name: </span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Email: </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Active Employees: </span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Story Points: </span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Task Name: </span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Assign To: </span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("BossUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Task Description: </span></p></body></html>"))
        self.create_task.setText(_translate("BossUI", "Create Task"))
