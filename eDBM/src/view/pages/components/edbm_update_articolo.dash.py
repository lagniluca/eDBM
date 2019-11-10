# -*- coding: utf-8 -*-

"""
Classe che contine il codice per la grafica usata per aggiornare un articolo
"""

# librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

class eDBMUpdateArticoloDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent):
        super(eDBMUpdateArticoloDash, self).__init__(super, style=wx.SUNKEN_BORDER)

        self.SetupScrolling()

    def _InitUI(self):
        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(13, 4, 9, 25)

        # codice
        self._aggiornaCodiceArticoloCheck = wx.CheckBox(self, wx.ID_ANY, u" vecchio codice:")
        self._vecchioCodiceArticoloCombo = wx.ComboBox(self, wx.ID_ANY)
        codice = wx.StaticText(self, label='=> nuovo codice: ')
        self._nuovoCodiceArticoloText = wx.TextCtrl(self)
        self._nuovoCodiceArticoloText.Enable(False)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._aggiungiDescrizioneArticoloText = wx.TextCtrl(self)

        # peso
        peso = wx.StaticText(self, label='peso:')
        self._aggiungiPesoArticoloText = wx.SpinCtrl(self)

        # rapporto
        rapporto = wx.StaticText(self, label='rapporto:')
        self._aggiungiRapportoArticoloText = wx.SpinCtrl(self)

        # inserto
        inserto = wx.StaticText(self, label='inserto:')
        self._aggiungiInsertoArticoloText = wx.TextCtrl(self)

        # quantità
        quantita = wx.StaticText(self, label="quantita':'")
        self._aggiungiQuantitaArticoloText = wx.SpinCtrl(self)

        # colore
        colore = wx.StaticText(self, label='colore:')
        self._aggiungiColoreArticoloText = wx.TextCtrl(self)

        # anticipo colore
        anticipo = wx.StaticText(self, label="anticipo colore:'")
        self._aggiungiAnticipoColoreArticoloText = wx.SpinCtrl(self)

        # programma C12
        programma_c12 = wx.StaticText(self, label='programma C12:')
        self._aggiungiProgrammaC12ArticoloText = wx.TextCtrl(self)

        # programma C25
        programma_c25 = wx.StaticText(self, label='programma C25:')
        self._aggiungiProgrammaC25ArticoloText = wx.TextCtrl(self)

        # data
        data = wx.StaticText(self, label='data:')
        self._aggiungiDataArticoloPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)

        # ora
        ora = wx.StaticText(self, label='ora:')
        self._aggiungiOraArticoloPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        # padding
        pad1 = wx.StaticText(self, label='')

        # bottone aggiungi
        self._aggiungiArticoloBtn = wx.Button(self, wx.ID_ANY, u"aggiungi")

        fgs.AddMany([
            (codice), (self._aggiungiCodiceArticoloText, wx.ID_ANY, wx.EXPAND),
            (descrizione), (self._aggiungiDescrizioneArticoloText, wx.ID_ANY, wx.EXPAND),
            (peso), (self._aggiungiPesoArticoloText, wx.ID_ANY, wx.EXPAND),
            (rapporto), (self._aggiungiRapportoArticoloText, wx.ID_ANY, wx.EXPAND),
            (inserto), (self._aggiungiInsertoArticoloText, wx.ID_ANY, wx.EXPAND),
            (quantita), (self._aggiungiQuantitaArticoloText, wx.ID_ANY, wx.EXPAND),
            (colore), (self._aggiungiColoreArticoloText, wx.ID_ANY, wx.EXPAND),
            (anticipo), (self._aggiungiAnticipoColoreArticoloText, wx.ID_ANY, wx.EXPAND),
            (programma_c12), (self._aggiungiProgrammaC12ArticoloText, wx.ID_ANY, wx.EXPAND),
            (programma_c25), (self._aggiungiProgrammaC25ArticoloText, wx.ID_ANY, wx.EXPAND),
            (data), (self._aggiungiDataArticoloPicker, wx.ID_ANY, wx.EXPAND),
            (ora), (self._aggiungiOraArticoloPicker, wx.ID_ANY, wx.EXPAND),
            (pad1), (self._aggiungiArticoloBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
        ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)