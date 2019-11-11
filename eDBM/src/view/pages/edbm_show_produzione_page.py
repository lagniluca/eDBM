# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la visualizzazione del tabbed pane flottante per la visualizzazione ed
il filtraggio della produzione
"""

import wx
import wx.adv

from eDBM.src.view.pages.components.edbm_produzione_dashboard import eDBMProduzioneDashboard
from eDBM.src.view.pages.components.edbm_produzione_grid_panel import eDBMProduzioneGridPanel


class eDBMShowProduzionePage(wx.Panel):
    def __init__(self, parent, dbconn):
        super(eDBMShowProduzionePage, self).__init__(parent)

        self._dbconn = dbconn

        self._notebook = wx.Notebook(self)
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        self._visualizzaProduzioneTab = wx.SplitterWindow(self._notebook, style=wx.SP_3DSASH)
        box = wx.BoxSizer(wx.VERTICAL)

        self._pan2 = eDBMProduzioneGridPanel(self._visualizzaProduzioneTab, parent, self._dbconn)
        self._pan1 = eDBMProduzioneDashboard(self._visualizzaProduzioneTab, self._dbconn, self._pan2)

        box.Add(self._pan1, wx.ID_ANY, wx.EXPAND | wx.ALL)
        box.Add(self._pan2, wx.ID_ANY, wx.EXPAND | wx.ALL)

        self._visualizzaProduzioneTab.SplitHorizontally(self._pan1, self._pan2, 200)

        self._visualizzaProduzioneTab.SetSizer(box)
        box.Fit(self._visualizzaProduzioneTab)

        self._notebook.AddPage(self._visualizzaProduzioneTab, "Visualizza produzione")

        generalSizer.Add(self._notebook, wx.ID_ANY, wx.EXPAND, 5)
        self.SetSizerAndFit(generalSizer)
