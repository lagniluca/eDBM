# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la visualizzazione del tabbed pane flottante per la visualizzazione ed
il filtraggio delle materie prime
"""

# librerie wx
import wx
import wx.adv

from eDBM.src.view.pages.components.edbm_materie_prime_grid_panel import eDBMMateriePrimeGridPanel
from eDBM.src.view.pages.components.edbm_show_materie_prime_dash import eDBMShowMateriePrimeDash


class eDBMShowMateriePrimePage(wx.Panel):
    def __init__(self, parent, dbconn, alter):
        super(eDBMShowMateriePrimePage, self).__init__(parent)

        self._dbconn = dbconn

        self._notebook = wx.Notebook(self)
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        # visualizza articoli
        self._visualizzaMateriePrimeTab = wx.SplitterWindow(self._notebook, style=wx.SP_3DSASH)
        box = wx.BoxSizer(wx.VERTICAL)

        self._pan2 = eDBMMateriePrimeGridPanel(self._visualizzaMateriePrimeTab, parent, dbconn, alter)
        self._pan1 = eDBMShowMateriePrimeDash(self._visualizzaMateriePrimeTab, self._dbconn, self._pan2)

        box.Add(self._pan1, wx.ID_ANY, wx.EXPAND | wx.ALL)
        box.Add(self._pan2, wx.ID_ANY, wx.EXPAND | wx.ALL)

        self._visualizzaMateriePrimeTab.SplitHorizontally(self._pan1, self._pan2, 200)

        self._visualizzaMateriePrimeTab.SetSizer(box)
        box.Fit(self._visualizzaMateriePrimeTab)

        self._notebook.AddPage(self._visualizzaMateriePrimeTab, "Visualizza materie prime")

        generalSizer.Add(self._notebook, wx.ID_ANY, wx.EXPAND, 5)
        self.SetSizerAndFit(generalSizer)
