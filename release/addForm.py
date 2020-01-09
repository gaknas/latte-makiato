# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 204)
        self.change = QtWidgets.QPushButton(Form)
        self.change.setGeometry(QtCore.QRect(4, 2, 281, 51))
        self.change.setObjectName("change")
        self.add = QtWidgets.QPushButton(Form)
        self.add.setGeometry(QtCore.QRect(4, 52, 281, 51))
        self.add.setObjectName("add")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 481, 81))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(290, 70, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 10, 201, 51))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.change.setText(_translate("Form", "ИЗМЕНИТЬ"))
        self.add.setText(_translate("Form", "ДОБАВИТЬ"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "new"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "название сорта"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "степень обжарки"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "молотый/в зёрнах"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "описание вкуса"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "цена"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "объём упаковки в граммах"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "какой изменить или\n"
" каким по счёту добавить"))
