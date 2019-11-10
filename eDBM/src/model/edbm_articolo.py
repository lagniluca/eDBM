# -*- coding: utf-8 -*-

"""
Rappresentazione di un articolo
"""
from eDBM.src.model.exceptions.edbm_exception import eDBMException


class eDBMArticolo:
    def __init__(self):
        self._id = None
        self._id_settato = False
        self._codice = None
        self._codice_settato = False
        self._descrizione = None
        self._descrizione_settato = False
        self._peso = None
        self._peso_settato = False
        self._rapporto = None
        self._rapporto_settato = False
        self._inserto = None
        self._inserto_settato = False
        self._quantita = None
        self._quantita_settato = False
        self._colore = None
        self._colore_settato = False
        self._percentuale_colore = None
        self._percentuale_colore_settato = False
        self._anticipo_colore = None
        self._anticipo_colore_settato = False
        self._programma_c12 = None
        self._programma_c12_settato = False
        self._programma_c25 = None
        self._programma_c25_settato = False
        self._programma_hp12 = None
        self._programma_hp12_settato = False
        self._data = None
        self._data_settato = False
        self._ora = None
        self._ora_settato = False

    def setID(self, id):
        if self._id is None:
            self._id = id
            self._id_settato = True

    def setCodice(self, codice):
        if self._codice is None:
            if isinstance(codice, str):
                self._codice = codice
                self._codice_settato = True
            else:
                raise eDBMException("codice inserito non è di tipo testo")
        else:
            raise eDBMException("codice già inserito")

    def setDescrizione(self, descrizione):
        if self._descrizione is None:
            if isinstance(descrizione, str):
                self._descrizione = descrizione
                self._descrizione_settato = True
            else:
                raise eDBMException("la descrizione inserita non è di tipo testo")
        else:
            raise eDBMException("descrizione già inserita")

    def setPeso(self, peso):
        if self._peso is None:
            if isinstance(peso, int):
               self._peso = peso
               self._peso_settato = True
            else:
                raise eDBMException("il peso inserito non è di tipo intero")
        else:
            raise eDBMException("peso già inserito")

    def seRapporto(self, rapporto):
        if self._rapporto is None:
            if isinstance(rapporto, int):
               self._rapporto = rapporto
               self._rapporto_settato = True
            else:
                raise eDBMException("il rapporto inserito non è di tipo intero")
        else:
            raise eDBMException("rapporto già inserito")

    def setInserto(self, inserto):
        if self._inserto is None:
            if isinstance(inserto, str):
                self._inserto = inserto
                self._inserto_settato = True
            else:
                raise eDBMException("inserto inserito non è di tipo testo")
        else:
            raise eDBMException("inserto già inserito")

    def setQuantita(self, quantita):
        if self._quantita is None:
            if isinstance(quantita, int):
               self._quantita = quantita
               self._quantita_settato = True
            else:
                raise eDBMException("la quantita inserita non è di tipo intero")
        else:
            raise eDBMException("quantita già inserita")

    def setColore(self, colore):
        if self._colore is None:
            if isinstance(colore, str):
                self._colore = colore
                self._colore_settato = True
            else:
                raise eDBMException("colore inserito non è di tipo testo")
        else:
            raise eDBMException("colore già inserito")

    def setPercentualeColore(self, percentuale_colore):
        if self._percentuale_colore is None:
            if isinstance(percentuale_colore, int):
               self._percentuale_colore = percentuale_colore
               self._percentuale_colore_settato = True
            else:
                raise eDBMException("la percentuale_colore inserita non è di tipo intero")
        else:
            raise eDBMException("percentuale_colore già inserita")

    def setAnticipoColore(self, anticipo_colore):
        if self._anticipo_colore is None:
            if isinstance(anticipo_colore, int):
               self._anticipo_colore = anticipo_colore
               self._anticipo_colore_settato = True
            else:
                raise eDBMException("l' anticipo_colore inserito non è di tipo intero")
        else:
            raise eDBMException("anticipo_colore già inserito")

    def setProgrammaC12(self, programma_c12):
        if self._programma_c12 is None:
            if isinstance(programma_c12, int):
                self._programma_c12 = programma_c12
                self._programma_c12_settato = True
            else:
                raise eDBMException("programma_c12 inserito non è di tipo intero")
        else:
            raise eDBMException("programma_c12 già inserito")

    def setProgrammaC25(self, programma_c25):
        if self._programma_c25 is None:
            if isinstance(programma_c25, int):
                self._programma_c25 = programma_c25
                self._programma_c25_settato = True
            else:
                raise eDBMException("programma_c25 inserito non è di tipo intero")
        else:
            raise eDBMException("programma_c25 già inserito")

    def setProgrammaHP12(self, programma_hp12):
        if self._programma_hp12 is None:
            if isinstance(programma_hp12, int):
                self._programma_hp12 = programma_hp12
                self._programma_hp12_settato = True
            else:
                raise eDBMException("programma_hp12 inserito non è di tipo intero")
        else:
            raise eDBMException("programma_hp12 già inserito")

    def setData(self, data):
        if self._data is None:
            if isinstance(data, str):
                self._data = data
                self._data_settato = True
            else:
                raise eDBMException("la data inserita non è di tipo testo")
        else:
            raise eDBMException("data già inserita")

    def setOra(self, ora):
        if self._ora is None:
            if isinstance(ora, str):
                self._ora = ora
                self._ora_settato = True
            else:
                raise eDBMException("l' ora inserita non è di tipo testo")
        else:
            raise eDBMException("ora già inserita")

    def getID(self):
        return self._id

    def getCodice(self):
        return self._codice

    def getDescrizione(self):
        return self._descrizione

    def getPeso(self):
        return self._peso

    def getRapporto(self):
        return self._rapporto

    def getInserto(self):
        return self._inserto

    def getQuantita(self):
        return self._quantita

    def getColore(self):
        return self._colore

    def getPercentualeColore(self):
        return self._percentuale_colore

    def getAnticipoColore(self):
        return self._anticipo_colore

    def getProgrammaC12(self):
        return self._programma_c12

    def getProgrammaC25(self):
        return self._programma_c25

    def getProgrammaHP12(self):
        return self._programma_hp12

    def getData(self):
        return self._data

    def getOra(self):
        return self._ora

    def valida(self):
        valido = False

        if self.getCodice() is None:
            raise eDBMException("codice non è settato")

        if self.getPeso() is None:
            raise eDBMException("peso non è settato")

        if self.getRapporto() is None:
            raise eDBMException("rapporto non è settato")

        if self.getColore() is None:
            raise eDBMException("colore non è settato")

        if self.getPercentualeColore() is None :
            raise eDBMException("percentuale colore non è settato")

        if self.getAnticipoColore() is None:
            raise eDBMException("anticipo colore non è settato")

        if self.getProgrammaC12() is None:
            raise eDBMException("programma c12 non è settato")

        if self.getProgrammaC25() is None:
            raise eDBMException("programma c25 non è settato")

        if self.getProgrammaHP12() is None:
            raise eDBMException("programma HP12 non è settato")

        if self.getData() is None:
            raise eDBMException("data non è settata")

        if self.getOra() is None:
            raise eDBMException("ora non è settata")

        valido = True

        return valido

    def generaAggiungiArticoloQuery(self):

        self.valida()

        str = "INSERT INTO articoli(Codice,"

        if self._descrizione_settato :
            str += "Descrizione,"

        str += "Peso, Rapporto,"

        if self._inserto_settato :
            str += "Inserto,"

        if self._quantita_settato:
            str += "Quantita,"

        str += "Colore,PercColore,AnticipoCol,Programma_C12,Programma_C25,Programma_HP12,Data,Ora)"
        str += "\nVALUES('" + self._codice +"',"

        if self._descrizione_settato :
            str += "'" + self._descrizione + "',"

        str+= "" + str(self._peso) + "," + str(self._rapporto) + ","

        if self._inserto_settato :
            str += "'" + self._inserto + "',"

        if self._quantita_settato:
            str += "" + str(self._quantita) +","

        str += "'" + self._colore + "',"
        str += "" + self._percentuale_colore + ","
        str += "" + self._anticipo_colore + ","
        str += "" + self._programma_c12 + ","
        str += "" + self._programma_c25 + ","
        str += "" + self._programma_hp12 + ","
        str += "'" + self._data + "',"
        str += "'" + self._ora +"');"

        return str






