# -*- coding: utf-8 -*-

"""
Class used for creating a grid component
"""

# librerie di sistema
import datetime
import traceback

# librerie WX
import wx
import wx.grid

# librerie di access
import pyodbc

# librerie applicazione
from eDBM.src.model.edbm_produzione import eDBMProduzione, generaVisualizzaProduzioneQuery

# numero campi
PRODUZIONE_NUMERO_CAMPI = 27

# costanti indici
PRODUZIONE_INDICE_ID = 0
PRODUZIONE_INDICE_LINEA = 1
PRODUZIONE_INDICE_ARTICOLO = 2
PRODUZIONE_INDICE_N_STAMPO = 3
PRODUZIONE_INDICE_PESO = 4
PRODUZIONE_INDICE_RAPPORTO = 5
PRODUZIONE_INDICE_TEMPO_COLATA = 6
PRODUZIONE_INDICE_QUANTITA_POLIOLO = 7
PRODUZIONE_INDICE_FLUSSO_POLIOLO = 8
PRODUZIONE_INDICE_TEMPERATURA_POLIOLO = 9
PRODUZIONE_INDICE_PRESSIONE_POLIOLO = 10
PRODUZIONE_INDICE_QUANTITA_ISOCIANATO = 11
PRODUZIONE_INDICE_FLUSSO_ISOCIANATO = 12
PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO = 13
PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO = 14
PRODUZIONE_INDICE_N_COLORE = 15
PRODUZIONE_INDICE_PERCENTUALE_COLORE = 16
PRODUZIONE_INDICE_FLUSSO_COLORE = 17
PRODUZIONE_INDICE_ANTICIPO_COLORE = 18
PRODUZIONE_INDICE_DATA = 19
PRODUZIONE_INDICE_ORA = 20
PRODUZIONE_INDICE_LOTTO_POLIOLO = 21
PRODUZIONE_INDICE_LOTTO_ISOCIANATO = 22
PRODUZIONE_INDICE_LOTTO_COLORE = 23
PRODUZIONE_INDICE_LOTTO_ARTICOLO = 24
PRODUZIONE_INDICE_LOTTO_INSERTO = 25
PRODUZIONE_INDICE_BADGE = 26


