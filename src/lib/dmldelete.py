# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI_Files/DMLDelete.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DMLDELETE(object):
    def setupUi(self, DMLDELETE):
        DMLDELETE.setObjectName("DMLDELETE")
        DMLDELETE.resize(922, 610)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DMLDELETE)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(DMLDELETE)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.delete_dbname = QtWidgets.QTextEdit(DMLDELETE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_dbname.sizePolicy().hasHeightForWidth())
        self.delete_dbname.setSizePolicy(sizePolicy)
        self.delete_dbname.setObjectName("delete_dbname")
        self.horizontalLayout.addWidget(self.delete_dbname)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(DMLDELETE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.delete_dbtable = QtWidgets.QTextEdit(DMLDELETE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_dbtable.sizePolicy().hasHeightForWidth())
        self.delete_dbtable.setSizePolicy(sizePolicy)
        self.delete_dbtable.setObjectName("delete_dbtable")
        self.horizontalLayout_3.addWidget(self.delete_dbtable)
        spacerItem5 = QtWidgets.QSpacerItem(101, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(700, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.delete_selectbutton = QtWidgets.QPushButton(DMLDELETE)
        self.delete_selectbutton.setObjectName("delete_selectbutton")
        self.horizontalLayout_7.addWidget(self.delete_selectbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.delete_tableview = QtWidgets.QTableWidget(DMLDELETE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_tableview.sizePolicy().hasHeightForWidth())
        self.delete_tableview.setSizePolicy(sizePolicy)
        self.delete_tableview.setObjectName("delete_tableview")
        self.delete_tableview.setColumnCount(0)
        self.delete_tableview.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.delete_tableview)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(700, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.delete_deletebutton = QtWidgets.QPushButton(DMLDELETE)
        self.delete_deletebutton.setObjectName("delete_deletebutton")
        self.horizontalLayout_5.addWidget(self.delete_deletebutton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DMLDELETE)
        QtCore.QMetaObject.connectSlotsByName(DMLDELETE)

    def retranslateUi(self, DMLDELETE):
        _translate = QtCore.QCoreApplication.translate
        DMLDELETE.setWindowTitle(_translate("DMLDELETE", "Delete"))
        self.label.setText(_translate("DMLDELETE", "Database Name:"))
        self.label_2.setText(_translate("DMLDELETE", "Table Name:"))
        self.delete_selectbutton.setText(_translate("DMLDELETE", "SELECT"))
        self.delete_deletebutton.setText(_translate("DMLDELETE", "DELETE"))
