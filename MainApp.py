# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogIn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from MainMenu import Ui_Form
import mysql.connector

class Ui_LogInMenu(object):
    def setupUi(self, LogInMenu, database):
        LogInMenu.setObjectName("LogInMenu")
        LogInMenu.resize(738, 499)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogInMenu.setWindowIcon(icon)
        LogInMenu.setStyleSheet("")
        self.db = database
        self.FrameTitle = QtWidgets.QFrame(LogInMenu)
        self.FrameTitle.setGeometry(QtCore.QRect(-1, -1, 271, 501))
        self.FrameTitle.setStyleSheet("background-color: rgb(0, 150, 136);")
        self.FrameTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameTitle.setObjectName("FrameTitle")
        self.LogoMelati = QtWidgets.QLabel(self.FrameTitle)
        self.LogoMelati.setGeometry(QtCore.QRect(20, 80, 231, 221))
        self.LogoMelati.setText("")
        self.LogoMelati.setPixmap(QtGui.QPixmap("img/melati.png"))
        self.LogoMelati.setScaledContents(True)
        self.LogoMelati.setObjectName("LogoMelati")
        self.TitleHotel = QtWidgets.QLabel(self.FrameTitle)
        self.TitleHotel.setGeometry(QtCore.QRect(20, 300, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Z003 [UKWN]")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TitleHotel.setFont(font)
        self.TitleHotel.setAlignment(QtCore.Qt.AlignCenter)
        self.TitleHotel.setObjectName("TitleHotel")
        self.SignIn = QtWidgets.QLabel(LogInMenu)
        self.SignIn.setGeometry(QtCore.QRect(430, 40, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(26)
        self.SignIn.setFont(font)
        self.SignIn.setStyleSheet("color: rgb(0, 150, 136);")
        self.SignIn.setAlignment(QtCore.Qt.AlignCenter)
        self.SignIn.setObjectName("SignIn")
        self.username = QtWidgets.QLineEdit(LogInMenu)
        self.username.setGeometry(QtCore.QRect(360, 170, 331, 41))
        self.username.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: black;\n"
"border-bottom: 2px solid rgb(0, 150, 136);")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(LogInMenu)
        self.password.setGeometry(QtCore.QRect(360, 270, 331, 41))
        self.password.setStyleSheet("background: transparent;\n"
"border: none;\n"
"color: black;\n"
"border-bottom: 2px solid rgb(0, 150, 136);")
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.EHUsername = QtWidgets.QLabel(LogInMenu)
        self.EHUsername.setGeometry(QtCore.QRect(360, 210, 160, 17))
        self.EHUsername.setObjectName("EHUsername")
        self.EHPassword = QtWidgets.QLabel(LogInMenu)
        self.EHPassword.setGeometry(QtCore.QRect(360, 310, 160, 17))
        self.EHPassword.setObjectName("EHPassword")
        self.ButtonLogIn = QtWidgets.QPushButton(LogInMenu)
        self.ButtonLogIn.setGeometry(QtCore.QRect(360, 390, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(20)
        self.ButtonLogIn.setFont(font)
        self.ButtonLogIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonLogIn.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color:rgb(0,150,136);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/akun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonLogIn.setIcon(icon1)
        self.ButtonLogIn.setIconSize(QtCore.QSize(31, 31))
        self.ButtonLogIn.setObjectName("ButtonLogIn")
        self.ButtonLogIn.clicked.connect(self.LogInClicked)

        self.retranslateUi(LogInMenu)
        QtCore.QMetaObject.connectSlotsByName(LogInMenu)

    def retranslateUi(self, LogInMenu):
        _translate = QtCore.QCoreApplication.translate
        LogInMenu.setWindowTitle(_translate("LogInMenu", "Hotel Melati"))
        self.TitleHotel.setText(_translate("LogInMenu", "Hotel Melati"))
        self.SignIn.setText(_translate("LogInMenu", "SIGN IN"))
        self.username.setPlaceholderText(_translate("LogInMenu", "Username"))
        self.password.setPlaceholderText(_translate("LogInMenu", "Password"))
        self.ButtonLogIn.setText(_translate("LogInMenu", "LOG IN"))

    def openMainWindow(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        LogInMenu.hide()
        self.window.show()

    def LogInClicked(self):
        _translate = QtCore.QCoreApplication.translate

        cursor = self.db.cursor()
        infoAdmin = ("SELECT `username`, `password` FROM Admin")
        cursor.execute(infoAdmin)

        infoUser = False
        infoPass = False

        for (username, password) in cursor:
            if self.username.text() == username:
                infoUser = True
            if self.password.text() == password:
                infoPass = True
        
        if infoPass == True and infoUser == True:
            self.openMainWindow()
        elif infoUser == False:
            self.EHUsername.setText(_translate("LogInMenu", "<font color=\"red\">Username anda salah</font>"))
            self.EHPassword.setText(_translate("LogInMenu", "<font color=\"red\">Password anda salah</font>"))
        else :
            self.EHUsername.setText(_translate("LogInMenu", "<font color=\"red\"> </font>"))
            self.EHPassword.setText(_translate("LogInMenu", "<font color=\"red\">Password anda salah</font>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogInMenu = QtWidgets.QWidget()
    DataBase = mysql.connector.connect(user="root", database="Hotel")
    ui = Ui_LogInMenu()
    ui.setupUi(LogInMenu, DataBase)
    LogInMenu.show()
    sys.exit(app.exec_())

