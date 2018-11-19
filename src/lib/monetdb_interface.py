#!/usr/bin/python

import pymonetdb
import os
import sys
import logging
logger = logging.getLogger(__name__)

class MONETDBINTERFACE:
    """
    CLASS for MONETDB TRANSACTIONS: CRUD
    """
    def __init__(self):
        """
        Class Contructor
        """
        self.connection = None
        self.cursor = None

    def connectDB(self,path_to_database):
        """
        MonetDB Create Connection, Initialize Connection

        Args:
            path_to_database - Name of database path
        Returns:
            connection - MonetDB connection object
        """
        try:
            self.connection =  pymonetdb.connect(username = 'monetdb',password = 'monetdb', hostname = 'localhost',database = path_to_database)
            self.cursor = self.connection.cursor()
            self.connection.set_autocommit(True)
        except Exception as ex:
            logger.error("Database Connection Error: {}, {}".format(type(ex).__name__,ex.args))

    def rollbackDB(self):
        """
        MonetDB Connection ROLLBACK
        """
        try:
            self.connection.close()
        except Exception as ex:
            logger.error("Database Connection Rollback Error: {}, {}".format(type(ex).__name__,ex.args))

    def createTable(self,*args,**kwargs):
        """
        MonetDB Table Creation Function
        Args:
            name_of_table - Name of the MonetDB Table
        Returns:
            status - Query Status (True/False - Success/Failure)
        """
        try:
            self.cursor.execute('CREATE TABLE if not exists {} {}'.format(kwargs['table_name'],kwargs['entries']))
            return True
        except Exception as ex:
            logger.error("Can not create TABLE {}: {},{}".format(kwargs['table_name'],type(ex).__name__,ex.args))
            return False

    def runQuery(self,*args,**kwargs):
        """
        MonetDB function to run queries on the DB
        Args:
            *args - Query & Data 
            **kwargs - Query & Data
        Returns:
            status - Query Status (True/False)
        """
        try:
            query = args[0]
            logger.debug("Querying Database with: {}".format(query))
            return_val = self.cursor.execute('{}'.format(query))
            if query.lower().startswith('select'):
                data = self.readDatabase()
                return data
            return return_val
        except Exception as ex:
            logger.error("Can not Run Query {}: {},{}".format(args[0],type(ex).__name__,ex.args))
            return None

    def readDatabase(self,*args,**kwargs):
        """
        MonetDB function to run Read Query
        Args:
            *args - Query & Data
            Kwargs - Query & Data
        Returns:
            status - Query Status (True/False)
        """
        try:
            data = self.cursor.fetchall()
            return data
        except Exceptipn as ex:
            logger.error("Can not Read from Table {}: {},{}".format(kwargs['table_name'],type(ex).__name__,ex.args))
            return False

    def deleteDatabase(self,path_to_database):
        """
        MonetDB Delete Database
        Args:
            path_to_database - Name of the MonetDB with absolute path
        Returns:
            status - Operation Status (True/False)
        """
        try:
            os.system("monetdb stop {}".format(path_to_database))
            os.system("monetdb destroy {}".format(path_to_database))
            return True
        except Exception as ex:
            logger.error("Failed to Delete Database {}: {},{}".format(path_to_database.split()[-1],type(ex).__name__,ex.args))
