#!/usr/bin/python

import sys
import os
import threading
import queue
import logging
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*

logger = logging.getLogger(__name__)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.relpath(os.getcwd() + '/lib'))
from mdvisual import Ui_MainWindow
from ddlalter import Ui_DDLALTER
from ddldrop import Ui_DDLDROP
from ddlcreate import Ui_DDLCREATE
from dmlinsert import Ui_DMLINSERT
from dmldelete import Ui_DMLDELETE
from dmlupdate import Ui_DMLUPDATE
from monetdb_interface import MONETDBINTERFACE

class DMLINSERT(QDialog,Ui_DMLINSERT):

    sigSelect = pyqtSignal()
    sigInsert = pyqtSignal()

    def __init__(self,monetdbobject):
        super(DMLINSERT,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.insert_selectbutton.clicked.connect(self.clickedSelect)
        self.insert_insertbutton.clicked.connect(self.clickedInsert)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigSelect.connect(self.insert_selectDBCallback)
        self.sigInsert.connect(self.insert_insertDBCallback)
        #self.insert_tableview.itemChanged.connect(self.selectCelldata)
        self.insert_tableview.itemSelectionChanged.connect(self.selectCelldata)

    def clickedInsert(self):
        """
        Callback function for INSERT Click Event
        """
        self.sigInsert.emit()

    def clickedSelect(self):
        """
        Callback function for SELECT Click Event
        """
        self.sigSelect.emit()

    def insert_selectDBCallback(self):
        """
        Callback function for Select button on Insert Page
        """
        self.databaseName = self.insert_dbname.toPlainText()
        self.tableName = self.insert_dbtable.toPlainText()
        data = self.monetdbobj.runQuery('select* from {}'.format(self.tableName))
        self.col_names = [i[0] for i in self.monetdbobj.cursor.description]
        self.insert_tableview.setRowCount(0)
        self.insert_tableview.setColumnCount(len(self.col_names))
        self.insert_tableview.verticalHeader().setVisible(True)
        self.insert_tableview.setHorizontalHeaderLabels(self.col_names)
        self.insert_tableview.insertRow(0)
        self.insert_tableview.clearContents()

    def selectCelldata(self):
        """
        Callback function for delete selected value from database
        """
        self.data_in = []
        self.col = []
        for item in self.insert_tableview.selectedItems():
            self.val = item.text()
            if self.val.isdigit():
                self.val = int(self.val)
            else:
                self.val = "'" + item.text() + "'"
            self.data_in.append(self.val)

        for item in self.insert_tableview.selectedItems():
            self.col.append(item.column())


    def insert_insertDBCallback(self):
        """
        Callback function for insert button on Insert Page
        """
        self.monetdbobj.runQuery('insert into %s (%s) values (%s)'%(self.tableName,','.join([str(self.col_names[item]) for item in self.col]),','.join([str(item) for item in self.data_in])))

class DMLDELETE(QDialog,Ui_DMLDELETE):
    sigSelect = pyqtSignal()
    sigDelete = pyqtSignal()

    def __init__(self):
        super(DMLDELETE,self).__init__()
        self.setupUi(self)

    def __init__(self,monetdbobject):
        super(DMLDELETE,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.delete_selectbutton.clicked.connect(self.clickedSelect)
        self.delete_deletebutton.clicked.connect(self.clickedDelete)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigSelect.connect(self.delete_selectDBCallback)
        self.sigDelete.connect(self.delete_deleteDBCallback)
        self.delete_tableview.itemSelectionChanged.connect(self.selectCelldata)

    def clickedDelete(self):
        """
        Callback function for INSERT Click Event
        """
        self.sigDelete.emit()

    def clickedSelect(self):
        """
        Callback function for SELECT Click Event
        """
        self.sigSelect.emit()

    def delete_selectDBCallback(self):
        """
        Callback function for Select button on Insert Page
        """
        self.databaseName = self.delete_dbname.toPlainText()
        self.tableName = self.delete_dbtable.toPlainText()
        self.data = self.monetdbobj.runQuery('select* from {}'.format(self.tableName))
        self.col_names = [i[0] for i in self.monetdbobj.cursor.description]
        self.delete_tableview.setRowCount(0)
        self.delete_tableview.setColumnCount(len(self.col_names))
        self.delete_tableview.verticalHeader().setVisible(False)
        self.delete_tableview.setHorizontalHeaderLabels(self.col_names)
        self.delete_tableview.setSelectionMode(QAbstractItemView.MultiSelection)
        for row_number,row_data in enumerate(self.data):
            self.delete_tableview.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.delete_tableview.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def delete_deleteDBCallback(self):
        """
        Callback function for insert button on Insert Page
        """
        self.monetdbobj.runQuery('delete from {} where {} = {}'.format(self.tableName,self.col_names[self.col],self.val))

    def selectCelldata(self):
        """
        Callback function for delete selected value from database
        """
        for item in self.delete_tableview.selectedItems():
            self.val = item.text()
            self.col = item.column()
            self.row = item.row()
            if self.val.isdigit():
                self.val = int(self.val)
            else:
                self.val = "'" + item.text() + "'"

class DMLUPDATE(QDialog,Ui_DMLUPDATE):
    sigSelect = pyqtSignal()
    sigUpdate = pyqtSignal()

    def __init__(self,monetdbobject):
        super(DMLUPDATE,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.update_selectbutton.clicked.connect(self.clickedSelect)
        self.update_updatebutton.clicked.connect(self.clickedUpdate)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigSelect.connect(self.update_selectDBCallback)
        self.sigUpdate.connect(self.update_updateDBCallback)
        #self.update_tableview.itemChanged.connect(self.selectCelldata)
        self.update_tableview.itemSelectionChanged.connect(self.selectCelldata)

    def clickedUpdate(self):
        """
        Callback function for INSERT Click Event
        """
        self.sigUpdate.emit()

    def clickedSelect(self):
        """
        Callback function for SELECT Click Event
        """
        self.sigSelect.emit()

    def update_selectDBCallback(self):
        """
        Callback function for Select button on Insert Page
        """
        self.databaseName = self.update_dbname.toPlainText()
        self.tableName = self.update_dbtable.toPlainText()
        self.data = self.monetdbobj.runQuery('select* from {}'.format(self.tableName))
        self.col_names = [i[0] for i in self.monetdbobj.cursor.description]
        self.update_tableview.setRowCount(0)
        self.update_tableview.setColumnCount(len(self.col_names))
        self.update_tableview.verticalHeader().setVisible(False)
        self.update_tableview.setHorizontalHeaderLabels(self.col_names)
        self.update_tableview.setSelectionMode(QAbstractItemView.MultiSelection)
        for row_number,row_data in enumerate(self.data):
            self.update_tableview.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.update_tableview.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def update_updateDBCallback(self):
        """
        Callback function for insert button on Insert Page
        """
        if len(self.data_in) >= 2:
            self.monetdbobj.runQuery("update {} set {} = {} where {} = {}".format(self.tableName,self.col_names[self.data_in[0][1]],self.data_in[0][0],self.col_names[self.data_in[1][1]],self.data_in[1][0]))

    def selectCelldata(self):
        """
        Callback function for delete selected value from database
        """
        self.data_in = []
        for item in self.update_tableview.selectedItems():
            self.val = item.text()
            if self.val.isdigit():
                self.val = int(self.val)
            else:
                self.val = "'" + item.text() + "'"
            self.data_in.append((self.val,item.column(),item.row()))

class DDLALTER(QDialog,Ui_DDLALTER):
    sigAlter = pyqtSignal()
    sigAdd = pyqtSignal()
    sigDrop = pyqtSignal()

    def __init__(self,monetdbobject):
        super(DDLALTER,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.alter_alterbutton.clicked.connect(self.clickedAlter)
        self.alter_addbutton.clicked.connect(self.clickedAdd)
        self.alter_dropbutton.clicked.connect(self.clickedDrop)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigAlter.connect(self.alter_alterDBCallback)
        self.sigAdd.connect(self.alter_addDBCallback)
        self.sigDrop.connect(self.alter_dropDBCallback)

    def clickedAlter(self):
        """
        Callback function for Alter button
        """
        self.sigAlter.emit()

    def clickedAdd(self):
        """
        Callback function for Add button
        """
        self.sigAdd.emit()

    def clickedDrop(self):
        """
        Callback function for Drop column
        """
        self.sigDrop.emit()

    def alter_alterDBCallback(self):
        """
        Callback function for Alter
        """
        self.databaseName = self.alter_dbname.toPlainText()
        self.tablename = self.alter_dbtable.toPlainText()

    def alter_addDBCallback(self):
        """
        Callback function for Add
        """
        self.columnname = self.alter_columnname.toPlainText()
        self.datatype = self.alter_datatype.currentText()
        self.constraint = self.alter_constraint.currentText()
        if self.constraint == 'NONE':
            self.monetdbobj.runQuery("alter table {} add {} {}".format(self.tablename,self.columnname,self.datatype))
        else:
            self.monetdbobj.runQuery("alter table {} add {} {} {}".format(self.tablename,self.columnname,self.datatype,self.constraint))


    def alter_dropDBCallback(self):
        """
        Callback function for Drop
        """
        self.columnname = self.alter_columnname.toPlainText()
        self.datatype = self.alter_datatype.currentText()
        self.constraint = self.alter_constraint.currentText()
        self.monetdbobj.runQuery("alter table {} drop {} {}".format(self.tablename,self.columnname,self.datatype))

class DDLDROP(QDialog,Ui_DDLDROP):
    sigDrop = pyqtSignal()
    sigListTables = pyqtSignal()

    def __init__(self,monetdbobject):
        super(DDLDROP,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.drop_dropbutton.clicked.connect(self.clickedDrop)
        self.drop_listtablebutton.clicked.connect(self.clickedListTables)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigDrop.connect(self.drop_dropDBCallback)
        self.sigListTables.connect(self.drop_ListTablesDBCallback)
        self.drop_listview.itemClicked.connect(self.selectListdata)

    def clickedDrop(self):
        """
        Callback function for Drop button
        """
        self.sigDrop.emit()

    def clickedListTables(self):
        """
        Callback function for Add button
        """
        self.sigListTables.emit()

    def selectListdata(self,item):
        """
        Callback function for List Item selection on click
        """
        self.drop_dbname.clear()
        self.tablename = item.text()
        self.drop_dbtable.setText(self.tablename)

    def drop_dropDBCallback(self):
        """
        Callback function for Drop
        """
        self.monetdbobj.runQuery("drop table {}".format(self.tablename))
        self.drop_dbname.clear()

    def drop_ListTablesDBCallback(self):
        """
        Callback function for Add
        """
        self.drop_listview.clear()
        self.databaseName = self.drop_dbname.toPlainText()
        if self.databaseName:
            tables = self.monetdbobj.runQuery("select t.name from sys.tables t where t.system=false")
            lst = [x[0] for x in tables]
            for item in lst:
                self.drop_listview.addItem(item)
        
class DDLCREATE(QDialog,Ui_DDLCREATE):
    sigCreate = pyqtSignal()
    sigAdd = pyqtSignal()

    def __init__(self,monetdbobject):
        super(DDLCREATE,self).__init__()
        self.setupUi(self)
        self.monetdbobj = monetdbobject
        self.create_createbutton.clicked.connect(self.clickedCreate)
        self.create_addbutton.clicked.connect(self.clickedAdd)

    def initWidget(self):
        """
        Widget Initialization for Insert
        """
        self.sigCreate.connect(self.create_createDBCallback)
        self.sigAdd.connect(self.create_addDBCallback)

    def clickedCreate(self):
        """
        Callback function for Drop button
        """
        self.sigCreate.emit()

    def clickedAdd(self):
        """
        Callback function for Add button
        """
        self.sigAdd.emit()

    def create_createDBCallback(self):
        """
        Callback function for Drop
        """
        self.databaseName = self.create_dbname.toPlainText()
        self.tablename = self.create_dbtable.toPlainText()

    def create_addDBCallback(self):
        """
        Callback function for Add
        """
        self.columnname = self.create_columnname.toPlainText()
        self.datatype = self.create_datatype.currentText()
        self.constraint = self.create_constraint.currentText()
        if self.constraint == 'NONE':
            self.monetdbobj.runQuery("create table if not exists {} ({} {})".format(self.tablename,self.columnname,self.datatype))
        else:
            self.monetdbobj.runQuery("create table if not exists {} ({} {} {})".format(self.tablename,self.columnname,self.datatype,self.constraint))

class MDVISUAL(QMainWindow,Ui_MainWindow):
    """
    Application class for MDVISUAL GUI.
    """
    sigConnect = pyqtSignal()
    sigCreate = pyqtSignal()
    #sigOpen = pyqtSignal()
    sigDelete = pyqtSignal()
    sigRunQuery = pyqtSignal()

    def __init__(self):
        """
        Class Constructor for initializing GUI
        """
        super(MDVISUAL,self).__init__()
        Ui_MainWindow().__init__()
        self.setupUi(self)
        Ui_DMLDELETE().__init__()
        Ui_DMLUPDATE().__init__()
        Ui_DDLDROP().__init__()
        Ui_DDLALTER().__init__()
        Ui_DDLCREATE().__init__()
        self.setupUi(self)
        self.monetDBObject = MONETDBINTERFACE()
        self.connectDB.clicked.connect(self.clickedConnect)
        self.createDB.clicked.connect(self.clickedCreate)
        #self.openDB.clicked.connect(self.clickedOpen)
        self.deleteDB.clicked.connect(self.clickedDelete)
        self.runQuerytoDB.clicked.connect(self.clickedRunQuery)

    def closeEvent(self,event):
        event.accept()
        self.monetDBObject.rollbackDB()
        print(os.system('monetdb stop {}'.format(self.database)))
        print("Closing...")

    def initWidget(self):
        """
        Function to initialize on-page widgets
        """
        #Button Connect Signals - Callback definitions
        self.sigConnect.connect(self.connectDBCallback)
        self.sigCreate.connect(self.createDBCallback)
        #self.sigOpen.connect(self.openDBCallback)
        self.sigDelete.connect(self.deleteDBCallback)
        self.sigRunQuery.connect(self.runQueryDBCallback)

        #Menubar Connect Signals - Callback definitions
        self.actionConnect_to_DB.triggered.connect(self.connectDBCallback)
        self.actionCreate_DB.triggered.connect(self.createDBCallback)
        self.actionDelete_DB.triggered.connect(self.deleteDBCallback)
        self.actionAdd_New_DB.triggered.connect(self.createDBCallback)
        self.actionInsert.triggered.connect(self.insertDMLCallback)
        self.actionUpdate.triggered.connect(self.updateDMLCallback)
        self.actionDelete.triggered.connect(self.deleteDMLCallback)
        self.actionCreate.triggered.connect(self.createDDLCallback)
        self.actionDrop.triggered.connect(self.dropDDLCallback)
        self.actionAlter.triggered.connect(self.alterDDLCallback)

    def createDBCallback(self):
        """
        Creating Database
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        openfile,_ = QFileDialog.getSaveFileName(self,'Create Database','Database Files (*.db)',options=options)
        datafarm = str(openfile).split("/")[:-1]
        self.database = str(openfile).split("/")[-1]
        path_to_datafarm = "/".join(datafarm)
        try:
            os.system("monetdbd create {}".format(path_to_datafarm))
            os.system("monetdbd start {}".format(path_to_datafarm))
            os.system("monetdb create {}".format(self.database))
            os.system("monetdb release {}".format(self.database))
        except Exception as ex:
            logger.error("MonetDB Create Datafarm Error {} {}".format(type(ex).___name__,ex.args))

    def connectDBCallback(self):
        """
        Connecting to Database
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        openfile,_ = QFileDialog.getSaveFileName(self,'Connect Database','Database Files (*.db)',options=options)
        self.database = str(openfile).split("/")[-1]
        self.monetDBObject.connectDB(self.database)

    #def openDBCallback(self):
    #    """
    #    Open existing Database
    #    """
    #    options = QFileDialog.Options()
    #    options |= QFileDialog.DontUseNativeDialog
    #    openfile,_ = QFileDialog.getOpenFileName(self,'Open Database','/home/buddy/','Database Files (*.db)',options=options)
    #    self.monetDBObject.openDB(openfile)

    def deleteDBCallback(self):
        """
        Delete existing Database
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        openfile,_ = QFileDialog.getSaveFileName(self,'Delete Database','home/buddy/','Database Files (*.db)',options=options)
        datafarm = str(openfile).split("/")[:-1]
        database = str(openfile).split("/")[-1]
        path_to_datafarm = str(openfile).split("/")[-2]
        #path_to_datafarm = "/".join(datafarm)
        try:
            os.system("monetdb stop {}".format(database))
            os.system("monetdb destroy {}".format(database))
            #os.system("monetdbd stop {}".format(path_to_datafarm))
            #os.system("monetdbd start {}".format(path_to_datafarm))
        except Exception as ex:
            logger.error("MonetDB Delete Datafarm Error {} {}".format(type(ex).___name__,ex.args))

    def runQueryDBCallback(self):
        """
        Function to Run Queries to Database
        """
        self.out_query.clear()
        self.query = self.in_query.toPlainText()
        return_val = self.monetDBObject.runQuery(self.query)
        self.out_query.setText(str(return_val))
        self.in_query.clear()

    def insertDMLCallback(self):
        """
        Callback function for DML Insert Button Click event
        """
        dmlinsertdialog = DMLINSERT(self.monetDBObject)
        dmlinsertdialog.initWidget()
        dmlinsertdialog.show()
        dmlinsertdialog.exec_()

    def updateDMLCallback(self):
        """
        Callback function for DML Update Button Click event
        """
        dmlupdatedialog = DMLUPDATE(self.monetDBObject)
        dmlupdatedialog.initWidget()
        dmlupdatedialog.show()
        dmlupdatedialog.exec_()

    def deleteDMLCallback(self):
        """
        Callback function for DML Delete Button Click event
        """
        dmldeletedialog = DMLDELETE(self.monetDBObject)
        dmldeletedialog.initWidget()
        dmldeletedialog.show()
        dmldeletedialog.exec_()

    def createDDLCallback(self):
        """
        Callback function for DDL Create Button Click event
        """
        ddlcreatedialog = DDLCREATE(self.monetDBObject)
        ddlcreatedialog.initWidget()
        ddlcreatedialog.show()
        ddlcreatedialog.exec_()

    def alterDDLCallback(self):
        """
        Callback function for DDL Alter Button Click event
        """
        ddlalterdialog = DDLALTER(self.monetDBObject)
        ddlalterdialog.initWidget()
        ddlalterdialog.show()
        ddlalterdialog.exec_()

    def dropDDLCallback(self):
        """
        Callback function for DDL Drop Button Click event
        """
        ddldropdialog = DDLDROP(self.monetDBObject)
        ddldropdialog.initWidget()
        ddldropdialog.show()
        ddldropdialog.exec_()

    def clickedConnect(self):
        """
        Function for Emitting Signal on "Connect" button click event
        """
        self.sigConnect.emit()

    def clickedCreate(self):
        """
        Function for Emitting Signal on "Create" button click event
        """
        self.sigCreate.emit()

    #def clickedOpen(self):
    #    """
    #    Function for Emitting Signal on "Open" button click event
    #    """
    #    self.sigOpen.emit()

    def clickedDelete(self):
        """
        Function for Emitting Signal on "Delete" button click event
        """
        self.sigDelete.emit()

    def clickedRunQuery(self):
        """
        Function for Emitting Signal on "Run Query" button click event
        """
        self.sigRunQuery.emit()


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MDVISUAL()
    window.initWidget()
    #scr_res = app.desktop().screenGeometry()
    #wid,hei = scr_res.width(),scr_res.height()
    #window.setFixedSize(wid,hei)
    window.show()
    sys.exit(app.exec_())



