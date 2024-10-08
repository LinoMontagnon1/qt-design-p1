# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bas3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 705)
        MainWindow.setMinimumSize(QtCore.QSize(1012, 705))
        MainWindow.setMaximumSize(QtCore.QSize(1012, 705))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background1 = QtWidgets.QWidget(self.centralwidget)
        self.background1.setGeometry(QtCore.QRect(20, 10, 311, 641))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.background1.setFont(font)
        self.background1.setStyleSheet("background-color: rgb(221, 221, 221)")
        self.background1.setObjectName("background1")
        self.mechanic_background = QtWidgets.QWidget(self.background1)
        self.mechanic_background.setGeometry(QtCore.QRect(0, 20, 311, 51))
        self.mechanic_background.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mechanic_background.setAutoFillBackground(False)
        self.mechanic_background.setStyleSheet("QWidget {\n"
"    background-color: #ffc355; /* cor de fundo amarela */\n"
"    /*border-radius: 10px;*/\n"
"\n"
"}\n"
"")
        self.mechanic_background.setObjectName("mechanic_background")
        self.mechanic_label = QtWidgets.QLabel(self.mechanic_background)
        self.mechanic_label.setGeometry(QtCore.QRect(90, 10, 121, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mechanic_label.setFont(font)
        self.mechanic_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mechanic_label.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.mechanic_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mechanic_label.setWordWrap(False)
        self.mechanic_label.setObjectName("mechanic_label")
        self.oversample = QtWidgets.QLabel(self.background1)
        self.oversample.setGeometry(QtCore.QRect(50, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.oversample.setFont(font)
        self.oversample.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.oversample.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.oversample.setAlignment(QtCore.Qt.AlignCenter)
        self.oversample.setWordWrap(False)
        self.oversample.setObjectName("oversample")
        self.scan = QtWidgets.QLabel(self.background1)
        self.scan.setGeometry(QtCore.QRect(50, 350, 131, 45))
        self.scan.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.scan.setFont(font)
        self.scan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scan.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.scan.setAlignment(QtCore.Qt.AlignCenter)
        self.scan.setWordWrap(False)
        self.scan.setObjectName("scan")
        self.pitch = QtWidgets.QLabel(self.background1)
        self.pitch.setGeometry(QtCore.QRect(50, 500, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pitch.setFont(font)
        self.pitch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pitch.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.pitch.setAlignment(QtCore.Qt.AlignCenter)
        self.pitch.setWordWrap(False)
        self.pitch.setObjectName("pitch")
        self.input_exposures = QtWidgets.QSpinBox(self.background1)
        self.input_exposures.setGeometry(QtCore.QRect(50, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_exposures.setFont(font)
        self.input_exposures.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_exposures.setPrefix("")
        self.input_exposures.setMinimum(-999999999)
        self.input_exposures.setMaximum(999999999)
        self.input_exposures.setObjectName("input_exposures")
        self.input_oversample = QtWidgets.QSpinBox(self.background1)
        self.input_oversample.setGeometry(QtCore.QRect(50, 260, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_oversample.setFont(font)
        self.input_oversample.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_oversample.setMinimum(-999999999)
        self.input_oversample.setMaximum(999999999)
        self.input_oversample.setObjectName("input_oversample")
        self.input_scan = QtWidgets.QSpinBox(self.background1)
        self.input_scan.setGeometry(QtCore.QRect(50, 400, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_scan.setFont(font)
        self.input_scan.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_scan.setMinimum(-999999999)
        self.input_scan.setMaximum(999999999)
        self.input_scan.setObjectName("input_scan")
        self.input_pitch = QtWidgets.QSpinBox(self.background1)
        self.input_pitch.setGeometry(QtCore.QRect(50, 540, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_pitch.setFont(font)
        self.input_pitch.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_pitch.setMinimum(-999999999)
        self.input_pitch.setMaximum(999999999)
        self.input_pitch.setObjectName("input_pitch")
        self.exposure_counts = QtWidgets.QLabel(self.background1)
        self.exposure_counts.setGeometry(QtCore.QRect(50, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exposure_counts.setFont(font)
        self.exposure_counts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exposure_counts.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.exposure_counts.setAlignment(QtCore.Qt.AlignCenter)
        self.exposure_counts.setWordWrap(False)
        self.exposure_counts.setObjectName("exposure_counts")
        self.discr_exposure_count = QtWidgets.QPushButton(self.background1)
        self.discr_exposure_count.setGeometry(QtCore.QRect(240, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_exposure_count.setFont(font)
        self.discr_exposure_count.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_exposure_count.setObjectName("discr_exposure_count")
        self.discr_oversample = QtWidgets.QPushButton(self.background1)
        self.discr_oversample.setGeometry(QtCore.QRect(240, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_oversample.setFont(font)
        self.discr_oversample.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_oversample.setObjectName("discr_oversample")
        self.discr_scan = QtWidgets.QPushButton(self.background1)
        self.discr_scan.setGeometry(QtCore.QRect(240, 360, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_scan.setFont(font)
        self.discr_scan.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_scan.setObjectName("discr_scan")
        self.discr_pitch = QtWidgets.QPushButton(self.background1)
        self.discr_pitch.setGeometry(QtCore.QRect(240, 500, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_pitch.setFont(font)
        self.discr_pitch.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_pitch.setObjectName("discr_pitch")
        self.background2 = QtWidgets.QWidget(self.centralwidget)
        self.background2.setGeometry(QtCore.QRect(350, 10, 311, 641))
        self.background2.setStyleSheet("background-color: rgb(221, 221, 221)")
        self.background2.setObjectName("background2")
        self.tube_background = QtWidgets.QWidget(self.background2)
        self.tube_background.setGeometry(QtCore.QRect(0, 20, 311, 51))
        self.tube_background.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tube_background.setAutoFillBackground(False)
        self.tube_background.setStyleSheet("QWidget {\n"
"    background-color: #ffc355; /* cor de fundo amarela */\n"
"    /*border-radius: 10px;*/\n"
"\n"
"}\n"
"")
        self.tube_background.setObjectName("tube_background")
        self.tube_label = QtWidgets.QLabel(self.tube_background)
        self.tube_label.setGeometry(QtCore.QRect(120, 10, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tube_label.setFont(font)
        self.tube_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tube_label.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.tube_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tube_label.setWordWrap(False)
        self.tube_label.setObjectName("tube_label")
        self.input_kv = QtWidgets.QSpinBox(self.background2)
        self.input_kv.setGeometry(QtCore.QRect(50, 220, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_kv.setFont(font)
        self.input_kv.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_kv.setMinimum(-999999999)
        self.input_kv.setMaximum(999999999)
        self.input_kv.setObjectName("input_kv")
        self.kv = QtWidgets.QLabel(self.background2)
        self.kv.setGeometry(QtCore.QRect(50, 180, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.kv.setFont(font)
        self.kv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kv.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.kv.setAlignment(QtCore.Qt.AlignCenter)
        self.kv.setWordWrap(False)
        self.kv.setObjectName("kv")
        self.mas = QtWidgets.QLabel(self.background2)
        self.mas.setGeometry(QtCore.QRect(50, 290, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mas.setFont(font)
        self.mas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mas.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.mas.setAlignment(QtCore.Qt.AlignCenter)
        self.mas.setWordWrap(False)
        self.mas.setObjectName("mas")
        self.input_mas = QtWidgets.QSpinBox(self.background2)
        self.input_mas.setGeometry(QtCore.QRect(50, 330, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_mas.setFont(font)
        self.input_mas.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_mas.setMinimum(-999999999)
        self.input_mas.setMaximum(999999999)
        self.input_mas.setObjectName("input_mas")
        self.focus = QtWidgets.QLabel(self.background2)
        self.focus.setGeometry(QtCore.QRect(50, 390, 71, 45))
        self.focus.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.focus.setFont(font)
        self.focus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.focus.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.focus.setAlignment(QtCore.Qt.AlignCenter)
        self.focus.setWordWrap(False)
        self.focus.setObjectName("focus")
        self.input_focus = QtWidgets.QSpinBox(self.background2)
        self.input_focus.setGeometry(QtCore.QRect(50, 440, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.input_focus.setFont(font)
        self.input_focus.setStyleSheet("QSpinBox {\n"
"    background-color: rgb(238, 238, 238);\n"
"    border: 1px solid #a9a9a9;\n"
"    border-radius: 5px; \n"
"    padding: 1px 3px; \n"
"}\n"
"\n"
"\n"
"")
        self.input_focus.setMinimum(-999999999)
        self.input_focus.setMaximum(999999999)
        self.input_focus.setObjectName("input_focus")
        self.discr_kv = QtWidgets.QPushButton(self.background2)
        self.discr_kv.setGeometry(QtCore.QRect(240, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_kv.setFont(font)
        self.discr_kv.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_kv.setObjectName("discr_kv")
        self.discr_mAs = QtWidgets.QPushButton(self.background2)
        self.discr_mAs.setGeometry(QtCore.QRect(240, 290, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_mAs.setFont(font)
        self.discr_mAs.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_mAs.setObjectName("discr_mAs")
        self.discr_focus = QtWidgets.QPushButton(self.background2)
        self.discr_focus.setGeometry(QtCore.QRect(240, 400, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.discr_focus.setFont(font)
        self.discr_focus.setStyleSheet("QPushButton {\n"
"    border: none; /* Remove a borda */\n"
"    background-color: transparent; /* Fundo transparente */\n"
"    color: blue; /* Cor do texto em azul */\n"
"}\n"
"")
        self.discr_focus.setObjectName("discr_focus")
        self.background3_2 = QtWidgets.QWidget(self.centralwidget)
        self.background3_2.setGeometry(QtCore.QRect(680, 10, 311, 641))
        self.background3_2.setStyleSheet("background-color: rgb(221, 221, 221)")
        self.background3_2.setObjectName("background3_2")
        self.execute_background_2 = QtWidgets.QWidget(self.background3_2)
        self.execute_background_2.setGeometry(QtCore.QRect(0, 20, 311, 51))
        self.execute_background_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.execute_background_2.setAutoFillBackground(False)
        self.execute_background_2.setStyleSheet("QWidget {\n"
"    background-color: #ffc355; /* cor de fundo amarela */\n"
"    /*border-radius: 10px;*/\n"
"\n"
"}\n"
"")
        self.execute_background_2.setObjectName("execute_background_2")
        self.execute_label_2 = QtWidgets.QLabel(self.execute_background_2)
        self.execute_label_2.setGeometry(QtCore.QRect(70, 10, 161, 30))
        self.execute_label_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.execute_label_2.setFont(font)
        self.execute_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.execute_label_2.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.execute_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.execute_label_2.setWordWrap(False)
        self.execute_label_2.setObjectName("execute_label_2")
        self.download_json_2 = QtWidgets.QPushButton(self.background3_2)
        self.download_json_2.setGeometry(QtCore.QRect(70, 250, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.download_json_2.setFont(font)
        self.download_json_2.setStyleSheet("QWidget {\n"
"    background-color: #FFB62D; /* cor de fundo amarela */\n"
"    border-radius: 10px; /* bordas arredondadas */\n"
"    border: 1px solid black; /* borda sólida preta */\n"
"}\n"
"")
        self.download_json_2.setObjectName("download_json_2")
        self.upload_json_2 = QtWidgets.QPushButton(self.background3_2)
        self.upload_json_2.setGeometry(QtCore.QRect(70, 310, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.upload_json_2.setFont(font)
        self.upload_json_2.setStyleSheet("QWidget {\n"
"    background-color: #FFB62D; /* cor de fundo amarela */\n"
"    border-radius: 10px; /* bordas arredondadas */\n"
"    border: 1px solid black; /* borda sólida preta */\n"
"}\n"
"")
        self.upload_json_2.setObjectName("upload_json_2")
        self.clear_fields_2 = QtWidgets.QPushButton(self.background3_2)
        self.clear_fields_2.setGeometry(QtCore.QRect(70, 520, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_fields_2.setFont(font)
        self.clear_fields_2.setStyleSheet("QWidget {\n"
"    background-color: #FFB62D; /* cor de fundo amarela */\n"
"    border-radius: 10px; /* bordas arredondadas */\n"
"    border: 1px solid black; /* borda sólida preta */\n"
"}\n"
"")
        self.clear_fields_2.setObjectName("clear_fields_2")
        self.send_parameters_2 = QtWidgets.QPushButton(self.background3_2)
        self.send_parameters_2.setGeometry(QtCore.QRect(70, 120, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send_parameters_2.setFont(font)
        self.send_parameters_2.setStyleSheet("QWidget {\n"
"    background-color: #FFB62D; /* cor de fundo amarela */\n"
"    border-radius: 10px; /* bordas arredondadas */\n"
"    border: 1px solid black; /* borda sólida preta */\n"
"}\n"
"")
        self.send_parameters_2.setObjectName("send_parameters_2")
        self.default_json = QtWidgets.QPushButton(self.background3_2)
        self.default_json.setGeometry(QtCore.QRect(70, 460, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.default_json.setFont(font)
        self.default_json.setStyleSheet("QWidget {\n"
"    background-color: #FFB62D; /* cor de fundo amarela */\n"
"    border-radius: 10px; /* bordas arredondadas */\n"
"    border: 1px solid black; /* borda sólida preta */\n"
"}\n"
"")
        self.default_json.setObjectName("default_json")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic Settings"))
        self.mechanic_label.setText(_translate("MainWindow", "Mechanic"))
        self.oversample.setText(_translate("MainWindow", "Oversample"))
        self.scan.setText(_translate("MainWindow", "Scan Height"))
        self.pitch.setText(_translate("MainWindow", "Pitch"))
        self.exposure_counts.setText(_translate("MainWindow", "Projections"))
        self.discr_exposure_count.setText(_translate("MainWindow", "?"))
        self.discr_oversample.setText(_translate("MainWindow", "?"))
        self.discr_scan.setText(_translate("MainWindow", "?"))
        self.discr_pitch.setText(_translate("MainWindow", "?"))
        self.tube_label.setText(_translate("MainWindow", "Tube"))
        self.kv.setText(_translate("MainWindow", "kV"))
        self.mas.setText(_translate("MainWindow", "mAs"))
        self.focus.setText(_translate("MainWindow", "Focus"))
        self.discr_kv.setText(_translate("MainWindow", "?"))
        self.discr_mAs.setText(_translate("MainWindow", "?"))
        self.discr_focus.setText(_translate("MainWindow", "?"))
        self.execute_label_2.setText(_translate("MainWindow", "Parameters"))
        self.download_json_2.setText(_translate("MainWindow", "Download"))
        self.upload_json_2.setText(_translate("MainWindow", "Upload"))
        self.clear_fields_2.setText(_translate("MainWindow", "Clear Fields"))
        self.send_parameters_2.setText(_translate("MainWindow", "Send "))
        self.default_json.setText(_translate("MainWindow", "Default"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
