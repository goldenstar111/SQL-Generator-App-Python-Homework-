# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/mainwork.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDlg(object):
    def setupUi(self, MainDlg):
        MainDlg.setObjectName("MainDlg")
        MainDlg.resize(1070, 705)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainDlg.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(MainDlg)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(MainDlg)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(MainDlg)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./ui\\ER_1.png"))
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 11)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(MainDlg)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(MainDlg)
        self.tableWidget.setEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(16, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(17, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(18, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(19, 2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.rdbtn1 = QtWidgets.QRadioButton(MainDlg)
        self.rdbtn1.setChecked(True)
        self.rdbtn1.setObjectName("rdbtn1")
        self.verticalLayout_6.addWidget(self.rdbtn1)
        self.rdbtn2 = QtWidgets.QRadioButton(MainDlg)
        self.rdbtn2.setObjectName("rdbtn2")
        self.verticalLayout_6.addWidget(self.rdbtn2)
        self.rdbtn3 = QtWidgets.QRadioButton(MainDlg)
        self.rdbtn3.setObjectName("rdbtn3")
        self.verticalLayout_6.addWidget(self.rdbtn3)
        self.btn_pr_add = QtWidgets.QPushButton(MainDlg)
        self.btn_pr_add.setObjectName("btn_pr_add")
        self.verticalLayout_6.addWidget(self.btn_pr_add)
        self.btn_pr_del = QtWidgets.QPushButton(MainDlg)
        self.btn_pr_del.setObjectName("btn_pr_del")
        self.verticalLayout_6.addWidget(self.btn_pr_del)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 7)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.label_5 = QtWidgets.QLabel(MainDlg)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(MainDlg)
        self.tableWidget_2.setEnabled(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(5, 4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)
        self.horizontalLayout_2.addWidget(self.tableWidget_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_fk_add = QtWidgets.QPushButton(MainDlg)
        self.btn_fk_add.setObjectName("btn_fk_add")
        self.verticalLayout_2.addWidget(self.btn_fk_add)
        self.btn_fk_del = QtWidgets.QPushButton(MainDlg)
        self.btn_fk_del.setObjectName("btn_fk_del")
        self.verticalLayout_2.addWidget(self.btn_fk_del)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_gen_query = QtWidgets.QPushButton(MainDlg)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_gen_query.setFont(font)
        self.btn_gen_query.setObjectName("btn_gen_query")
        self.horizontalLayout_3.addWidget(self.btn_gen_query)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 7)
        self.verticalLayout_3.setStretch(3, 1)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(MainDlg)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 4)
        self.gridLayout.setColumnStretch(1, 7)
        self.gridLayout.setRowStretch(0, 6)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(MainDlg)
        QtCore.QMetaObject.connectSlotsByName(MainDlg)

    def retranslateUi(self, MainDlg):
        _translate = QtCore.QCoreApplication.translate
        MainDlg.setWindowTitle(_translate("MainDlg", "Dialog"))
        self.label_2.setText(_translate("MainDlg", "Demo Table(Data1)"))
        self.label_6.setText(_translate("MainDlg", "Tables"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainDlg", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainDlg", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainDlg", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainDlg", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainDlg", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainDlg", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainDlg", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainDlg", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainDlg", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainDlg", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainDlg", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainDlg", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainDlg", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainDlg", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainDlg", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainDlg", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainDlg", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainDlg", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainDlg", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MainDlg", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainDlg", "T_Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainDlg", "P_Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainDlg", "P_Type"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainDlg", "city_tb"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainDlg", "city_tb"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainDlg", "City_name"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainDlg", "varchar"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainDlg", "email_tb"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainDlg", "email_tb"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainDlg", "Email_addr"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainDlg", "varchar"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainDlg", "job_tb"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainDlg", "job_tb"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainDlg", "job_type"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainDlg", "varchar"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainDlg", "Name"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("MainDlg", "A"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainDlg", "University"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainDlg", "Sex"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("MainDlg", "varchar"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("MainDlg", "Age"))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("MainDlg", "Country"))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("MainDlg", "City"))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("MainDlg", "Email"))
        item = self.tableWidget.item(13, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("MainDlg", "Job"))
        item = self.tableWidget.item(14, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("MainDlg", "university_tb"))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("MainDlg", "Id"))
        item = self.tableWidget.item(15, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("MainDlg", "university_tb"))
        item = self.tableWidget.item(16, 1)
        item.setText(_translate("MainDlg", "university_name"))
        item = self.tableWidget.item(16, 2)
        item.setText(_translate("MainDlg", "varchar"))
        item = self.tableWidget.item(17, 0)
        item.setText(_translate("MainDlg", "university_tb"))
        item = self.tableWidget.item(17, 1)
        item.setText(_translate("MainDlg", "country"))
        item = self.tableWidget.item(17, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(18, 0)
        item.setText(_translate("MainDlg", "country_tb"))
        item = self.tableWidget.item(18, 1)
        item.setText(_translate("MainDlg", "Id"))
        item = self.tableWidget.item(18, 2)
        item.setText(_translate("MainDlg", "int"))
        item = self.tableWidget.item(19, 0)
        item.setText(_translate("MainDlg", "country_tb"))
        item = self.tableWidget.item(19, 1)
        item.setText(_translate("MainDlg", "country_name"))
        item = self.tableWidget.item(19, 2)
        item.setText(_translate("MainDlg", "varchar"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.rdbtn1.setText(_translate("MainDlg", "Data1"))
        self.rdbtn2.setText(_translate("MainDlg", "Data2"))
        self.rdbtn3.setText(_translate("MainDlg", "Manual"))
        self.btn_pr_add.setText(_translate("MainDlg", "add"))
        self.btn_pr_del.setText(_translate("MainDlg", "del"))
        self.label_5.setText(_translate("MainDlg", "Foreign Keys:"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainDlg", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainDlg", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainDlg", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainDlg", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainDlg", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainDlg", "6"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainDlg", "FK"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainDlg", "SRC_T"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainDlg", "SRC_F"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainDlg", "TRG_T"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainDlg", "TRG_F"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainDlg", "f1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainDlg", "University"))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("MainDlg", "university_tb"))
        item = self.tableWidget_2.item(0, 4)
        item.setText(_translate("MainDlg", "Id"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainDlg", "f2"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("MainDlg", "Country"))
        item = self.tableWidget_2.item(1, 3)
        item.setText(_translate("MainDlg", "country_tb"))
        item = self.tableWidget_2.item(1, 4)
        item.setText(_translate("MainDlg", "Id"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainDlg", "f3"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("MainDlg", "Email"))
        item = self.tableWidget_2.item(2, 3)
        item.setText(_translate("MainDlg", "email_tb"))
        item = self.tableWidget_2.item(2, 4)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("MainDlg", "f4"))
        item = self.tableWidget_2.item(3, 1)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget_2.item(3, 2)
        item.setText(_translate("MainDlg", "Job"))
        item = self.tableWidget_2.item(3, 3)
        item.setText(_translate("MainDlg", "job_tb"))
        item = self.tableWidget_2.item(3, 4)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget_2.item(4, 0)
        item.setText(_translate("MainDlg", "f5"))
        item = self.tableWidget_2.item(4, 1)
        item.setText(_translate("MainDlg", "user_tb"))
        item = self.tableWidget_2.item(4, 2)
        item.setText(_translate("MainDlg", "City"))
        item = self.tableWidget_2.item(4, 3)
        item.setText(_translate("MainDlg", "city_tb"))
        item = self.tableWidget_2.item(4, 4)
        item.setText(_translate("MainDlg", "ID"))
        item = self.tableWidget_2.item(5, 0)
        item.setText(_translate("MainDlg", "f6"))
        item = self.tableWidget_2.item(5, 1)
        item.setText(_translate("MainDlg", "university_tb"))
        item = self.tableWidget_2.item(5, 2)
        item.setText(_translate("MainDlg", "country"))
        item = self.tableWidget_2.item(5, 3)
        item.setText(_translate("MainDlg", "country_tb"))
        item = self.tableWidget_2.item(5, 4)
        item.setText(_translate("MainDlg", "Id"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.btn_fk_add.setText(_translate("MainDlg", "add"))
        self.btn_fk_del.setText(_translate("MainDlg", "del"))
        self.btn_gen_query.setText(_translate("MainDlg", "Generate Query"))
