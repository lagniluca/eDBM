# -*- coding: utf-8 -*-

"""
Class that contains the code used for managing the GUI related to
saved queries
"""

import wx


class SavedQueryPanel(wx.Panel):
    def __init__(self, parent):
        super(SavedQueryPanel, self).__init__(parent)
        self._InitUI()

    def _InitUI(self):
        # Components
        self._listBox = wx.ListBox(self)
        btnPanel = wx.Panel(self)
        self._eseguiBtn = wx.Button(btnPanel, wx.ID_ANY, 'Esegui', size=(90, 30))
        self._rimuoviBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rimuovi', size=(90, 30))

        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox.add(self._listBox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        vbox.Add((-1, 20))
        vbox.Add(self._eseguiBtn)
        vbox.Add(self._rimuoviBtn, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        self.SetSizer(hbox)


