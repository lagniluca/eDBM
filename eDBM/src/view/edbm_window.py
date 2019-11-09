# -*- coding: utf-8 -*-

"""
Class that contains the code for the main window of the application
"""

# wx libraries
import traceback

import wx

from eDBM.src.controller.edbm_db_manager import eDBMDBManager
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog


class eDBMWindow(wx.Frame):

    def __init__(self, parent):
        super(eDBMWindow, self).__init__(parent, title='eDBM - Produzione')

        self._InitUI()

    def _InitUI(self):
        # Layout of the frame
        # layout = wx.GridSizer(1, 1, 1, 1)
        # self.SetSizer(layout)

        # login
        self._InitLoginPanel()

        # Setting the topbar menu
        # self._InitTopMenu()
        self.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
        self.SetSize((700, 500))
        self.Center()

    # Method used for displaying the connection panel
    def _InitLoginPanel(self):
        self._loginPanel = wx.Panel(self)

        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(4, 2, 9, 25)

        # user login
        user = wx.StaticText(self._loginPanel, label='utente:')
        self._userLoginText = wx.TextCtrl(self._loginPanel, style=wx.TE_READONLY)
        # pad1 = wx.StaticText(self, label='') # padding element

        # password login
        pwd = wx.StaticText(self._loginPanel, label='password:')
        self._pwdLoginText = wx.TextCtrl(self._loginPanel, style=wx.TE_PASSWORD | wx.TE_READONLY)
        # pad2 = wx.StaticText(self._loginPanel, label='')  # padding element

        # database location
        dbl = wx.StaticText(self._loginPanel, label='database:')
        self._dblLoginPicker = wx.FilePickerCtrl(self._loginPanel, wx.ID_ANY, wx.EmptyString,
                                                 u"Seleziona file MS Access (.mdb)",
                                                 u"*.mdb", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        # pad3 = wx.StaticText(self._loginPanel, label='')  # padding element

        # connection button
        pad4 = wx.StaticText(self._loginPanel, label='')  # padding element
        # pad5 = wx.StaticText(self._loginPanel, label='')  # padding element
        self._connettiDBLoginBtn = wx.Button(self._loginPanel, wx.ID_ANY, u"connetti", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self._connettiDBLoginBtn.Bind(wx.EVT_BUTTON, self._connettiDB)

        fgs.AddMany([(user), (self._userLoginText, 1, wx.EXPAND),  # (pad1),
                     (pwd), (self._pwdLoginText, 1, wx.EXPAND),  # (pad2),
                     (dbl), (self._dblLoginPicker, 1, wx.EXPAND),  # (pad3),
                     (pad4), (self._connettiDBLoginBtn, 1, wx.EXPAND),  # (pad5)
                     ])

        """
        Righe e colonne espandibili
        """
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self._loginPanel.SetSizer(hbox)

    # Method used for initialize the top bar
    def _InitTopMenu(self):
        self._menubar = wx.MenuBar()

        # Menu articoli
        self._articoliMenu = wx.Menu()

        self._aggiungiArticoloItem = self._articoliMenu.Append(wx.ID_ANY, 'Aggiungi articolo')
        self._articoliMenu.AppendSeparator()
        self._modificaArticoloItem = self._articoliMenu.Append(wx.ID_ANY, 'Modifica articolo')
        self._articoliMenu.AppendSeparator()
        self._visualizzaArticoloItem = self._articoliMenu.Append(wx.ID_ANY, 'Visualizza articoli')

        self._menubar.Append(self._articoliMenu, '&Articoli')

        # Menu ricette
        self._ricetteMenu = wx.Menu()

        self._aggiungiRicettaItem = self._ricetteMenu.Append(wx.ID_ANY, 'Aggiungi ricetta')
        self._ricetteMenu.AppendSeparator()
        self._modificaRicettaItem = self._ricetteMenu.Append(wx.ID_ANY, 'Modifica ricetta')
        self._ricetteMenu.AppendSeparator()
        self._visualizzaRicettaItem = self._ricetteMenu.Append(wx.ID_ANY, 'Visualizza ricette')

        self._menubar.Append(self._ricetteMenu, '&Ricette')

        # Menu produzione
        self._produzioneMenu = wx.Menu()

        self._visualizzaProduzioneItem = self._produzioneMenu.Append(wx.ID_ANY, 'Visualizza produzione')

        self._menubar.Append(self._produzioneMenu, '&Produzione')

        self.SetMenuBar(self._menubar)

    # Metodo richiamato dal button per stabilire la connessione al database
    def _connettiDB(self, evt):
        user = None  # self._userLoginText.GetValue()
        pwd = None  # self._pwdLoginText.GetValue()
        dbl = self._dblLoginPicker.GetPath()
        dbm = eDBMDBManager(user, pwd, dbl)

        try:
            connesso = dbm.connettiDB()

            if connesso:
                md = eDBMMessageDialog('Connessione database produzione', 'Connessione stabilita', False)
                md.start()
                self._loginPanel.Hide()
                self._InitTopMenu()
            else:
                md = eDBMMessageDialog('Connessione database produzione', 'Connessione NON stabilita', True)
                md.start()

        except Exception as e:
            track = traceback.format_exc()
            md = eDBMMessageDialog('Connessione database produzione - NON STABILITA - Eccezione lanciata', track, True)
            md.start()