class eDBMProduzioneGridPanel(wx.Panel):
    def __init__(self, parent, window, dbm):
        super(eDBMProduzioneGridPanel, self).__init__(parent, style=wx.BORDER_RAISED)

        self._window = window
        self._dbm = dbm
        self._grid = None
        self._table_content_original = list()  # contenuti della tabella subito dopo il commit

        self._InitUI()

    def _InitGridHeader(self):
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_ID, "ID")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LINEA, "Linea")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_ARTICOLO, "Articolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_N_STAMPO, "N. Stampo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_PESO, "Peso")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_RAPPORTO, "Rapporto")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_TEMPO_COLATA, "Tempo colata")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_QUANTITA_POLIOLO, "Quantita' poliolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_FLUSSO_POLIOLO, "Flusso poliolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_TEMPERATURA_POLIOLO, "Temperatura poliolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_PRESSIONE_POLIOLO, "Pressione poliolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_QUANTITA_ISOCIANATO, "Quantita' isocianato")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_FLUSSO_ISOCIANATO, "Flusso isocianato")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO, "Temperatura isocianato")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO, "Pressione isocianato")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_N_COLORE, "N. Colore")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_PERCENTUALE_COLORE, "% Colore")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_FLUSSO_COLORE, "Flusso colore")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_ANTICIPO_COLORE, "Anticipo colore")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_DATA, "Data")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_ORA, "Ora")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_POLIOLO, "Lotto poliolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_ISOCIANATO, "Lotto isocianato")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_COLORE, "Lotto colore")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_ARTICOLO, "Lotto articolo")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_INSERTO, "Lotto inserto")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_BADGE, "Badge")

    def _immettiStringa(self, dato):
        stringa = ""

        if (dato is None) or (not dato):
            stringa = " "
        else:
            stringa = dato

        if dato == 'None':
            stringa = " "

        return stringa

    def _InitGridContent(self):
        read_only = True
        record = 0
        current_rows = self._grid.GetNumberRows()

        for prod in self._table_content_original:

            if record >= current_rows:
                self._grid.AppendRows(1)
                record = current_rows
                current_rows = current_rows + 1

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ID, self._immettiStringa(str(prod.getID())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ID, True)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LINEA, self._immettiStringa(str(prod.getLinea())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LINEA, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ARTICOLO, self._immettiStringa(str(prod.getArticolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ARTICOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_N_STAMPO, self._immettiStringa(str(prod.getNumeroStampo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_N_STAMPO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PESO, self._immettiStringa(str(prod.getPeso())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PESO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_RAPPORTO, self._immettiStringa(str(prod.getRapporto())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_RAPPORTO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPO_COLATA, self._immettiStringa(str(prod.getTempoColata())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPO_COLATA, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_QUANTITA_POLIOLO, self._immettiStringa(str(prod.getQuantitaPoliolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_QUANTITA_POLIOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_POLIOLO, self._immettiStringa(str(prod.getFlussoPoliolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_POLIOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPERATURA_POLIOLO, self._immettiStringa(str(prod.getTemperaturaPoliolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPERATURA_POLIOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PRESSIONE_POLIOLO, self._immettiStringa(str(prod.getPressionePoliolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PRESSIONE_POLIOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_QUANTITA_ISOCIANATO, self._immettiStringa(str(prod.getQuantitaIsocianato())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_QUANTITA_ISOCIANATO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_ISOCIANATO, self._immettiStringa(str(prod.getFlussoIsocianato())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_ISOCIANATO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO,
                                    self._immettiStringa(str(prod.getTemperaturaIsocianato())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO, self._immettiStringa(str(prod.getPressioneIsocianato())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_N_COLORE, self._immettiStringa(str(prod.getNumColore())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_N_COLORE, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PERCENTUALE_COLORE, self._immettiStringa(str(prod.getPercentualeColore())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PERCENTUALE_COLORE, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_COLORE, self._immettiStringa(str(prod.getFlussoColore())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_COLORE, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ANTICIPO_COLORE, self._immettiStringa(str(prod.getAnticipoColore())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ANTICIPO_COLORE, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_DATA, self._immettiStringa(str(prod.getData())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_DATA, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ORA, self._immettiStringa(str(prod.getOra())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ORA, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_POLIOLO, self._immettiStringa(str(prod.getLottoPoliolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_POLIOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_ISOCIANATO, self._immettiStringa(str(prod.getLottoIsocianato())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_ISOCIANATO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_COLORE, self._immettiStringa(str(prod.getLottoColore())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_COLORE, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_ARTICOLO, self._immettiStringa(str(prod.getLottoArticolo())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_ARTICOLO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_INSERTO, self._immettiStringa(str(prod.getLottoInserto())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_INSERTO, read_only)
            self._grid.SetCellValue(record, PRODUZIONE_INDICE_BADGE, self._immettiStringa(str(prod.getBadge())))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_BADGE, read_only)

            record = record + 1

    def _InitUI(self):
        self._grid = wx.grid.Grid(self)
        self._grid.CreateGrid(0, PRODUZIONE_NUMERO_CAMPI)

        self._InitGridHeader()
        self._InitGridContent()

        # Placement of the grid component inside the panel
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(1, 1, 9, 25)

        fgs.AddMany([
            (self._grid, wx.ID_ANY, wx.EXPAND | wx.ALIGN_LEFT)
        ])

        fgs.AddGrowableCol(0, 1)
        fgs.AddGrowableRow(0, 1)

        sizer.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.SetSizer(sizer)
        sizer.Fit(self)

    def _RetriveTableContent(self, query):
        self._table_content_original = list()
        cursor = self._dbm.connessione().cursor()
        cursor.execute(query)

        records = cursor.fetchall()
        for record in records:
            # creazione dell'oggetto materia prima per ogni record
            prod = eDBMProduzione()

            prod.setID(int(record[PRODUZIONE_INDICE_ID]))
            prod.setLinea(self._immettiStringa(str(record[PRODUZIONE_INDICE_LINEA])))
            prod.setArticolo(self._immettiStringa(str(record[PRODUZIONE_INDICE_ARTICOLO])))
            prod.setNumeroStampo(int(record[PRODUZIONE_INDICE_N_STAMPO]))
            prod.setPeso(int(record[PRODUZIONE_INDICE_PESO]))
            prod.setRapporto(int(record[PRODUZIONE_INDICE_RAPPORTO]))
            prod.setTempoColata(int(record[PRODUZIONE_INDICE_TEMPO_COLATA]))
            prod.setQuantitaPoliolo(int(record[PRODUZIONE_INDICE_QUANTITA_POLIOLO]))
            prod.setFlussoPoliolo(int(record[PRODUZIONE_INDICE_FLUSSO_POLIOLO]))
            prod.setTemperaturaPoliolo(int(record[PRODUZIONE_INDICE_TEMPERATURA_POLIOLO]))
            prod.setPressionePoliolo(int(record[PRODUZIONE_INDICE_PRESSIONE_POLIOLO]))
            prod.setQuantitaIsocianato(int(record[PRODUZIONE_INDICE_QUANTITA_ISOCIANATO]))
            prod.setFlussoIsocianato(int(record[PRODUZIONE_INDICE_FLUSSO_ISOCIANATO]))
            prod.setTemperaturaIsocianato(int(record[PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO]))
            prod.setPressioneIsocianato(int(record[PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO]))
            prod.setNumColore(int(record[PRODUZIONE_INDICE_N_COLORE]))
            prod.setPercentualeColore(int(record[PRODUZIONE_INDICE_PERCENTUALE_COLORE]))
            prod.setFlussoColore(int(record[PRODUZIONE_INDICE_FLUSSO_COLORE]))
            prod.setAnticipoColore(int(record[PRODUZIONE_INDICE_ANTICIPO_COLORE]))
            data = str(record[PRODUZIONE_INDICE_DATA].strftime("%d/%m/%Y"))
            prod.setData(self._immettiStringa(data))
            ora = str(record[PRODUZIONE_INDICE_ORA].strftime("%H:%M:%S"))
            prod.setOra(self._immettiStringa(str(ora)))
            prod.setLottoPoliolo(self._immettiStringa(str(record[PRODUZIONE_INDICE_LOTTO_POLIOLO])))
            prod.setLottoIsocianato(self._immettiStringa(str(record[PRODUZIONE_INDICE_LOTTO_ISOCIANATO])))
            prod.setLottoColore(self._immettiStringa(str(record[PRODUZIONE_INDICE_LOTTO_COLORE])))
            prod.setLottoArticolo(self._immettiStringa(str(record[PRODUZIONE_INDICE_LOTTO_ARTICOLO])))
            prod.setLottoInserto(self._immettiStringa(str(record[PRODUZIONE_INDICE_LOTTO_INSERTO])))
            prod.setBadge(int(record[PRODUZIONE_INDICE_BADGE]))

            self._table_content_original.append(prod)

        self._InitGridContent()

    def _aggiorna(self, evt):
        self._window.aggiornaVisualizzaProduzione()

    def _refresh(self):
        self._window.aggiornaVisualizzaProduzione()

    def filtraRisultato(self, articolo, data):

       query = generaVisualizzaProduzioneQuery(articolo, data)

       print(query)

       if query is not None:
           self._RetriveTableContent(query)
       else:
           self._refresh()

