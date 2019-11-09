# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la visualizzazione del tabbed pane flottante per la visualizzazione ed
il filtraggio degli articoli
"""

# librerie wx
import wx
import wx.adv

from eDBM.src.view.pages.components.edbm_grid_panel import eDBMGridPanel
from eDBM.src.view.pages.components.edbm_show_articoli_dash import eDBMShowArticoliDash


class eDBMShowArticoliPage(wx.Panel):
    def __init__(self, parent):
        super(eDBMShowArticoliPage, self).__init__(parent)

        self._notebook = wx.Notebook(self)
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        # visualizza articoli
        self._visualizzaArticoliTab = wx.SplitterWindow(self._notebook)
        box = wx.BoxSizer(wx.VERTICAL)

        self._pan1 = eDBMShowArticoliDash(self._visualizzaArticoliTab)
        self._pan2 = eDBMGridPanel(self._visualizzaArticoliTab)

        box.Add(self._pan1, wx.ID_ANY, wx.EXPAND | wx.ALL )
        box.Add(self._pan2, wx.ID_ANY, wx.EXPAND | wx.ALL)

        self._visualizzaArticoliTab.SplitHorizontally(self._pan1, self._pan2, 200)

        self._visualizzaArticoliTab.SetSizer(box)
        box.Fit(self._visualizzaArticoliTab)

        self._notebook.AddPage(self._visualizzaArticoliTab, "Visualizza")

        generalSizer.Add(self._notebook,wx.ID_ANY, wx.EXPAND, 5)

        self.SetSizerAndFit(generalSizer)



