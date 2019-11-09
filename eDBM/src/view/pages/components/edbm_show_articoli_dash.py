# -*- coding: utf-8 -*-

"""
Classe contenente il cruscotto per il filtraggio degli articoli
"""

# librerie wx
import wx
import wx.adv

class eDBMShowArticoliDash(wx.Panel):
    def __init__(self, parent):
        super(eDBMShowArticoliDash, self).__init__(parent, style=wx.SUNKEN_BORDER)

        self.__InitUI()

    def __InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(1, 4, 9, 25)

        # codice
        codice = wx.StaticText(self, label='codice:')
        self._codiceArticoliText = wx.TextCtrl(self)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._descrizioneArticoliText = wx.TextCtrl(self)

        # data

        fgs.AddMany([(codice), (self._codiceArticoliText, 1, wx.EXPAND | wx.ALL),  # (pad1),
                     (descrizione), (self._descrizioneArticoliText, 1, wx.EXPAND | wx.ALL)  # (pad2),
                     ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableCol(3, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)




