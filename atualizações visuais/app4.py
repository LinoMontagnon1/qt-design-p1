# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1344, 878)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 1131, 40))
        self.label.setObjectName("label")
        self.frame_detector = QtWidgets.QFrame(self.centralwidget)
        self.frame_detector.setGeometry(QtCore.QRect(140, 90, 450, 270))
        self.frame_detector.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_detector.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_detector.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_detector.setObjectName("frame_detector")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_detector)
        self.verticalLayout_2.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_detector = QtWidgets.QLabel(self.frame_detector)
        self.label_detector.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_detector.setStyleSheet("Border: None\n"
"")
        self.label_detector.setObjectName("label_detector")
        self.verticalLayout_2.addWidget(self.label_detector)
        self.button_detector = QtWidgets.QPushButton(self.frame_detector)
        self.button_detector.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_detector.setObjectName("button_detector")
        self.verticalLayout_2.addWidget(self.button_detector)
        self.frame_command = QtWidgets.QFrame(self.centralwidget)
        self.frame_command.setGeometry(QtCore.QRect(90, 410, 271, 187))
        self.frame_command.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_command.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_command.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_command.setObjectName("frame_command")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_command)
        self.verticalLayout_7.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_command = QtWidgets.QLabel(self.frame_command)
        self.label_command.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_command.setStyleSheet("Border: None\n"
"")
        self.label_command.setObjectName("label_command")
        self.verticalLayout_7.addWidget(self.label_command)
        self.button_command = QtWidgets.QPushButton(self.frame_command)
        self.button_command.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_command.setObjectName("button_command")
        self.verticalLayout_7.addWidget(self.button_command)
        self.Basic_Settings_Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Basic_Settings_Button_3.setGeometry(QtCore.QRect(1080, 710, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Basic_Settings_Button_3.setFont(font)
        self.Basic_Settings_Button_3.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 9pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #f6d57c;")
        self.Basic_Settings_Button_3.setObjectName("Basic_Settings_Button_3")
        self.Basic_Settings_Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Basic_Settings_Button_2.setGeometry(QtCore.QRect(1080, 763, 151, 31))
        self.Basic_Settings_Button_2.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 9pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #f6d57c;")
        self.Basic_Settings_Button_2.setObjectName("Basic_Settings_Button_2")
        self.button_user = QtWidgets.QPushButton(self.centralwidget)
        self.button_user.setGeometry(QtCore.QRect(250, 723, 201, 51))
        self.button_user.setMaximumSize(QtCore.QSize(16777215, 64))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_user.setFont(font)
        self.button_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_user.setStyleSheet("display: flex;\n"
"color: rgb(255, 255, 255);\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 16pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #B0BF1A")
        self.button_user.setObjectName("button_user")
        self.label_user = QtWidgets.QLabel(self.centralwidget)
        self.label_user.setGeometry(QtCore.QRect(100, 680, 141, 131))
        self.label_user.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_user.setObjectName("label_user")
        self.frame_image = QtWidgets.QFrame(self.centralwidget)
        self.frame_image.setGeometry(QtCore.QRect(740, 90, 450, 270))
        self.frame_image.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_image)
        self.verticalLayout_4.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_visualizer = QtWidgets.QLabel(self.frame_image)
        self.label_visualizer.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_visualizer.setStyleSheet("Border: None\n"
"")
        self.label_visualizer.setObjectName("label_visualizer")
        self.verticalLayout_4.addWidget(self.label_visualizer)
        self.button_visualizer = QtWidgets.QPushButton(self.frame_image)
        self.button_visualizer.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_visualizer.setObjectName("button_visualizer")
        self.verticalLayout_4.addWidget(self.button_visualizer)
        self.frame_basic = QtWidgets.QFrame(self.centralwidget)
        self.frame_basic.setGeometry(QtCore.QRect(390, 410, 271, 187))
        self.frame_basic.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_basic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_basic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_basic.setObjectName("frame_basic")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_basic)
        self.verticalLayout_8.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_basic = QtWidgets.QLabel(self.frame_basic)
        self.label_basic.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_basic.setStyleSheet("Border: None\n"
"")
        self.label_basic.setObjectName("label_basic")
        self.verticalLayout_8.addWidget(self.label_basic)
        self.button_basic = QtWidgets.QPushButton(self.frame_basic)
        self.button_basic.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_basic.setObjectName("button_basic")
        self.verticalLayout_8.addWidget(self.button_basic)
        self.frame_advance = QtWidgets.QFrame(self.centralwidget)
        self.frame_advance.setGeometry(QtCore.QRect(690, 410, 271, 187))
        self.frame_advance.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_advance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_advance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_advance.setObjectName("frame_advance")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_advance)
        self.verticalLayout_9.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_advance = QtWidgets.QLabel(self.frame_advance)
        self.label_advance.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_advance.setStyleSheet("Border: None\n"
"")
        self.label_advance.setObjectName("label_advance")
        self.verticalLayout_9.addWidget(self.label_advance)
        self.button_advance = QtWidgets.QPushButton(self.frame_advance)
        self.button_advance.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_advance.setObjectName("button_advance")
        self.verticalLayout_9.addWidget(self.button_advance)
        self.frame_server = QtWidgets.QFrame(self.centralwidget)
        self.frame_server.setGeometry(QtCore.QRect(970, 410, 271, 187))
        self.frame_server.setStyleSheet("background-color: rgb(244, 244, 244);\n"
"border-radius: 10px;\n"
"border: 1px solid #ACACAC;\n"
"")
        self.frame_server.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_server.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_server.setObjectName("frame_server")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_server)
        self.verticalLayout_10.setContentsMargins(-1, 16, 16, 0)
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_server = QtWidgets.QLabel(self.frame_server)
        self.label_server.setMaximumSize(QtCore.QSize(16777215, 82))
        self.label_server.setStyleSheet("Border: None\n"
"")
        self.label_server.setObjectName("label_server")
        self.verticalLayout_10.addWidget(self.label_server)
        self.button_server = QtWidgets.QPushButton(self.frame_server)
        self.button_server.setStyleSheet("display: flex;\n"
"padding: 8px 24px;\n"
"justify-content: center;\n"
"align-items: center;\n"
"gap: 10px;\n"
"align-self: stretch;\n"
"font: 12pt \"Segoe UI\";\n"
"\n"
"border-radius: 8px;\n"
"background: #FFB62D;")
        self.button_server.setObjectName("button_server")
        self.verticalLayout_10.addWidget(self.button_server)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CT IBTI"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/Logo-IBTI-resised.png\"/></p></body></html>"))
        self.label_detector.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/tomograph 1.png\"/></p></body></html>"))
        self.button_detector.setText(_translate("MainWindow", "Status"))
        self.label_command.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/send.png\"/></p></body></html>"))
        self.button_command.setText(_translate("MainWindow", "CT Controler"))
        self.Basic_Settings_Button_3.setText(_translate("MainWindow", "Guidelines"))
        self.Basic_Settings_Button_2.setText(_translate("MainWindow", "Version Info"))
        self.button_user.setText(_translate("MainWindow", "Change user"))
        self.label_user.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/user.png\"/></p></body></html>"))
        self.label_visualizer.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/tomograph 1.png\"/></p></body></html>"))
        self.button_visualizer.setText(_translate("MainWindow", "Image Analizer"))
        self.label_basic.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/send.png\"/></p></body></html>"))
        self.button_basic.setText(_translate("MainWindow", "Basic Settings"))
        self.label_advance.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/send.png\"/></p></body></html>"))
        self.button_advance.setText(_translate("MainWindow", "Advance Settings"))
        self.label_server.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><img src=\":/Logo/QT designer assets/send.png\"/></p></body></html>"))
        self.button_server.setText(_translate("MainWindow", "Data Controler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
