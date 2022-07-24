# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'name_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NameDialog(object):
    def setupUi(self, NameDialog):
        NameDialog.setObjectName("NameDialog")
        NameDialog.resize(720, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NameDialog.sizePolicy().hasHeightForWidth())
        NameDialog.setSizePolicy(sizePolicy)
        NameDialog.setMinimumSize(QtCore.QSize(720, 250))
        NameDialog.setMaximumSize(QtCore.QSize(720, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        NameDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NameDialog.setWindowIcon(icon)
        NameDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayoutWidget = QtWidgets.QWidget(NameDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 701, 151))
        self.verticalLayoutWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_cur_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_cur_name.setFont(font)
        self.label_cur_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_cur_name.setObjectName("label_cur_name")
        self.verticalLayout.addWidget(self.label_cur_name)
        self.lineEdit_cur_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cur_name.setFont(font)
        self.lineEdit_cur_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_cur_name.setReadOnly(True)
        self.lineEdit_cur_name.setObjectName("lineEdit_cur_name")
        self.verticalLayout.addWidget(self.lineEdit_cur_name)
        self.label_new_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_new_name.setFont(font)
        self.label_new_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_new_name.setObjectName("label_new_name")
        self.verticalLayout.addWidget(self.label_new_name)
        self.lineEdit_new_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_new_name.setFont(font)
        self.lineEdit_new_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lineEdit_new_name.setObjectName("lineEdit_new_name")
        self.verticalLayout.addWidget(self.lineEdit_new_name)
        self.horizontalLayoutWidget = QtWidgets.QWidget(NameDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 170, 701, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_skip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_skip.setFont(font)
        self.pushButton_skip.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_skip.setObjectName("pushButton_skip")
        self.horizontalLayout.addWidget(self.pushButton_skip)
        self.pushButton_apply = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_apply.setFont(font)
        self.pushButton_apply.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)

        self.retranslateUi(NameDialog)
        QtCore.QMetaObject.connectSlotsByName(NameDialog)

    def retranslateUi(self, NameDialog):
        _translate = QtCore.QCoreApplication.translate
        NameDialog.setWindowTitle(_translate("NameDialog", "Manual rename"))
        self.label_cur_name.setText(_translate("NameDialog", "Current name:"))
        self.label_new_name.setText(_translate("NameDialog", "New name:"))
        self.pushButton_cancel.setText(_translate("NameDialog", "Cancel"))
        self.pushButton_skip.setText(_translate("NameDialog", "Skip"))
        self.pushButton_apply.setText(_translate("NameDialog", "Apply"))
