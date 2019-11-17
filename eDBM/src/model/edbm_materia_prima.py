# -*- coding: utf-8 -*-
import datetime

from eDBM.src.controller.exceptions.edbm_exception import eDBMException


def generaVisualizzaMateriePrimeQuery(codice, descrizione, data):
    query = None

    if (codice is not None) or (descrizione is not None) or (data is not None):

        query = "SELECT * FROM materie_prime WHERE "
        if codice is not None :
            query += "Codice='" + str(codice) +"'"
            if (descrizione is not None) or (data is not None) :
                query += " AND "

        if descrizione is not None:
            query += " Descrizione='" + str(descrizione) + "'"
            if data is not None:
                query += " AND "

        if data is not None:
            data_idiota = datetime.datetime.strptime(data, '%d/%m/%Y')
            query += "Data=#" + str(data_idiota.date()) + "#"

    return query

class eDBMMateriaPrima:

    def __init__(self):
        self._id = ''
        self._id_settato = False
        self._codice = ""
        self._codice_settato = False
        self._descrizione = ""
        self._descrizione_settato = False
        self._lotto = ""
        self._lotto_settato = False
        self._registrazione = ""
        self._registrazione_settato = False
        self._tipo = -1
        self._tipo_settato = False
        self._data = ""
        self._data_settato = False
        self._ora = ""
        self._ora_settato = False
        self._ddt = ""
        self._ddt_settato = False
        self._data_ddt = ""
        self._data_ddt_settato = False

    def setID(self, id):
        if self.validaID(id):
            self._id = id

    def validaID(self, id):
        if id is None:
            return False

        if not isinstance(id, int):
            return False

        if id < 0 :
            return False

        return True

    def confrontaID(self, id):
        uguali = False
        if self.validaID(id) :
            if self._id == id:
                uguali = True

        return uguali

    def setCodice(self, codice):
        if self.validaCodice(codice):
            self._codice = codice
        else:
            raise eDBMException("codice inserito non valido")

    def validaCodice(self, codice):
        if codice is None:
            return False

        if not isinstance(codice, str):
            return False

        if not codice:
            return False

        return True

    def confrontaCodice(self, codice):
        uguali = False
        if self.validaCodice(codice):
            if self._codice is not None :
                if self._codice == codice :
                    uguali = True

        return uguali

    def setDescrizione(self, descrizione):
        if self.validaDescrizione(descrizione):
            self._descrizione = descrizione
        else:
            raise eDBMException("descrizione non valida")

    def validaDescrizione(self, descrizione):
        if descrizione is None:
            return False

        if not isinstance(descrizione, str):
            return False

        return True

    def confrontaDescrizione(self, descrizione):
        uguali = False
        if self.validaDescrizione(descrizione):
            if self._descrizione == descrizione:
                uguali = True

    def setLotto(self, lotto):
        if self.validaLotto(lotto):
           self._lotto = lotto
        else:
            raise eDBMException("lotto non valido")

    def validaLotto(self, lotto):
        if lotto is None:
            return False

        if not isinstance(lotto, str):
            return False

        if not lotto :
            return False

        return True

    def confrontaLotto(self, lotto):
        uguali = False
        if self.validaLotto(lotto):
            if self._lotto == lotto:
                uguali = True

        return uguali

    def setRegistrazione(self, registrazione):
        if self.validaRegistrazione(registrazione):
            self._registrazione = registrazione
        else:
            raise eDBMException("registrazione non valida")

    def validaRegistrazione(self, registrazione):
        if registrazione is None :
            return False

        if not isinstance(registrazione, str):
            return False

        if not registrazione:
            return False

        return True

    def confrontaRegistrazione(self, registrazione):
        uguali = False

        if self.validaRegistrazione(registrazione):
            if self._registrazione == registrazione:
                uguali = True

    def setTipo(self, tipo):
        if self.validaTipo(tipo):
            self._tipo = tipo
        else:
            raise eDBMException("tipo non valido")

    def validaTipo(self, tipo):
        if tipo is None:
            return False

        if not isinstance(tipo, int):
            return False

        if tipo < 0 :
            return False

        return True

    def confrontaTipo(self, tipo):
        uguali = False

        if self.validaTipo(tipo):
            if self._tipo == tipo :
                uguali = True

        return uguali

    def setData(self, data):
        if self.validaData(data):
            self._data = data
        else:
            raise eDBMException("data non valida")

    def validaData(self, data):
        if data is None :
            return False

        if not isinstance(data, str):
            return False

        if not data:
            return False

        try:
            datetime.datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            return False

        return True

    def confrontaData(self, data):
        uguali = False

        if self.validaData(data):
            if self._data == data:
                uguali = True

        return uguali

    def setOra(self, ora):
        if self.validaOra(ora):
            self._ora = ora
        else:
            raise eDBMException("ora non valida")

    def validaOra(self, ora):
        if ora is None :
            return False

        if not isinstance(ora, str):
            return False

        if not ora :
            return False

        try:
            datetime.datetime.strptime(ora, "%H:%M:%S")
        except ValueError:
            return False

        return True

    def confrontaOra(self, ora):
        uguali = False

        if self.validaOra(ora):
            if self._ora == ora:
                uguali = True

        return uguali

    def setDDT(self, ddt):
        if self.validaDDT(ddt):
            self._ddt = ddt
        else:
            raise eDBMException("ddt non valido")

    def validaDDT(self, ddt):
        if ddt is None:
           ddt = " "

        if not isinstance(ddt, str):
            return False

        return True

    def confrontaDDT(self, ddt):
        uguali = False

        if self.validaDDT(ddt):
            if self._ddt == ddt:
                uguali = True

        return uguali


    def setDataDDT(self, data_ddt):
        if self.validaDataDDT(data_ddt):
            self._data_ddt = data_ddt
        else:
            raise eDBMException("data DDT non valida")

    def validaDataDDT(self, dataDDT):
        if dataDDT is None :
            return False

        if not isinstance(dataDDT, str):
            return False

        if not dataDDT :
            return False

        try:
            datetime.datetime.strptime(dataDDT, "%d/%m/%Y")
        except ValueError:
            return False

        return True

    def confrontaDataDDT(self, dataDDT):
        uguali = False

        if self.validaDataDDT(dataDDT):
            if self._data_ddt == dataDDT:
                uguali = True

        return uguali

    def equals(self, altra_mp):
        uguali = True

        uguali = uguali and self.confrontaID(altra_mp.getID())
        uguali = uguali and self.confrontaCodice(altra_mp.getCodice())
        uguali = uguali and self.confrontaDescrizione(altra_mp.getDescrizione())
        uguali = uguali and self.confrontaLotto(altra_mp.getLotto())
        uguali = uguali and self.confrontaRegistrazione(altra_mp.getID())
        uguali = uguali and self.confrontaTipo(altra_mp.getTipo())
        uguali = uguali and self.confrontaData(altra_mp.getData())
        uguali = uguali and self.confrontaOra(altra_mp.getOra())
        uguali = uguali and self.confrontaDDT(altra_mp.getDDT())
        uguali = uguali and self.confrontaDataDDT(altra_mp.getDataDDT())

        return uguali

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

        if not self.validaID(self._id):
            pass

        if not self.validaCodice(self._codice) :
            raise eDBMException("codice non valido")

        if not self.validaDescrizione(self._descrizione) :
            raise eDBMException("descrizione non valida")

        if not self.validaLotto(self._lotto):
            raise eDBMException("lotto non valido")

        if not self.validaRegistrazione(self._registrazione):
            raise eDBMException("registrazione non valida")

        if not self.validaTipo(self._tipo):
            raise eDBMException("tipo non valido")

        if not self.validaData(self._data):
            raise eDBMException("data non valida")

        if not self.validaOra(self._ora):
            raise eDBMException("ora non valida")

        if not self.validaDDT(self._ddt):
            raise eDBMException("DDT non valido")

        if not self.validaDataDDT(self._data_ddt):
            raise eDBMException("data DDT non valida")

        return True

    def generaAggiungiMateriaPrimaQuery(self):
        self.valida()

        query = "INSERT INTO materie_prime (Codice, Descrizione, Lotto, Registrazione, Tipo, Data, Ora, DDT, DataDDT) "
        query += "VALUES ('" + self._codice +"', "
        query += "'" + self._descrizione + "',"
        query += "'" + self._lotto + "', "
        query += "'" + self._registrazione + "', "
        query += "'" + str(self._tipo) + "', "
        query += "'" + self._data + "', "
        query += "'" + self._ora + "', "
        query += "'" + self._ddt +"', "
        query += "'" + self._data_ddt + "') "

        print(query);

        return query

    def generaRimuoviMateriaPrimaQuery(self):
        self.valida()

        query = "DELETE FROM materie_prime WHERE "
        query += "ID=" + str(self.getID()) +""

        return query

    def generaModificaMateriaPrimaQuery(self):
        self.valida()

        query = "UPDATE materie_prime SET "
        query += "Codice='" + str(self.getCodice()) + "',"
        query += "Descrizione='" + str(self.getDescrizione()) + "',"
        query += "Lotto='" + str(self.getLotto()) + "',"
        query += "Registrazione='" + str(self.getRegistrazione()) + "',"
        query += "Tipo=" + str(self.getTipo()) + ","
        query += "Data='" + str(self.getData()) + "',"
        query += "Ora='" + str(self.getOra()) + "',"
        query += "DDT='" + str(self.getDDT()) + "',"
        query += "DataDdt='" + str(self.getDataDDT()) + "' "
        query += "WHERE ID=" + str(self.getID()) + ""

        return query

