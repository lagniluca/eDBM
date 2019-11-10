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
from eDBM.src.view.pages.components.edbm_sottoscorte_dialog import eDBMSottoscorteDialog
from eDBM.src.view.pages.edbm_add_articolo_page import eDBMAddArticoloPage
from eDBM.src.view.pages.edbm_add_materia_prima_page import eDBMAddMateriaPrimaPage
from eDBM.src.view.pages.edbm_show_articoli_page import eDBMShowArticoliPage
from eDBM.src.view.pages.edbm_show_materie_prime_page import eDBMShowMateriePrimePage


class eDBMWindow(wx.Frame):

    def __init__(self, parent):
        super(eDBMWindow, self).__init__(parent, title='eDBM - Produzione')

        self._content_manager = wx.aui.AuiManager(self)
        self._current_central_panel = None # reference al pannello centrale corrente


        #Manager del database
        self._dbm = None

        self._InitUI()

    # Method used for instantiating the GUI of the main window
    def _InitUI(self):

        # login
        self._InitToolBar()
        self._InitLoginPanel()

        # window settings
        self.SetIcon(wx.Icon('logo.png', wx.BITMAP_TYPE_PNG))
        self.SetSize((700, 500))
        self.Center()

    def _ShowHomePage(self):
        self._loginPanel.Show(False)
        self._content_manager.Update()

    # Articoli
    def _ShowArticoliPage(self):
        pan = eDBMShowArticoliPage(self, self._dbm)
        info1 = wx.aui.AuiPaneInfo().Center().Dockable(True)
        self._content_manager.AddPane(pan, info1)
        self._content_manager.Update()
        self._current_central_panel = pan

    def _AddArticoloPage(self):
        pan = eDBMAddArticoloPage(self)
        info1 = wx.aui.AuiPaneInfo().Center().Dockable(True)
        self._content_manager.AddPane(pan, info1)
        self._content_manager.Update()
        self._current_central_panel = pan

    # Materie prime
    def _AddMateriaPrimaPage(self):
        pan = eDBMAddMateriaPrimaPage(self, self._dbm)
        info1 = wx.aui.AuiPaneInfo().Center().Dockable(True)
        self._content_manager.AddPane(pan, info1)
        self._content_manager.Update()
        self._current_central_panel = pan

    def _ShowMateriePrimePage(self):
        pan = eDBMShowMateriePrimePage(self, self._dbm)
        info1 = wx.aui.AuiPaneInfo().Center().Dockable(True)
        self._content_manager.AddPane(pan, info1)
        self._content_manager.Update()
        self._current_central_panel = pan

    def _InitToolBar(self):
        self._toolbar = self.CreateToolBar(style=wx.TB_BOTTOM)
        self._disconnettiTool = self._toolbar.AddTool(100, "Disconnetti", wx.Bitmap('logout.png'))
        self._toolbar.AddSeparator()
        self._infoTool = self._toolbar.AddTool(200, 'Info', wx.Bitmap('info.png'))
        self._toolbar.AddSeparator()
        #self._logsTool = self._toolbar.AddTool(300, 'Logs', wx.Bitmap('logs.png'))
        #self._toolbar.AddSeparator()
        self._sottoscorteTool = self._toolbar.AddTool(400, 'Sottoscorte', wx.Bitmap('sottoscorte.png'))

        self._toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self._OnSottoscorteClicked, self._sottoscorteTool)

        self._toolbar.EnableTool(100, False)
        self._toolbar.EnableTool(200, True)
        #self._toolbar.EnableTool(300, False)
        self._toolbar.EnableTool(400, True)

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
                     (pad4), (self._connettiDBLoginBtn, 1, wx.ALIGN_RIGHT),  # (pad5)
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
        self._visualizzaArticoloItem = self._articoliMenu.Append(wx.ID_ANY, 'Visualizza articolo')

        self.Bind(wx.EVT_MENU, self._AggiungiArticoloDBPageLoader, self._aggiungiArticoloItem)
        self.Bind(wx.EVT_MENU, self._VisualizzaArticoliDBPageLoader, self._visualizzaArticoloItem)

        self._menubar.Append(self._articoliMenu, '&Articoli')

        # Menu materie prime
        self._mpMenu = wx.Menu()

        self._aggiungiMPItem = self._mpMenu.Append(wx.ID_ANY, 'Aggiungi materia prima')
        self._mpMenu.AppendSeparator()
        self._modificaMPItem = self._mpMenu.Append(wx.ID_ANY, 'Modifica materia prima')
        self._mpMenu.AppendSeparator()
        self._visualizzaMPItem = self._mpMenu.Append(wx.ID_ANY, 'Visualizza materie prime')

        self.Bind(wx.EVT_MENU, self._AggiungiMateriaPrimaDBPageLoader, self._aggiungiMPItem)
        self.Bind(wx.EVT_MENU, self._VisualizzaMateriePrimeDBPageLoader, self._visualizzaMPItem)

        self._menubar.Append(self._mpMenu, '&Materie prime')

        # Menu produzione
        self._produzioneMenu = wx.Menu()

        self._visualizzaProduzioneItem = self._produzioneMenu.Append(wx.ID_ANY, 'Visualizza produzione')

        self._menubar.Append(self._produzioneMenu, '&Produzione')

        self.SetMenuBar(self._menubar)

    # metodo usato per rimuovere il pannello centrale dalla finestra
    def _CleanWindowsCentralPanel(self):
        if self._current_central_panel is not None:
            self._content_manager.DetachPane(self._current_central_panel)
            self._current_central_panel.Destroy()
        self._content_manager.Update()

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
                self._ShowHomePage()
            else:
                md = eDBMMessageDialog('Connessione database produzione', 'Connessione NON stabilita', True)
                md.start()

        except Exception as e:
            track = traceback.format_exc()
            md = eDBMMessageDialog('Connessione database produzione - NON STABILITA - Eccezione lanciata', track, True)
            md.start()

    # Articoli
    def _VisualizzaArticoliDBPageLoader(self, evt):
        self._CleanWindowsCentralPanel()
        self._loginPanel.Hide()
        self._ShowArticoliPage()

    def _AggiungiArticoloDBPageLoader(self, evt):
        self._CleanWindowsCentralPanel()
        self._loginPanel.Hide()
        self._AddArticoloPage()

    # Materie prime
    def _AggiungiMateriaPrimaDBPageLoader(self, evt):
        self._CleanWindowsCentralPanel()
        self._AddMateriaPrimaPage()

    def _VisualizzaMateriePrimeDBPageLoader(self, evt):
        self._CleanWindowsCentralPanel()
        self._ShowMateriePrimePage()

    def _OnSottoscorteClicked(self, evt):
        dia = eDBMSottoscorteDialog(None)
        dia.Show(True)

    def aggiornaVisualizzaMateriePrime(self):
        self._CleanWindowsCentralPanel()
        self._ShowMateriePrimePage()



