# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../UI_Files/DDLAlter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DDLALTER(object):
    def setupUi(self, DDLALTER):
        DDLALTER.setObjectName("DDLALTER")
        DDLALTER.resize(838, 557)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DDLALTER)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.alter_dbname = QtWidgets.QTextEdit(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_dbname.sizePolicy().hasHeightForWidth())
        self.alter_dbname.setSizePolicy(sizePolicy)
        self.alter_dbname.setObjectName("alter_dbname")
        self.horizontalLayout.addWidget(self.alter_dbname)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(DDLALTER)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.alter_dbtable = QtWidgets.QTextEdit(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_dbtable.sizePolicy().hasHeightForWidth())
        self.alter_dbtable.setSizePolicy(sizePolicy)
        self.alter_dbtable.setObjectName("alter_dbtable")
        self.horizontalLayout_8.addWidget(self.alter_dbtable)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(700, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.alter_alterbutton = QtWidgets.QPushButton(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_alterbutton.sizePolicy().hasHeightForWidth())
        self.alter_alterbutton.setSizePolicy(sizePolicy)
        self.alter_alterbutton.setObjectName("alter_alterbutton")
        self.horizontalLayout_7.addWidget(self.alter_alterbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.alter_columnname = QtWidgets.QTextEdit(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_columnname.sizePolicy().hasHeightForWidth())
        self.alter_columnname.setSizePolicy(sizePolicy)
        self.alter_columnname.setObjectName("alter_columnname")
        self.horizontalLayout_6.addWidget(self.alter_columnname)
        spacerItem9 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.label_4 = QtWidgets.QLabel(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem11 = QtWidgets.QSpacerItem(65, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.alter_datatype = QtWidgets.QComboBox(DDLALTER)
        self.alter_datatype.setEditable(False)
        self.alter_datatype.setObjectName("alter_datatype")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.alter_datatype.addItem("")
        self.horizontalLayout_5.addWidget(self.alter_datatype)
        self.label_5 = QtWidgets.QLabel(DDLALTER)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem12 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.label_6 = QtWidgets.QLabel(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem14 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.alter_constraint = QtWidgets.QComboBox(DDLALTER)
        self.alter_constraint.setObjectName("alter_constraint")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.alter_constraint.addItem("")
        self.horizontalLayout_4.addWidget(self.alter_constraint)
        self.label_7 = QtWidgets.QLabel(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem15 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.alter_addbutton = QtWidgets.QPushButton(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_addbutton.sizePolicy().hasHeightForWidth())
        self.alter_addbutton.setSizePolicy(sizePolicy)
        self.alter_addbutton.setObjectName("alter_addbutton")
        self.horizontalLayout_3.addWidget(self.alter_addbutton)
        spacerItem16 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.alter_dropbutton = QtWidgets.QPushButton(DDLALTER)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alter_dropbutton.sizePolicy().hasHeightForWidth())
        self.alter_dropbutton.setSizePolicy(sizePolicy)
        self.alter_dropbutton.setObjectName("alter_dropbutton")
        self.horizontalLayout_3.addWidget(self.alter_dropbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DDLALTER)
        QtCore.QMetaObject.connectSlotsByName(DDLALTER)

    def retranslateUi(self, DDLALTER):
        _translate = QtCore.QCoreApplication.translate
        DDLALTER.setWindowTitle(_translate("DDLALTER", "Alter"))
        self.label.setText(_translate("DDLALTER", "Database Name:"))
        self.label_2.setText(_translate("DDLALTER", "Table Name:"))
        self.alter_alterbutton.setText(_translate("DDLALTER", "Select"))
        self.label_3.setText(_translate("DDLALTER", "Column Name:"))
        self.label_4.setText(_translate("DDLALTER", "Data Type:"))
        self.alter_datatype.setItemText(0, _translate("DDLALTER", "INTEGER"))
        self.alter_datatype.setItemText(1, _translate("DDLALTER", "VARCHAR"))
        self.alter_datatype.setItemText(2, _translate("DDLALTER", "TEXT"))
        self.alter_datatype.setItemText(3, _translate("DDLALTER", "BLOB"))
        self.alter_datatype.setItemText(4, _translate("DDLALTER", "BOOLEAN"))
        self.alter_datatype.setItemText(5, _translate("DDLALTER", "TINYINT"))
        self.alter_datatype.setItemText(6, _translate("DDLALTER", "SMALLINT"))
        self.alter_datatype.setItemText(7, _translate("DDLALTER", "BIGINT"))
        self.alter_datatype.setItemText(8, _translate("DDLALTER", "HUGEINT"))
        self.alter_datatype.setItemText(9, _translate("DDLALTER", "DECIMAL"))
        self.alter_datatype.setItemText(10, _translate("DDLALTER", "REAL"))
        self.alter_datatype.setItemText(11, _translate("DDLALTER", "FLOAT"))
        self.alter_datatype.setItemText(12, _translate("DDLALTER", "DOUBLE"))
        self.label_5.setText(_translate("DDLALTER", "Hint: Integer/Char"))
        self.label_6.setText(_translate("DDLALTER", "Constraint:"))
        self.alter_constraint.setItemText(0, _translate("DDLALTER", "PRIMARY KEY"))
        self.alter_constraint.setItemText(1, _translate("DDLALTER", "CHECK"))
        self.alter_constraint.setItemText(2, _translate("DDLALTER", "UNIQUE"))
        self.alter_constraint.setItemText(3, _translate("DDLALTER", "FOREIGN KEY"))
        self.alter_constraint.setItemText(4, _translate("DDLALTER", "NOT NULL"))
        self.alter_constraint.setItemText(5, _translate("DDLALTER", "DEFAULT"))
        self.alter_constraint.setItemText(6, _translate("DDLALTER", "INDEX"))
        self.label_7.setText(_translate("DDLALTER", "Hint: Primary Key"))
        self.alter_addbutton.setText(_translate("DDLALTER", "ADD COLUMN"))
        self.alter_dropbutton.setText(_translate("DDLALTER", "DROP COLUMN"))

