# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuEdit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import pymysql
import mysql.connector

class Ui_Edit(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1082, 605)
        self.datetime = datetime.datetime.now()
        self.TableInform = QtWidgets.QTableWidget(Form)
        self.TableInform.setGeometry(QtCore.QRect(370, 80, 701, 521))
        self.TableInform.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TableInform.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TableInform.setObjectName("TableInform")
        self.TableInform.setColumnCount(7)
        self.TableInform.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
        self.TableInform.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
        self.TableInform.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        item.setFont(font)
        self.TableInform.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableInform.setHorizontalHeaderItem(6, item)
        self.TableInform.itemSelectionChanged.connect(self.InsertData)
        self.FramHeader = QtWidgets.QFrame(Form)
        self.FramHeader.setGeometry(QtCore.QRect(-1, 0, 1091, 51))
        self.FramHeader.setStyleSheet("background-color: rgb(0, 150, 136);")
        self.FramHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FramHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FramHeader.setObjectName("FramHeader")
        self.LabelTittle = QtWidgets.QLabel(self.FramHeader)
        self.LabelTittle.setGeometry(QtCore.QRect(0, 0, 861, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTittle.setFont(font)
        self.LabelTittle.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelTittle.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTittle.setObjectName("LabelTittle")
        self.LogoTitle = QtWidgets.QLabel(self.FramHeader)
        self.LogoTitle.setGeometry(QtCore.QRect(650, 10, 41, 31))
        self.LogoTitle.setText("")
        self.LogoTitle.setPixmap(QtGui.QPixmap("img/LogMenu.png"))
        self.LogoTitle.setScaledContents(True)
        self.LogoTitle.setObjectName("LogoTitle")
        self.FormNama = QtWidgets.QLineEdit(Form)
        self.FormNama.setGeometry(QtCore.QRect(20, 110, 331, 31))
        self.FormNama.setObjectName("FormNama")
        self.LabelNama = QtWidgets.QLabel(Form)
        self.LabelNama.setGeometry(QtCore.QRect(20, 90, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelNama.setFont(font)
        self.LabelNama.setObjectName("LabelNama")
        self.LabelAlamat = QtWidgets.QLabel(Form)
        self.LabelAlamat.setGeometry(QtCore.QRect(20, 160, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelAlamat.setFont(font)
        self.LabelAlamat.setObjectName("LabelAlamat")
        self.LineAlamat = QtWidgets.QLineEdit(Form)
        self.LineAlamat.setGeometry(QtCore.QRect(20, 180, 331, 71))
        self.LineAlamat.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.LineAlamat.setObjectName("LineAlamat")
        self.LabelKamar = QtWidgets.QLabel(Form)
        self.LabelKamar.setGeometry(QtCore.QRect(20, 270, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelKamar.setFont(font)
        self.LabelKamar.setObjectName("LabelKamar")
        self.RadioEkonomi = QtWidgets.QRadioButton(Form)
        self.RadioEkonomi.setGeometry(QtCore.QRect(140, 290, 112, 23))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.RadioEkonomi.setFont(font)
        self.RadioEkonomi.setObjectName("RadioEkonomi")
        self.RadioEkonomi.toggled.connect(lambda:self.clickedRadio(self.RadioEkonomi))
        self.RadioVVIP = QtWidgets.QRadioButton(Form)
        self.RadioVVIP.setGeometry(QtCore.QRect(70, 290, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.RadioVVIP.setFont(font)
        self.RadioVVIP.setObjectName("RadioVVIP")
        self.RadioVVIP.toggled.connect(lambda:self.clickedRadio(self.RadioVVIP))
        self.DateIn = QtWidgets.QDateEdit(Form)
        self.DateIn.setGeometry(QtCore.QRect(20, 350, 110, 26))
        self.DateIn.setMinimumDate(QtCore.QDate(self.datetime.year, self.datetime.month, self.datetime.day))
        self.DateIn.setObjectName("DateIn")
        self.LabelTanggalIn = QtWidgets.QLabel(Form)
        self.LabelTanggalIn.setGeometry(QtCore.QRect(20, 330, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelTanggalIn.setFont(font)
        self.LabelTanggalIn.setObjectName("LabelTanggalIn")
        self.LabelTanggalOut = QtWidgets.QLabel(Form)
        self.LabelTanggalOut.setGeometry(QtCore.QRect(20, 390, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelTanggalOut.setFont(font)
        self.LabelTanggalOut.setObjectName("LabelTanggalOut")
        self.DateOut = QtWidgets.QDateEdit(Form)
        self.DateOut.setGeometry(QtCore.QRect(20, 410, 110, 26))
        self.DateOut.setMinimumDate(QtCore.QDate(self.datetime.year, self.datetime.month, self.datetime.day, ))
        self.DateOut.setObjectName("DateOut")
        self.LabelHarga = QtWidgets.QLabel(Form)
        self.LabelHarga.setGeometry(QtCore.QRect(20, 450, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.LabelHarga.setFont(font)
        self.LabelHarga.setObjectName("LabelHarga")
        self.FormHarga = QtWidgets.QLabel(Form)
        self.FormHarga.setGeometry(QtCore.QRect(150, 450, 191, 17))
        self.FormHarga.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FormHarga.setObjectName("FormHarga")
        self.BtnEdit = QtWidgets.QPushButton(Form)
        self.BtnEdit.setGeometry(QtCore.QRect(20, 480, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.BtnEdit.setFont(font)
        self.BtnEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnEdit.setStyleSheet("QPushButton{\n"
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
        self.BtnEdit.setObjectName("BtnEdit")
        self.BtnEdit.clicked.connect(self.ClickedEdit)
        self.BtnDelete = QtWidgets.QPushButton(Form)
        self.BtnDelete.setGeometry(QtCore.QRect(190, 480, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.BtnDelete.setFont(font)
        self.BtnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnDelete.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 150, 136);\n"
"color:white;\n"
"border-style:outset;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(204, 0, 0);\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color:rgb(0, 150, 136);\n"
"}")
        self.BtnDelete.setObjectName("BtnDelete")
        self.BtnDelete.clicked.connect(self.ClickedDelete)
        self.FormNoKamar = QtWidgets.QLineEdit(Form)
        self.FormNoKamar.setGeometry(QtCore.QRect(20, 290, 41, 25))
        self.FormNoKamar.setObjectName("FormNoKamar")
        self.BtnExit = QtWidgets.QPushButton(Form)
        self.BtnExit.setGeometry(QtCore.QRect(190, 540, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.BtnExit.setFont(font)
        self.BtnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnExit.setStyleSheet("QPushButton{\n"
"background-color: rgb(204, 0, 0);\n"
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
"border-color:rgb(204, 0, 0);\n"
"}")
        self.BtnExit.setObjectName("BtnExit")
        self.BtnExit.clicked.connect(self.ClickedExit)
        self.BtnReload = QtWidgets.QPushButton(Form)
        self.BtnReload.setGeometry(QtCore.QRect(20, 540, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.BtnReload.setFont(font)
        self.BtnReload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnReload.setStyleSheet("QPushButton{\n"
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
        self.BtnReload.setObjectName("BtnReload")
        self.BtnReload.clicked.connect(self.ClickedReload)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.TableInform.horizontalHeaderItem(0)
        item.setText(_translate("Form", "No. Kamar"))
        item = self.TableInform.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama"))
        item = self.TableInform.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Alamat"))
        item = self.TableInform.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Jenis Kamar"))
        item = self.TableInform.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tanggal In"))
        item = self.TableInform.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Tanggal Out"))
        item = self.TableInform.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Harga"))
        self.LabelTittle.setText(_translate("Form", "FORM EDIT HOTEL MELATI"))
        self.LabelNama.setText(_translate("Form", "Nama :"))
        self.LabelAlamat.setText(_translate("Form", "Alamat :"))
        self.LabelKamar.setText(_translate("Form", "No & Jenis Kamar :"))
        self.RadioEkonomi.setText(_translate("Form", "Ekonomi"))
        self.RadioVVIP.setText(_translate("Form", "VVIP"))
        self.LabelTanggalIn.setText(_translate("Form", "Tanggal In :"))
        self.LabelTanggalOut.setText(_translate("Form", "Tanggal Out :"))
        self.LabelHarga.setText(_translate("Form", "Harga :"))
        self.BtnEdit.setText(_translate("Form", "EDIT"))
        self.BtnDelete.setText(_translate("Form", "DELETE"))
        self.BtnExit.setText(_translate("Form", "EXIT APP"))
        self.BtnReload.setText(_translate("Form", "RELOAD"))

    def show_message(self, title="text", message="text"):
        QtWidgets.QMessageBox.information(None, title, message)

    def ReloadData(self):
        db = mysql.connector.connect(user="root", database="Hotel")
        cursor = db.cursor()

        query = ("SELECT `Kamar`.`no_kamar`, `Tamu`.`nama_tamu`, `Tamu`.`alamat`, `Kamar`.`jenis_kamar`, `Transaksi`.`tanggal_in`, `Transaksi`.`tanggal_out`, `Transaksi`.`jumlah` FROM Transaksi, Kamar, Tamu WHERE Kamar.no_kamar = Transaksi.no_kamarFK AND Tamu.id_tamu = Transaksi.id_tamuFK")
        cursor.execute(query)

        self.TableInform.setRowCount(0)
        for row_number, row_data in enumerate(cursor):
            self.TableInform.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.TableInform.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        
        db.commit()
        cursor.close()
        db.close()

    def ClickedReload(self):
        self.ReloadData()
        self.show_message("Reload Data", "Reload Data Selesai")

    def SelectedItems(self):
        return self.TableInform.item(self.TableInform.currentRow(), 0).text()

    def clickedRadio(self, b):
        _translate = QtCore.QCoreApplication.translate
        self.infoRadio = ""
        radioButton = b.sender()
        if radioButton.isChecked():
            if radioButton.text() == "Ekonomi":
                self.infoRadio = radioButton.text()
                self.FormHarga.setText(_translate("Form", "Rp. 300.000,00"))
            else :
                self.infoRadio = radioButton.text()
                self.FormHarga.setText(_translate("Form", "Rp. 400.000,00"))

    def InsertData(self):
        _translate = QtCore.QCoreApplication.translate

        selected_item = (self.TableInform.currentRow())
        nama = self.TableInform.item(selected_item, 1).text()
        alamat = self.TableInform.item(selected_item, 2).text()
        no_kamar = self.TableInform.item(selected_item, 0).text()
        Tanggal_In = self.TableInform.item(selected_item, 4).text()
        Tanggal_Out = self.TableInform.item(selected_item, 5).text()
        jenis_kamar = self.TableInform.item(selected_item, 3).text()

        YearIn = Tanggal_In.split("-")[0]
        MonthIn = Tanggal_In.split("-")[1]
        DayIn = Tanggal_In.split("-")[2]

        YearOut = Tanggal_Out.split("-")[0]
        MontOut = Tanggal_Out.split("-")[1]
        DayOut = Tanggal_Out.split("-")[2]

        self.FormNama.setText(nama)
        self.LineAlamat.setText(alamat)
        self.FormNoKamar.setText(no_kamar)
        self.DateIn.setDate(QtCore.QDate(int(YearIn), int(MonthIn), int(DayIn)))
        self.DateOut.setDate(QtCore.QDate(int(YearOut), int(MontOut), int(DayOut)))
        if jenis_kamar == "Ekonomi":
            self.RadioEkonomi.setChecked(True)
            self.FormHarga.setText(_translate("Form", "Rp. 300.000,00"))
        else :
            self.FormHarga.setText(_translate("Form", "Rp. 400.000,00"))
            self.RadioVVIP.setChecked(True)

    def ClickedEdit(self):
        conn = pymysql.connect(user="root", db="Hotel", autocommit=True)
        cursor = conn.cursor()

        query = ("SELECT id_transaksi, id_tamuFK, no_kamarFK FROM Transaksi WHERE no_kamarFK = %s")
        cursor.execute(query, self.SelectedItems())

        id_transaksi = 0
        id_tamu = 0
        id_kamar = 0

        for (id_data1, id_data2, id_data3) in cursor:
            id_transaksi = int(id_data1)
            id_tamu = int(id_data2)
            id_kamar = int(id_data3)

        DateIn = self.DateIn.text()
        DayIn = DateIn.split("/")[0]
        MonthIn = DateIn.split("/")[1]
        YearIn = DateIn.split("/")[2]

        DateOut = self.DateOut.text()
        DayOut = DateOut.split("/")[0]
        MonthOut = DateOut.split("/")[1]
        YearOut = DateOut.split("/")[2]

        harga = 0
        if self.infoRadio == "Ekonomi":
            harga = 300000
        else :
            harga = 400000

        query2 = ("UPDATE Tamu SET nama_tamu = %s, alamat = %s WHERE id_tamu = %s")
        cursor.execute(query2, (self.FormNama.text(), self.LineAlamat.text(), id_tamu))
        query3 = ("UPDATE Kamar SET jenis_kamar = %s WHERE no_kamar = %s")
        cursor.execute(query3, (self.infoRadio, id_kamar))
        query4 = ("UPDATE Kamar SET no_kamar = %s WHERE no_kamar = %s")
        cursor.execute(query4, (self.FormNoKamar.text(), id_kamar))
        query5 = ("UPDATE Transaksi SET no_kamarFK = %s, tanggal_in = %s, tanggal_out = %s, jumlah = %s WHERE id_transaksi = %s")
        cursor.execute(query5, (self.FormNoKamar.text(), "20"+YearIn+"-"+MonthIn+"-"+DayIn, "20"+YearOut+"-"+MonthOut+"-"+DayOut, harga, id_transaksi))

        cursor.close()
        conn.close()

        self.ReloadData()
        self.show_message("Edit Data", "Edit Data Selesai")

    def ClickedDelete(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Delete Data")
        msg.setText("Are you sure delete this data?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.DeleteData)

        x = msg.exec_()

    def DeleteData(self, i):
        if i.text() == "&Yes":
            conn = pymysql.connect(user="root", db="Hotel", autocommit=True)
            cursor = conn.cursor()

            query = ("SELECT id_transaksi, id_tamuFK, no_kamarFK FROM Transaksi WHERE no_kamarFK = %s")
            cursor.execute(query, self.SelectedItems())

            id_transaksi = 0
            id_tamu = 0
            id_kamar = 0

            for (id_data1, id_data2, id_data3) in cursor:
                id_transaksi = int(id_data1)
                id_tamu = int(id_data2)
                id_kamar = int(id_data3)

            query2 = ("DELETE FROM Transaksi WHERE id_transaksi = %s")
            cursor.execute(query2, id_transaksi)
            query3 = ("DELETE FROM Tamu WHERE id_tamu = %s")
            cursor.execute(query3, id_tamu)
            query4 = ("DELETE FROM Kamar WHERE no_kamar = %s")
            cursor.execute(query4, id_kamar)

            cursor.close()
            conn.close()

            self.ReloadData()

    def ClickedExit(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Exit Aplication")
        msg.setText("Are you sure exit?")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Yes)
        msg.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msg.buttonClicked.connect(self.LogOut)

        x = msg.exec_()

    def LogOut(self, i):
        if i.text() == "&Yes":
            QtWidgets.QApplication.quit()
