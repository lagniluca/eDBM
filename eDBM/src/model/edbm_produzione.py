# -*- coding: utf-8 -*-

"""
Classe che modella un record di produzione
"""
from eDBM.src.model.exceptions.edbm_exception import eDBMException

class eDBMProduzione:
    def __init__(self):
        self._id = -1
        self._linea = ''
        self._articolo = ''
        self._n_stampo = -1
        self._peso = -1
        self._rapporto = -1
        self._tempo_colata = -1
        self._qta_poliolo = -1
        self._flusso_poliolo = -1
        self._temp_poliolo = -1
        self._press_poliolo = -1
        self._qta_isocianato = -1
        self._flusso_isocianato = -1
        self._temp_isocianato = -1
        self._press_isocianato = -1
        self._num_colore = -1
        self._perc_colore = -1
        self._flusso_colore = -1
        self._anticipo_colore = -1
        self._data = ''
        self._ora = ''
        self._lotto_poliolo = ''
        self._lotto_isocianato = ''
        self._lotto_colore = ''
        self._lotto_articolo = ''
        self._lotto_inserto = ''
        self._badge = -1

    # validatori
    def validaID(self, id):
        if id is None :
            return False

        if not isinstance(id, int):
            return False

        if id < 0 :
            return False

        return True

    def validaLinea(self, linea):
        if linea is None:
            return False

        if not isinstance(linea, str):
            return False

        return True

    def validaArticolo(self, articolo):
        if articolo is None:
            return False

        if not isinstance(articolo, str):
            return False

        return True

    def validaNStampo(self, n_stampo):
        if n_stampo is None:
            return False

        if not isinstance(n_stampo , int):
            return False

        if n_stampo < 0 :
            return False

        return True

    def validaPeso(self, peso):
        if peso is None:
            return False

        if not isinstance(peso, int):
            return False

        if peso < 0:
            return False

        return True

    def validaRapporto(self, rapporto):
        if rapporto is None:
            return False

        if not isinstance(rapporto, int):
            return False

        if rapporto < 0:
            return False

        return True

    def validaTempoColata(self, tempo_colata):
        if tempo_colata is None:
            return False

        if not isinstance(tempo_colata, int):
            return False

        if tempo_colata < 0:
            return False

        return True

    def validaQuantitaPoliolo(self, qta_poliolo):
        if qta_poliolo is None:
            return False

        if not isinstance(qta_poliolo, int):
            return False

        if qta_poliolo < 0 :
            return False

        return True

    def validaFlussoPoliolo(self, flusso_poliolo):
        if flusso_poliolo is None:
            return False

        if not isinstance(flusso_poliolo, int):
            return False

        if flusso_poliolo < 0:
            return False

        return True

    def validaTemperaturaPoliolo(self, temp_poliolo):
        if temp_poliolo is None:
            return False

        if not isinstance(temp_poliolo, int):
            return False

        if temp_poliolo < 0 :
            return False

        return True

    def validaPressionePoliolo(self, press_poliolo):
        if press_poliolo is None:
            return False

        if not isinstance(press_poliolo, int):
            return False

        if press_poliolo < 0:
            return False

        return True

    def validaQuantitaIsocianato(self, qta_isocianato):
        if qta_isocianato is None:
            return False

        if not isinstance(qta_isocianato, int):
            return False

        if qta_isocianato < 0:
            return False

        return True

    def validaFlussoIsocianato(self, flusso_isocianato):
        if flusso_isocianato is None:
            return False

        if not isinstance(flusso_isocianato, int):
            return False

        if flusso_isocianato < 0:
            return False

        return True

    def validaTemperaturaIsocianato(self, temp_isocianato):
        if temp_isocianato is None:
            return False

        if not isinstance(temp_isocianato, int):
            return False

        if temp_isocianato < 0:
            return False

        return True

    def validaPressioneIsocianato(self, press_isocianato):
        if press_isocianato is None:
            return False

        if not isinstance(press_isocianato, int):
            return False

        if press_isocianato < 0:
            return False

        return True

    def validaNumColore(self, num_colore):
        if num_colore is None:
            return False

        if not isinstance(num_colore, int):
            return False

        if num_colore < 0:
            return False

        return True

    def validaPercentualeColore(self, perc_colore):
        if perc_colore is None:
            return False

        if not isinstance(perc_colore, int):
            return False

        if perc_colore < 0:
            return False

        return True

    def validaFlussoColore(self, flusso_colore):
        if flusso_colore is None:
            return False

        if not isinstance(flusso_colore, int):
            return False

        if flusso_colore < 0:
            return False

        return True

    def validaAnticipoColore(self, antic_colore):
        if antic_colore is None:
            return False

        if not isinstance(antic_colore, int):
            return False

        if antic_colore < 0:
            return False

        return True

    def validaData(self, data):
        if data is None:
            return False

        if not isinstance(data, str):
            return False

        if not data:
            return False

        return True

    def validaOra(self, ora):
        if ora is None:
            return False

        if not isinstance(ora, str):
            return False

        if not ora:
            return False

        return True

    def validaLottoPoliolo(self, lotto_poliolo):
        if lotto_poliolo is None:
            return False

        if not isinstance(lotto_poliolo, str):
            return False

        return True

    def validaLottoIsocianato(self, lotto_isocianato):
        if lotto_isocianato is None:
            return False

        if not isinstance(lotto_isocianato, str):
            return False

        return True

    def validaLottoColore(self, lotto_colore):
        if lotto_colore is None:
            return False

        if not isinstance(lotto_colore, str):
            return False

        return True

    def validaLottoArticolo(self, lotto_articolo):
        if lotto_articolo is None:
            return False

        if not isinstance(lotto_articolo, str):
            return False

        return True

    def validaLottoInserto(self, lotto_inserto):
        if lotto_inserto is None:
            return False

        if not isinstance(lotto_inserto, str):
            return False

        return True

    def validaBadge(self, badge):
        if badge is None:
            return False

        if not isinstance(badge, int):
            return False

        if badge < 0:
            return  False

        return True

    # setters
    def setID(self, id):
        if self.validaID(id):
            self._id = id
        else:
            raise eDBMException("id non valido")

    def setLinea(self, linea):
        if self.validaLinea(linea):
            self._linea = linea
        else:
            raise eDBMException("linea non valida")

    def setArticolo(self, articolo):
        if self.validaArticolo(articolo):
            self._articolo = articolo
        else:
            raise eDBMException("articolo non valido")

    def setNumeroStampo(self, num_stampo):
        if self.validaNStampo(num_stampo):
            self._n_stampo = num_stampo
        else:
            raise eDBMException("numero stampo non valido")

    def setPeso(self, peso):
        if self.validaPeso(peso):
            self._peso = peso
        else:
            raise eDBMException("peso non valido")

    def setRapporto(self, rapporto):
        if self.validaRapporto(rapporto):
            self._rapporto = rapporto
        else:
            raise eDBMException("rapporto non valido")

    def setTempoColata(self, tempo_colata):
        if self.validaTempoColata(tempo_colata):
            self._tempo_colata = tempo_colata
        else:
            raise eDBMException("tempo colata non valido")

    def setQuantitaPoliolo(self, qta_poliolo):
        if self.validaQuantitaPoliolo(qta_poliolo):
            self._qta_poliolo = qta_poliolo
        else:
            raise eDBMException("quantita' poliolo non valido")

    def setFlussoPoliolo(self, flusso_poliolo):
        if self.validaFlussoPoliolo(flusso_poliolo):
            self._flusso_poliolo = flusso_poliolo
        else:
            raise eDBMException("flusso poliolo non valido")

    def setTemperaturaPoliolo(self, temp_poliolo):
        if self.validaTemperaturaPoliolo(temp_poliolo):
            self._temp_poliolo = temp_poliolo
        else:
            raise eDBMException("tempearura poliolo non valida")

    def setPressionePoliolo(self, press_poliolo):
        if self.validaPressionePoliolo(press_poliolo):
            self._press_poliolo = press_poliolo
        else:
            raise eDBMException("pressione poliolo non valido")

    def setQuantitaIsocianato(self, qta_isocianato):
        if self.validaQuantitaIsocianato(qta_isocianato):
            self._qta_isocianato = qta_isocianato
        else:
            raise eDBMException("quantita' isocianato non valido")

    def setFlussoIsocianato(self, flusso_isocianato):
        if self.validaFlussoIsocianato(flusso_isocianato):
            self._flusso_isocianato = flusso_isocianato
        else:
            raise eDBMException("flusso isocianato non valido")

    def setTemperaturaIsocianato(self, temp_isocianato):
        if self.validaTemperaturaIsocianato(temp_isocianato):
            self._temp_isocianato = temp_isocianato
        else:
            raise eDBMException("temperatura isocianato non valido")

    def setPressioneIsocianato(self, press_isocianato):
        if self.validaPressioneIsocianato(press_isocianato):
            self._press_isocianato = press_isocianato
        else:
            raise eDBMException("pressione isocianato non valido")

    def setNumColore(self, num_colore):
        if self.validaNumColore(num_colore):
            self._num_colore = num_colore
        else:
            raise eDBMException("numero colore non valido")

    def setPercentualeColore(self, perc_colore):
        if self.validaPercentualeColore(perc_colore):
            self._perc_colore = perc_colore
        else:
            raise eDBMException("percentuale colore non valido")

    def setFlussoColore(self, flusso_colore):
        if self.validaFlussoColore(flusso_colore):
            self._flusso_colore = flusso_colore
        else:
            raise eDBMException("flusso colore non valido")

    def setAnticipoColore(self, ant_colore):
        if self.validaAnticipoColore(ant_colore):
            self._anticipo_colore = ant_colore
        else:
            raise eDBMException("anticipo colore non valido")

    def setData(self, data):
        if self.validaData(data):
            self._data = data
        else:
            raise eDBMException("data non valido")

    def setOra(self, ora):
        if self.validaOra(ora) :
            self._ora = ora
        else:
            raise eDBMException("ora non valida")

    def setLottoPoliolo(self, lotto_poliolo):
        if self.validaLottoPoliolo(lotto_poliolo):
            self._lotto_poliolo = lotto_poliolo
        else:
            raise eDBMException("lotto poliolo non valido")

    def setLottoIsocianato(self, lotto_isocianato):
        if self.validaLottoIsocianato(lotto_isocianato) :
            self._lotto_isocianato = lotto_isocianato
        else:
            raise eDBMException("lotto isocianato non valido")

    def setLottoColore(self, lotto_colore):
        if self.validaLottoColore(lotto_colore):
            self._lotto_colore = lotto_colore
        else:
            raise eDBMException("lotto colore non valido")

    def setLottoArticolo(self, lotto_articolo):
        if self.validaLottoArticolo(lotto_articolo):
            self._lotto_articolo = lotto_articolo
        else:
            raise eDBMException("lotto articolo non valido")

    def setLottoInserto(self, lotto_inserto):
        if self.validaLottoInserto(lotto_inserto):
            self._lotto_inserto = lotto_inserto
        else:
            raise eDBMException("lotto inserto non valido")

    def setBadge(self, badge):
        if self.validaBadge(badge):
            self._badge = badge
        else:
            raise eDBMException("badge non valido")

    # getters
    def getID(self):
        return self._id

    def getLinea(self):
        return self._linea

    def getArticolo(self):
        return self._articolo

    def getNumeroStampo(self):
        return self._n_stampo

    def getPeso(self):
        return self._peso

    def getRapporto(self):
        return self._rapporto

    def getTempoColata(self):
        return self._tempo_colata

    def getQuantitaPoliolo(self):
        return self._qta_poliolo

    def getFlussoPoliolo(self):
        return self._flusso_poliolo

    def getTemperaturaPoliolo(self):
        return self._temp_poliolo

    def getPressionePoliolo(self):
        return self._press_poliolo

    def getQuantitaIsocianato(self):
        return self._qta_isocianato

    def getFlussoIsocianato(self):
        return self._flusso_isocianato

    def getTemperaturaIsocianato(self):
        return self._temp_isocianato

    def getPressioneIsocianato(self):
        return self._press_isocianato

    def getNumColore(self):
        return self._num_colore

    def getPercentualeColore(self):
        return self._perc_colore

    def getFlussoColore(self):
        return self._flusso_colore

    def getAnticipoColore(self):
        return self._anticipo_colore

    def getData(self):
        return self._data

    def getOra(self):
        return self._ora

    def getLottoPoliolo(self):
        return self._lotto_poliolo

    def getLottoIsocianato(self):
        return self._lotto_isocianato

    def getLottoColore(self):
        return self._lotto_colore

    def getLottoArticolo(self):
        return self._lotto_articolo

    def getLottoInserto(self):
        return self._lotto_inserto

    def getBadge(self):
        return self._badge
