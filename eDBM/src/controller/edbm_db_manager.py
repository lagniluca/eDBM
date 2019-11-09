# -*- coding: utf-8 -*-

"""
Classe che permette gestisce la connessione al database
"""

# libreria di connessione a MS access
import pyodbc

class eDBMDBManager:

    def __init__(self, user, pwd, db_path):
        self._user = user
        self._pwd = pwd
        self._db_path = db_path
        self._conn = None
        self._connesso = False

    # Methodo usato per stabilire una connessione con il database
    def connettiDB(self):

        odbc_conn_str = ''

        if not self._connesso :

            if self._user is not None :
                if self._pwd is not None:
                    odbc_conn_str = (
                            r'DRIVER={Microsoft Access Driver (.*mdb, *.accdb)};'
                            r'DBQ=%s;'
                            r'UID=%s;'
                            r'PWD=%s' %
                            (self._db_path, self._user, self._pwd)
                    )
                else:
                    pass
            else:
                odbc_conn_str = (
                        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                        r'DBQ=%s;' %
                        self._db_path
                )

            try:
                self._conn = pyodbc.connect(odbc_conn_str)
            except Exception as e:
                raise e

            if self._conn is not None:
                self._connesso = True
            else:
                self._connesso = False

        return self._connesso

    # Metodo usato per chiudere una connessione con il database
    def disconnettiDB(self):
        if self._connesso :
            self._conn = None
            self._connesso = False

        return self._connesso


