# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eowmsdialog.ui'
#
# Created by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EOWMSDialog(object):
    def setupUi(self, EOWMSDialog):
        EOWMSDialog.setObjectName(_fromUtf8("EOWMSDialog"))
        EOWMSDialog.resize(400, 441)
        self.formLayoutWidget = QtGui.QWidget(EOWMSDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(19, 19, 361, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_url = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_url.setObjectName(_fromUtf8("lineEdit_url"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_url)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_layers = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_layers.setObjectName(_fromUtf8("lineEdit_layers"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_layers)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.dateTimeEdit_startTime = QtGui.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit_startTime.setObjectName(_fromUtf8("dateTimeEdit_startTime"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.dateTimeEdit_startTime)
        self.dateTimeEdit_endTime = QtGui.QDateTimeEdit(self.formLayoutWidget)
        self.dateTimeEdit_endTime.setObjectName(_fromUtf8("dateTimeEdit_endTime"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.dateTimeEdit_endTime)
        self.horizontalLayoutWidget = QtGui.QWidget(EOWMSDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 129, 361, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_createLayer = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_createLayer.setObjectName(_fromUtf8("pushButton_createLayer"))
        self.horizontalLayout.addWidget(self.pushButton_createLayer)
        self.pushButton_exit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.textBrowser_log = QtGui.QTextBrowser(EOWMSDialog)
        self.textBrowser_log.setGeometry(QtCore.QRect(20, 190, 361, 231))
        self.textBrowser_log.setObjectName(_fromUtf8("textBrowser_log"))

        self.retranslateUi(EOWMSDialog)
        QtCore.QMetaObject.connectSlotsByName(EOWMSDialog)

    def retranslateUi(self, EOWMSDialog):
        EOWMSDialog.setWindowTitle(QtGui.QApplication.translate("EOWMSDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EOWMSDialog", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("EOWMSDialog", "Layer(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("EOWMSDialog", "Start Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("EOWMSDialog", "End Time", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_createLayer.setText(QtGui.QApplication.translate("EOWMSDialog", "Create WMS Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exit.setText(QtGui.QApplication.translate("EOWMSDialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))

