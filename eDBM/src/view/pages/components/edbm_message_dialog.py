# -*- coding: utf-8 -*-

"""
Classe utilizzata per visualizzare messaggi in maniera asincrona
"""

# librerie standard
from threading import Thread
import time

# librerie wx
import wx

class eDBMMessageDialog(Thread):
    def __init__(self, intestazione, messaggio, errore):
        Thread.__init__(self)

        self.intestazione = intestazione
        self.messaggio = messaggio
        self.errore = errore

    def run(self):
        if not self.errore :
            wx.MessageBox(self.messaggio, self.intestazione, wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox(self.messaggio, self.intestazione, wx.OK | wx.ICON_ERROR)
