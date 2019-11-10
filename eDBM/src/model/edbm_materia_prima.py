# -*- coding: utf-8 -*-
from eDBM.src.model.exceptions.edbm_exception import eDBMException


class eDBMMateriaPrima:

    def __init__(self):
        self._id = None
        self._id_settato = False
        self._codice = None
        self._codice_settato = False
        self._descrizione = None
        self._descrizione_settato = False
        self._lotto = None
        self._lotto_settato = False
        self._registrazione = None
        self._registrazione_settato = False
        self._tipo = None
        self._tipo_settato = False
        self._data = None
        self._data_settato = False
        self._ora = None
        self._ora_settato = False
        self._ddt = None
        self._ddt_settato = False
        self._data_ddt = None
        self._data_ddt_settato = False

    def setID(self, id):
        if self._id is None :
            self._id = id
            self._id_settato = True

    def setCodice(self, codice):
        if self._codice is None:
            print("11b ")
            if isinstance(codice, str) is True:
                if not codice :
                    raise eDBMException("codice inserito nullo")
                else:
                    self._codice = codice
                    self._codice_settato = True
            else:
                raise eDBMException("codice inserito non è di tipo testo")
        else:
            raise eDBMException("codice già inserito")

    def setDescrizione(self, descrizione):
        if self._descrizione is None:
            if isinstance(descrizione, str):
                if not descrizione :
                    pass
                else:
                    self._descrizione = descrizione
                    self._descrizione_settato = True
            else:
                raise eDBMException("la descrizione inserita non è di tipo testo")

    def setLotto(self, lotto):
        if self._lotto is None:
            if isinstance(lotto, str):
                if not lotto:
                    raise eDBMException("lotto inserito nullo")
                else:
                    self._lotto = lotto
                    self._lotto_settato = True
            else:
                raise eDBMException("lotto inserito non è di tipo testo")
        else:
            raise eDBMException("lotto già inserito")

    def setRegistrazione(self, registrazione):
        if self._registrazione is None:
            if isinstance(registrazione, str):
                if not registrazione:
                    raise eDBMException("registrazione inserita nulla")
                else:
                    self._registrazione = registrazione
                    self._registrazione_settato = True
            else:
                raise eDBMException("registrazione inserito non è di tipo testo")
        else:
            raise eDBMException("registrazione già inserito")

    def setTipo(self, tipo):
        if self._tipo is None:
            if isinstance(tipo, int):
                self._tipo = tipo
                self._tipo_settato = True
            else:
                raise eDBMException("tipo inserito non è di tipo intero")
        else:
            raise eDBMException("tipo già inserito")

    def setData(self, data):
        if self._data is None:
            if isinstance(data, str):
                if not data:
                    raise eDBMException("data inserita nulla")
                else:
                    self._data = data
                    self._data_settato = True
            else:
                raise eDBMException("la data inserita non è di tipo testo")
        else:
            raise eDBMException("data già inserita")

    def setOra(self, ora):
        if self._ora is None:
            if isinstance(ora, str):
                if not ora :
                    raise eDBMException("ora inserita nulla")
                else:
                    self._ora = ora
                    self._ora_settato = True
            else:
                raise eDBMException("l' ora inserita non è di tipo testo")
        else:
            raise eDBMException("ora già inserita")

    def setDDT(self, ddt):
        if self._ddt is None:
            if isinstance(ddt, str):
                if not ddt:
                    pass
                else:
                    self._ddt = ddt
                    self._ddt_settato = True
            else:
                raise eDBMException("ddt inserito non è di tipo testo")
        else:
            raise eDBMException("ddt già inserita")

    def setDataDDT(self, data_ddt):
        if self._data_ddt is None and data_ddt is not None:
            if isinstance(data_ddt, str):
                if not data_ddt :
                    raise eDBMException("data ddt inserita nulla")
                else:
                    self._data_ddt = data_ddt
                    self._data_ddt_settato = True
            else:
                raise eDBMException("data DDT inserita non è di tipo testo")
        else:
            raise eDBMException("data DDT già inserita")

    def getID(self):
        return self._id

    def getCodice(self):
        return self._codice

    def getDescrizione(self):
        return self._descrizione

    def getLotto(self):
        return self._lotto

    def getRegistrazione(self):
        return self._registrazione

    def getTipo(self):
        return self._tipo

    def getData(self):
        return self._data

    def getOra(self):
        return self._ora

    def getDDT(self):
        return self._ddt

    def getDataDDT(self):
        return self._data_ddt

    def valida(self):
        valido = False

        if not self._codice_settato:
            raise eDBMException("codice non settato")

        if not self._lotto_settato :
            raise eDBMException("lotto non settato")

        if not self._registrazione_settato :
            raise eDBMException("registrazione non settato")

        if not self._tipo_settato:
            raise eDBMException("tipo non settato")

        if not self._data_settato:
            raise eDBMException("data non settato")

        if not self._ora_settato:
            raise eDBMException("ora non settato")

        if not self._data_ddt_settato:
            raise eDBMException("data ddt non settato")

        valido = True

        return valido

    def generaAggiungiMateriaPrimaQuery(self):
        self.valida()

        query = "INSERT INTO materie_prime (Codice,"

        if self._descrizione_settato :
            query += "Descrizione,"

        query += "Lotto, Registrazione, Tipo, Data, Ora, "

        if self._ddt_settato :
            query += "DDT, "

        query += "DataDdt) "
        query += "VALUES ('" + self._codice +"', "

        if self._descrizione_settato:
            query += "'" + self._descrizione + "',"

        query += "'" + self._lotto + "', "
        query += "'" + self._registrazione + "', "
        query += "'" + str(self._tipo) + "', "
        query += "'" + self._data + "', "
        query += "'" + self._ora + "', "

        if self._ddt_settato :
            query += "'" + self._ddt +"', "

        query += "'" + self._data_ddt + "') "

        print(query)

        return query

    def __str__(self):
        s = "ID : " + str(self._id)

        return s

