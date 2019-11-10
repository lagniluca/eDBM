# -*- coding: utf-8 -*-

"""
Classe contenente il cruscotto per il filtraggio degli articoli
"""

# librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

class eDBMShowArticoliDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, dbm, gridPanel):
        super(eDBMShowArticoliDash, self).__init__(parent, style=wx.SUNKEN_BORDER)

        self.SetupScrolling()

        self._dbm = dbm
        self._gridPanel = gridPanel

        self.__InitUI()

    # setup interfaccia grafica del cruscotto articoli
    def __InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 4, 9, 25)

        # codice
        codice = wx.StaticText(self, label='codice:')
        self._codiceArticoliText = wx.TextCtrl(self)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._descrizioneArticoliText = wx.TextCtrl(self)

        # data
        data = wx.StaticText(self, label='data:')
        self._dataArticoliPicker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime)

        # ora
        ora = wx.StaticText(self, label='ora:')
        self._oraArticoliPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        # padding
        pad1 = wx.StaticText(self, label='')
        pad2 = wx.StaticText(self, label='')
        pad3 = wx.StaticText(self, label='')

        # filtra
        self._filtraArticoliBtn = wx.Button(self, label='filtra')

        fgs.AddMany([(codice), (self._codiceArticoliText, 1, wx.EXPAND | wx.ALL),  # (pad1),
                     (descrizione), (self._descrizioneArticoliText, 1, wx.EXPAND | wx.ALL),  # (pad2),
                     (data), (self._dataArticoliPicker, 1, wx.EXPAND | wx.ALL),
                     (ora), (self._oraArticoliPicker, 1, wx.EXPAND | wx.ALL),
                     (pad1), (pad2), (pad3), (self._filtraArticoliBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
                     ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableCol(3, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)

    # funzione usata per inizializzare la tabella
    def _InitGrid(self):
        pass



