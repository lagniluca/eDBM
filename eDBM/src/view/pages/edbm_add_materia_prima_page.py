# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la pagine riguardante l'aggiunta di una materia prima
"""

# Librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.view.pages.components.edbm_add_materia_prima_dash import eDBMAddMateriaPrimaDash


class eDBMAddMateriaPrimaPage(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, window, dbm):
        super(eDBMAddMateriaPrimaPage, self).__init__(parent)

        self._notebook = wx.Notebook(self)
        generalSizer = wx.BoxSizer(wx.HORIZONTAL)

        self._aggiungiMateriaPrimaTab = wx.Panel(self._notebook)
        box = wx.BoxSizer(wx.VERTICAL)

        self._pan1 = eDBMAddMateriaPrimaDash(self._aggiungiMateriaPrimaTab, window, dbm)

        box.Add(self._pan1, wx.ID_ANY, wx.EXPAND)
        self._aggiungiMateriaPrimaTab.SetSizer(box)
        box.Fit(self._aggiungiMateriaPrimaTab)

        self._notebook.AddPage(self._aggiungiMateriaPrimaTab, "Aggiungi materia prima")

        generalSizer.Add(self._notebook, wx.ID_ANY, wx.EXPAND, 5)
        self.SetSizer(generalSizer)