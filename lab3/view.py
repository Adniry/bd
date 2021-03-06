# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Database(object):
    def __init__(self, Database):
        Database.setObjectName("Database")
        Database.resize(798, 529)
        self.centralwidget = QtWidgets.QWidget(Database)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 70, 71, 41))
        self.pushButton.setObjectName("pushButton")
        self.table = QtWidgets.QComboBox(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 50, 131, 41))
        self.table.setObjectName("table")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.table.addItem("")
        self.action = QtWidgets.QComboBox(self.centralwidget)
        self.action.setGeometry(QtCore.QRect(200, 50, 151, 41))
        self.action.setObjectName("action")
        self.action.addItem("")
        self.action.addItem("")
        self.action.addItem("")
        self.actLabel = QtWidgets.QLabel(self.centralwidget)
        self.actLabel.setGeometry(QtCore.QRect(30, 10, 291, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.actLabel.setFont(font)
        self.actLabel.setObjectName("actLabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(360, 50, 321, 70))
        self.textEdit.setObjectName("textEdit")
        self.genData = QtWidgets.QPushButton(self.centralwidget)
        self.genData.setGeometry(QtCore.QRect(20, 330, 611, 51))
        self.genData.setObjectName("genData")
        self.textSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.textSearch.setGeometry(QtCore.QRect(20, 190, 751, 131))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textSearch.setFont(font)
        self.textSearch.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.textSearch.setOverwriteMode(True)
        self.textSearch.setObjectName("textSearch")
        self.labelSearch = QtWidgets.QLabel(self.centralwidget)
        self.labelSearch.setGeometry(QtCore.QRect(30, 140, 151, 31))
        self.labelSearch.setObjectName("labelSearch")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 390, 751, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 300, 63, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 350, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(380, 120, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info.setFont(font)
        self.info.setStyleSheet("color:green")
        self.info.setObjectName("info")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(370, 10, 401, 31))
        self.error.setStyleSheet("color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.full_text_box = QtWidgets.QComboBox(self.centralwidget)
        self.full_text_box.setGeometry(QtCore.QRect(190, 130, 131, 41))
        self.full_text_box.setObjectName("full_text_box")
        self.full_text_box.addItem("")
        self.full_text_box.addItem("")
        self.full_text_box.addItem("")
        self.full_text_box.addItem("")
        self.full_text_box.addItem("")
        self.full_text_box.addItem("")
        self.gen_label = QtWidgets.QLabel(self.centralwidget)
        self.gen_label.setGeometry(QtCore.QRect(660, 320, 62, 19))
        self.gen_label.setText("")
        self.gen_label.setObjectName("gen_label")
        Database.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Database)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName("menubar")
        Database.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Database)
        self.statusbar.setObjectName("statusbar")
        Database.setStatusBar(self.statusbar)

        self.retranslateUi(Database)
        QtCore.QMetaObject.connectSlotsByName(Database)

    def retranslateUi(self, Database):
        _translate = QtCore.QCoreApplication.translate
        Database.setWindowTitle(_translate("Database", "MainWindow"))
        self.pushButton.setText(_translate("Database", "Action"))
        self.table.setItemText(0, _translate("Database", "Person"))
        self.table.setItemText(1, _translate("Database", "Transport"))
        self.table.setItemText(2, _translate("Database", "Stop"))
        self.table.setItemText(3, _translate("Database", "Ticket"))
        self.table.setItemText(4, _translate("Database", "Schedule"))
        self.table.setItemText(5, _translate("Database", "Trip"))
        self.action.setItemText(0, _translate("Database", "delete"))
        self.action.setItemText(1, _translate("Database", "update"))
        self.action.setItemText(2, _translate("Database", "insert"))
        self.actLabel.setText(_translate("Database", "Choose table and action to do:"))
        self.genData.setText(_translate("Database", "Generate random data to database!"))
        self.textSearch.setHtml(_translate("Database", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\';\"><br /></p></body></html>"))
        self.labelSearch.setText(_translate("Database", "Enter word or phrase:"))
        self.pushButton_2.setText(_translate("Database", "Find trips in time interval -->"))
        self.pushButton_3.setText(_translate("Database", "Search "))
        self.info.setText(_translate("Database", " delete: pid = 10;\n"
" insert: pid =10, name=\'Andriy\'... \n"
" update: (where) pid = 10 \n"
" (what)exemption = \'pensioner\' "))
        self.full_text_box.setItemText(0, _translate("Database", "Person"))
        self.full_text_box.setItemText(1, _translate("Database", "Transport"))
        self.full_text_box.setItemText(2, _translate("Database", "Stop"))
        self.full_text_box.setItemText(3, _translate("Database", "Ticket"))
        self.full_text_box.setItemText(4, _translate("Database", "Schedule"))
        self.full_text_box.setItemText(5, _translate("Database", "Trip"))
