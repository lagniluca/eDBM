# -*- coding: utf-8 -*-

"""
Class that contains the code for the main window of the application
"""

# wx libraries
import traceback

import wx
import wx.aui

from eDBM.src.controller.edbm_db_manager import eDBMDBManager
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog
from eDBM.src.view.pages.edbm_show_articoli_page import eDBMShowArticoliPage


class eDBMWindow(wx.Frame):

    def __init__(self, parent):
        super(eDBMWindow, self).__init__(parent, title='eDBM - Produzione')

        self._content_manager = wx.aui.AuiManager(self)

        #Manager del database
        self._dbm = None

        self._InitUI()

    # Method used for instantiating the GUI of the main window
    def _InitUI(self):

        # login
        self._InitLoginPanel()

        # window settings
        self.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
        self.SetSize((700, 500))
        self.Center()

    def _ShowArticoliPage(self):
        art = eDBMShowArticoliPage(self)
        info1 = wx.aui.AuiPaneInfo().Center()
        self._content_manager.AddPane(art, info1)
        self._content_manager.Update()

    def _InitToolBar(self):
        self._toolbar = self.CreateToolBar(style=wx.TB_BOTTOM)

        #disconnessione
        self._disconnettiTool = self._toolbar.AddTool(wx.ID_ANY, 'Disconnetti', wx.Bitmap('disconnetti.png'))
        self._sottoscorteTool = self._toolbar.AddTool(wx.ID_ANY, 'Sottoscorte', wx.Bitmap('warning.png'))

        self._toolbar.Realize()

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

        # Menu materie prime
        self._mpMenu = wx.Menu()

        self._aggiungiMPItem = self._mpMenu.Append(wx.ID_ANY, 'Aggiungi materia prima')
        self._mpMenu.AppendSeparator()
        self._modificaMPItem = self._mpMenu.Append(wx.ID_ANY, 'Modifica materia prima')
        self._mpMenu.AppendSeparator()
        self._visualizzaMPItem = self._mpMenu.Append(wx.ID_ANY, 'Visualizza materie prime')

        self._menubar.Append(self._mpMenu, '&Materie prime')

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
        self._dbm = eDBMDBManager(user, pwd, dbl)

        try:
            connesso = self._dbm.connettiDB()

            if connesso:
                md = eDBMMessageDialog('Connessione database produzione', 'Connessione stabilita', False)
                md.start()
                self._loginPanel.Hide()
                self._InitTopMenu()
                self._InitToolBar()
                self._ShowArticoliPage()
            else:
                md = eDBMMessageDialog('Connessione database produzione', 'Connessione NON stabilita', True)
                md.start()

        except Exception as e:
            track = traceback.format_exc()
            md = eDBMMessageDialog('Connessione database produzione - NON STABILITA - Eccezione lanciata', track, True)
            md.start()



