# -*- coding: utf-8 -*-

"""
Class used for creating a grid component
"""

# wx Libraries
import datetime

import wx
import wx.grid

# Access libraries
import pyodbc

from eDBM.src.model.edbm_materia_prima import eDBMMateriaPrima


class eDBMMateriePrimeGridPanel(wx.Panel):
    def __init__(self, parent, window, dbm, alter_flag):
        super(eDBMMateriePrimeGridPanel, self).__init__(parent, style=wx.BORDER_RAISED)

        self._window = window

        self._dbm = dbm
        self._alter_flag = alter_flag  # flag usato per stabilire se la griglia è per la modifica (True) o la semplice visualizzazione (False)

        self._table_content_original = list()  # contenuti della tabella subito dopo il commit
        self._table_content_altered = list()  # contenuti alterati della tabella
        self._table_content_deleted = list()  # record eliminati dalla tabella

        self._grid = None

        self._InitUI()

    def _InitGridHeader(self):
        position = 0

        self._grid.SetColLabelValue(position, "ID")
        position = position + 1
        self._grid.SetColLabelValue(position, "Codice")
        position = position + 1
        self._grid.SetColLabelValue(position, "Descrizione")
        position = position + 1
        self._grid.SetColLabelValue(position, "Lotto")
        position = position + 1
        self._grid.SetColLabelValue(position, "Registrazione")
        position = position + 1
        self._grid.SetColLabelValue(position, "Tipo")
        position = position + 1
        self._grid.SetColLabelValue(position, "Data")
        position = position + 1
        self._grid.SetColLabelValue(position, "Ora")
        position = position + 1
        self._grid.SetColLabelValue(position, "DDT")
        position = position + 1
        self._grid.SetColLabelValue(position, "Data DDT")

    def _InitGridContent(self):
        row = 0
        column = 0
        read_only = not self._alter_flag

        for mp in self._table_content_original:
            column = 0

            self._grid.SetCellValue(row, column, str(mp.getID()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getCodice()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            if mp.getDescrizione() is not None:
                self._grid.SetCellValue(row, column, str(mp.getDescrizione()))
            else:
                self._grid.SetCellValue(row, column, str(''))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getLotto()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getRegistrazione()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getTipo()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getData()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getOra()))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            if mp.getDDT() is not None:
                self._grid.SetCellValue(row, column, str(mp.getDDT()))
            else:
                self._grid.SetCellValue(row, column, str(''))
            self._grid.SetReadOnly(row, column, read_only)
            column = column + 1
            self._grid.SetCellValue(row, column, str(mp.getDataDDT()))
            self._grid.SetReadOnly(row, column, read_only)

            row = row + 1

    def _InitGrid(self):
        self._RetriveTableContent()
        # Grid component
        self._grid = wx.grid.Grid(self)
        self._grid.CreateGrid(len(self._table_content_original), 10)

        self._InitGridHeader()
        self._InitGridContent()

    # Method used for defying the UI of the panel
    def _InitUI(self):
        #self._grid = wx.grid.Grid(self)
        self._InitGrid()

        vbox = wx.BoxSizer(wx.VERTICAL)

        self._aggiornaBtn = wx.Button(self, wx.ID_ANY, u'Aggiorna')
        self._aggiornaBtn.Bind(wx.EVT_BUTTON, self._aggiorna)

        if self._alter_flag :
            self._modificaBtn = wx.Button(self, wx.ID_ANY, u'Modifica')
            self._eliminaBtn = wx.Button(self, wx.ID_ANY, u'Elimina')

        vbox.Add(self._aggiornaBtn, flag=wx.LEFT|wx.TOP, border=10)

        if self._alter_flag :
            vbox.Add(self._modificaBtn, flag=wx.LEFT|wx.CENTER, border=10)
            vbox.Add(self._eliminaBtn, flag=wx.LEFT | wx.BOTTOM, border=10)

        # Example of column header setting
        # self._grid.SetColLabelValue(0, "ID")
        # self._grid.SetColLabelValue(1, "Codice")

        # Example of setting the value of a cell
        # self._grid.SetCellValue(0, 0, "cell 0")
        # self._grid.SetCellBackgroundColour(0, 0, wx.RED)
        # self._grid.SetCellTextColour(0, 0, wx.WHITE)
        # self._grid.SetReadOnly(0, 0, True)

        # Example of custom type grid cell
        # self._grid.SetCellEditor(1, 1, wx.grid.GridCellNumberEditor(1, 20))

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
        query = "SELECT * FROM materie_prime"
        cursor = self._dbm.connessione().cursor()
        cursor.execute(query)
        # self._dbm.connessione().commit()

        for record in cursor.fetchall():
            # creazione dell'oggetto materia prima per ogni record
            mp = eDBMMateriaPrima()

            mp.setID(int(record[0]))
            mp.setCodice(record[1])
            if record[2] is not None:
                mp.setDescrizione(record[2])
            mp.setLotto(record[3])
            mp.setRegistrazione(record[4])
            mp.setTipo(int(record[5]))
            data = str(record[6].strftime("%d/%m/%Y"))
            mp.setData(data)
            ora = str(record[7].strftime("%H:%M:%S"))
            mp.setOra(str(ora))
            if record[8] is not None:
                mp.setDDT(record[8])
            data_ddt = str(record[9].strftime("%H:%M:%S"))
            mp.setDataDDT(data_ddt)

            # aggiunta alla lista dell'oggetto materia prima
            self._table_content_original.append(mp)

    def _aggiorna(self, evt):
        #self._InitGrid()
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
