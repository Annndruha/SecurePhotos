# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterkey.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterKey(object):
    def setupUi(self, EnterKey):
        EnterKey.setObjectName("EnterKey")
        font = QtGui.QFont()
        font.setPointSize(10)
        EnterKey.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EnterKey.setWindowIcon(icon)
        EnterKey.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EnterKey)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_cur_name = QtWidgets.QLabel(EnterKey)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cur_name.setFont(font)
        self.label_cur_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_cur_name.setObjectName("label_cur_name")
        self.horizontalLayout.addWidget(self.label_cur_name)
        self.keyField = QtWidgets.QLineEdit(EnterKey)
        self.keyField.setObjectName("keyField")
        self.horizontalLayout.addWidget(self.keyField)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(EnterKey)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(EnterKey)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_apply = QtWidgets.QPushButton(EnterKey)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.gridLayout_2.addWidget(self.pushButton_apply, 0, 2, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(EnterKey)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_2.addWidget(self.pushButton_cancel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.retranslateUi(EnterKey)
        QtCore.QMetaObject.connectSlotsByName(EnterKey)

    def retranslateUi(self, EnterKey):
        _translate = QtCore.QCoreApplication.translate
        EnterKey.setWindowTitle(_translate("EnterKey", "Enter Key"))
        self.label_cur_name.setText(_translate("EnterKey", "Enter password:"))
        self.label.setText(_translate("EnterKey", "This password used for encryption and decryption your files."))
        self.label_2.setText(_translate("EnterKey", "It will be lost after close app!"))
        self.pushButton_apply.setText(_translate("EnterKey", "Apply"))
        self.pushButton_cancel.setText(_translate("EnterKey", "Cancel"))
