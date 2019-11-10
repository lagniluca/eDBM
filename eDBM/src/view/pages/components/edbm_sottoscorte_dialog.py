# -*- coding: utf-8 -*-

"""
Classe usata per rappresentare un dialog box nel caso di sottoscorte
"""

#librerie wx
import wx

class eDBMSottoscorteDialog(wx.Frame):
    def __init__(self, parent):
        super(eDBMSottoscorteDialog, self).__init__(parent, title='eDBM - Sottoscorte')

        self.SetIcon(wx.Icon('sottoscorte.png', wx.BITMAP_TYPE_PNG))
        self.SetSize((300, 300))

        self._InitUI()

    def _InitUI(self):
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel)
        hbox.Add(self.listbox, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Azzera', size=(90, 30))

        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        #self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(clrBtn)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

    def OnClear(self, evt):
        pass