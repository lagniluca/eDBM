# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la pagine riguardante l'aggiunta di un articolo
"""

# Librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.view.pages.components.edbm_add_articolo_dash import eDBMAddArticoloDash


class eDBMAddArticoloPage(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent):
        super(eDBMAddArticoloPage, self).__init__(parent)

        self._notebook = wx.Notebook(self)
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        self._aggiungiArticoloTab = wx.Panel(self._notebook)
        box = wx.BoxSizer(wx.VERTICAL)

        self._pan1 = eDBMAddArticoloDash(self._aggiungiArticoloTab)

        box.Add(self._pan1, wx.ID_ANY, wx.EXPAND)
        self._aggiungiArticoloTab.SetSizer(box)
        box.Fit(self._aggiungiArticoloTab)

        self._notebook.AddPage(self._aggiungiArticoloTab, "Aggiungi articolo")

        generalSizer.Add(self._notebook, wx.ID_ANY, wx.EXPAND, 5)
        self.SetSizer(generalSizer)

