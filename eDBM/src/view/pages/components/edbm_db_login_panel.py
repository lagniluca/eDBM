# -*- coding: utf-8 -*-

"""
Pagina grafica per l'inserimento dei dat relativi alla connessione con il database
 Non utilizzata ma mantenuta per test su eventuali modifiche
"""
import traceback

import wx

from eDBM.src.controller.edbm_db_manager import eDBMDBManager


class eDBMDBLoginPanel(wx.Panel):

    def __init__(self, parent):
        super(eDBMDBLoginPanel, self).__init__(parent)

        self._InitUI()

    def _InitUI(self):
        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(4, 2, 9, 25)

        # user login
        user = wx.StaticText(self, label='utente:')
        self._userLoginText = wx.TextCtrl(self, style=wx.TE_READONLY)
        #pad1 = wx.StaticText(self, label='') # padding element

        # password login
        pwd = wx.StaticText(self, label='password:')
        self._pwdLoginText = wx.TextCtrl(self, style=wx.TE_PASSWORD|wx.TE_READONLY)
        #pad2 = wx.StaticText(self, label='')  # padding element

        # database location
        dbl = wx.StaticText(self, label='database:')
        self._dblLoginPicker = 	wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Seleziona file MS Access (.mdb)", u"*.mdb", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        #pad3 = wx.StaticText(self, label='')  # padding element

        # connection button
        pad4 = wx.StaticText(self, label='')  # padding element
        #pad5 = wx.StaticText(self, label='')  # padding element
        self._connettiDBLoginBtn = wx.Button(self, wx.ID_ANY, u"connetti")
        self._connettiDBLoginBtn.Bind(wx.EVT_BUTTON, self._connettiDB)

        fgs.AddMany([(user), (self._userLoginText, 1, wx.EXPAND), #(pad1),
                     (pwd), (self._pwdLoginText, 1, wx.EXPAND), #(pad2),
                     (dbl), (self._dblLoginPicker, 1, wx.EXPAND), #(pad3),
                     (pad4), (self._connettiDBLoginBtn, wx.ID_ANY, wx.ALIGN_RIGHT), #(pad5)
                     ])

        """
        Righe e colonne espandibili
        """
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizer(hbox)

    # Metodo richiamato dal button per stabilire la connessione al database
    def _connettiDB(self, evt):
        user = None #self._userLoginText.GetValue()
        pwd = None #self._pwdLoginText.GetValue()
        dbl = self._dblLoginPicker.GetPath()
        dbm = eDBMDBManager(user, pwd, dbl)

        try:
            connesso = dbm.connettiDB()

            if connesso:
                wx.MessageBox('Connessione stabilita', 'Connessione database produzione', wx.OK | wx.ICON_INFORMATION)
            else:
                wx.MessageBox('Connessione NON stabilita', 'Connessione database produzione', wx.OK | wx.ICON_ERROR)

        except Exception as e :
            track = traceback.format_exc()
            wx.MessageBox( track, 'Connessione database produzione - NON STABILITA - Eccezione lanciata', wx.OK | wx.ICON_ERROR)
