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
from eDBM.src.model.edbm_produzione import eDBMProduzione
from eDBM.src.model.exceptions.edbm_exception import eDBMException
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog

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
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_LOTTO_INSERTO, "Lotto inserto")
        self._grid.SetColLabelValue(PRODUZIONE_INDICE_BADGE, "Badge")

    def _InitGridContent(self):
        record = 0
        read_only = True

        for prod in self._table_content_original:

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ID, str(prod.getID()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ID, True)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LINEA, str(prod.getLinea()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LINEA, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ARTICOLO, str(prod.getArticolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ARTICOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_N_STAMPO, str(prod.getNumeroStampo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_N_STAMPO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PESO, str(prod.getPeso()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PESO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_RAPPORTO, str(prod.getRapporto()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_RAPPORTO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPO_COLATA, str(prod.getTempoColata()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPO_COLATA, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_QUANTITA_POLIOLO, str(prod.getQuantitaPoliolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_QUANTITA_POLIOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_POLIOLO, str(prod.getFlussoPoliolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_POLIOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPERATURA_POLIOLO, str(prod.getTemperaturaPoliolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPERATURA_POLIOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PRESSIONE_POLIOLO, str(prod.getPressionePoliolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PRESSIONE_POLIOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_QUANTITA_ISOCIANATO, str(prod.getQuantitaIsocianato()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_QUANTITA_ISOCIANATO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_ISOCIANATO, str(prod.getFlussoIsocianato()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_ISOCIANATO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO, str(prod.getTemperaturaIsocianato()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO, str(prod.getPressioneIsocianato()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_N_COLORE, str(prod.getNumColore()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_N_COLORE, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_PERCENTUALE_COLORE, str(prod.getPercentualeColore()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_PERCENTUALE_COLORE, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_FLUSSO_COLORE, str(prod.getFlussoColore()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_FLUSSO_COLORE, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ANTICIPO_COLORE, str(prod.getAnticipoColore()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ANTICIPO_COLORE, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_DATA, str(prod.getData()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_DATA, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_ORA, str(prod.getOra()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_ORA, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_POLIOLO, str(prod.getLottoPoliolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_POLIOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_ISOCIANATO, str(prod.getLottoIsocianato()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_ISOCIANATO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_COLORE, str(prod.getLottoColore()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_COLORE, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_ARTICOLO, str(prod.getLottoArticolo()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_ARTICOLO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_LOTTO_INSERTO, str(prod.getLottoInserto()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_LOTTO_INSERTO, read_only)

            self._grid.SetCellValue(record, PRODUZIONE_INDICE_BADGE, str(prod.getBadge()))
            self._grid.SetReadOnly(record, PRODUZIONE_INDICE_BADGE, read_only)

            record = record + 1

    def _InitUI(self):
        self._RetriveTableContent()

        self._grid = wx.grid.Grid(self)
        self._grid.CreateGrid(len(self._table_content_original), PRODUZIONE_NUMERO_CAMPI)

        self._InitGridHeader()
        self._InitGridContent()

        vbox = wx.BoxSizer(wx.VERTICAL)

        self._aggiornaBtn = wx.Button(self, wx.ID_ANY, u'Aggiorna')
        self._aggiornaBtn.Bind(wx.EVT_BUTTON, self._aggiorna)

        vbox.Add(self._aggiornaBtn, flag=wx.LEFT | wx.TOP, border=10)

        # Placement of the grid component inside the panel
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(1, 2, 9, 25)

        fgs.AddMany([
            (vbox, wx.ID_ANY, wx.ALIGN_RIGHT),
            (self._grid, wx.ID_ANY, wx.EXPAND | wx.ALIGN_LEFT)
        ])

        fgs.AddGrowableCol(1, 1)

        sizer.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.SetSizer(sizer)
        sizer.Fit(self)

    def _RetriveTableContent(self):
        self._table_content_original = list()
        query = "SELECT * FROM produzione_cosmec"
        cursor = self._dbm.connessione().cursor()
        cursor.execute(query)

        for record in cursor.fetchall():
            # creazione dell'oggetto materia prima per ogni record
            prod = eDBMProduzione()

            prod.setID(int(record[PRODUZIONE_INDICE_ID]))
            prod.setLinea(str(record[PRODUZIONE_INDICE_LINEA]))
            prod.setArticolo(str(record[PRODUZIONE_INDICE_ARTICOLO]))
            prod.setNumeroStampo(int(record[PRODUZIONE_INDICE_N_STAMPO]))
            prod.setPeso(int(record[PRODUZIONE_INDICE_PESO]))
            prod.setRapporto(int(record[PRODUZIONE_INDICE_RAPPORTO]))
            prod.setTempoColata(int(record[PRODUZIONE_INDICE_TEMPO_COLATA]))
            prod.setQuantitaPoliolo(int(record[PRODUZIONE_INDICE_QUANTITA_POLIOLO]))
            prod.setFlussoPoliolo(int(record[PRODUZIONE_INDICE_FLUSSO_POLIOLO]))
            prod.setTemperaturaPoliolo(int(record[PRODUZIONE_INDICE_TEMPERATURA_POLIOLO]))
            prod.setPressionePoliolo(int(record[PRODUZIONE_INDICE_PRESSIONE_POLIOLO]))
            prod.setQuantitaIsocianato(int(record[PRODUZIONE_INDICE_QUANTITA_ISOCIANATO]))
            prod.setFlussoIsocianato((int(prod[PRODUZIONE_INDICE_FLUSSO_ISOCIANATO])))
            prod.setTemperaturaIsocianato(int(prod[PRODUZIONE_INDICE_TEMPERATURA_ISOCIANATO]))
            prod.setPressioneIsocianato(int(prod[PRODUZIONE_INDICE_PRESSIONE_ISOCIANATO]))
            prod.setNumColore(int(prod[PRODUZIONE_INDICE_N_COLORE]))
            prod.setPercentualeColore(int(prod[PRODUZIONE_INDICE_PERCENTUALE_COLORE]))
            prod.setFlussoColore(int(prod[PRODUZIONE_INDICE_FLUSSO_COLORE]))
            prod.setAnticipoColore(int(prod[PRODUZIONE_INDICE_ANTICIPO_COLORE]))
            data = str(record[PRODUZIONE_INDICE_DATA].strftime("%d/%m/%Y"))
            prod.setData(data)
            ora = str(record[PRODUZIONE_INDICE_ORA].strftime("%H:%M:%S"))
            prod.setOra(str(ora))
            prod.setLottoPoliolo(str(prod[PRODUZIONE_INDICE_LOTTO_POLIOLO]))
            prod.setLottoIsocianato(str(prod[PRODUZIONE_INDICE_LOTTO_ISOCIANATO]))
            prod.setLottoColore(str(prod[PRODUZIONE_INDICE_LOTTO_COLORE]))
            prod.setLottoArticolo(str(prod[PRODUZIONE_INDICE_LOTTO_ARTICOLO]))
            prod.setLottoInserto(str(prod[PRODUZIONE_INDICE_LOTTO_INSERTO]))
            prod.setBadge(str(prod[PRODUZIONE_INDICE_BADGE]))

            self._table_content_original.append(prod)

    def _aggiorna(self, evt):
        self._window.aggiornaVisualizzaMateriePrime()

    def filtraRisultato(self, codice, descrizione, data, ora):
        codice_flag = False
        descrizione_flag = False
        data_flag = False
        ora_flag = False

        if codice is not None:
            if not codice:
                pass
            else:
                codice_flag = True

        if descrizione is not None:
            descrizione_flag = True

        if data is not None:
            if not data:
                pass
            else:
                data_flag = True

        if ora is not None:
            if not ora:
                pass
            else:
                ora_flag = True

        row = 0

        for mp in self._table_content_original:
            if codice_flag:
                if codice != mp.getCodice():
                    self._grid.HideRow(row)
                    row = row + 1
                    continue
            else:
                self._grid.ShowRow(row)

            if descrizione_flag:
                if mp.getDescrizione() is None:
                    if not descrizione:
                        self._grid.ShowRow(row)
                    else:
                        self._grid.HideRow(row)
                        row = row + 1
                        continue
                else:
                    if descrizione != mp.getDescrizione():
                        self._grid.HideRow(row)
                        row = row + 1
                        continue
            else:
                self._grid.ShowRow(row)

            if data_flag:
                if data != mp.getData():
                    self._grid.HideRow(row)
                    row = row + 1
                    continue
            else:
                self._grid.ShowRow(row)

            if ora_flag:
                if ora != mp.getOra():
                    self._grid.HideRow(row)
                    row = row + 1
                    continue
            else:
                self._grid.ShowRow(row)

            row = row + 1