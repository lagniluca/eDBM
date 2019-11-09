# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.aui
import wx.grid
import wx.adv

class eDBMWindow(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"eDBM - Produzione", pos=wx.DefaultPosition,
                          size=wx.Size(1134, 772), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

        self._menuBar = wx.MenuBar(0)
        self._articoliMenu = wx.Menu()
        self._aggiungiArticoloMenu = wx.MenuItem(self._articoliMenu, wx.ID_ANY, u"Aggiungi Articolo", wx.EmptyString,
                                                 wx.ITEM_NORMAL)
        self._articoliMenu.Append(self._aggiungiArticoloMenu)

        self._articoliMenu.AppendSeparator()

        self._modificaArticoloMenu = wx.MenuItem(self._articoliMenu, wx.ID_ANY, u"Modifica Articolo", wx.EmptyString,
                                                 wx.ITEM_NORMAL)
        self._articoliMenu.Append(self._modificaArticoloMenu)

        self._articoliMenu.AppendSeparator()

        self._visualizzaArticoliMenu = wx.MenuItem(self._articoliMenu, wx.ID_ANY, u"Visualizza Articoli",
                                                   wx.EmptyString, wx.ITEM_NORMAL)
        self._articoliMenu.Append(self._visualizzaArticoliMenu)

        self._menuBar.Append(self._articoliMenu, u"Articoli")

        self._ricetteMenu = wx.Menu()
        self._aggiungiRicettaMenu = wx.MenuItem(self._ricetteMenu, wx.ID_ANY, u"Aggiungi Ricetta", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self._ricetteMenu.Append(self._aggiungiRicettaMenu)

        self._ricetteMenu.AppendSeparator()

        self._modificaRicettaMenu = wx.MenuItem(self._ricetteMenu, wx.ID_ANY, u"Modifica Ricetta", wx.EmptyString,
                                                wx.ITEM_NORMAL)
        self._ricetteMenu.Append(self._modificaRicettaMenu)

        self._ricetteMenu.AppendSeparator()

        self._visualizzaRicetteMenu = wx.MenuItem(self._ricetteMenu, wx.ID_ANY, u"Visualizza Ricette", wx.EmptyString,
                                                  wx.ITEM_NORMAL)
        self._ricetteMenu.Append(self._visualizzaRicetteMenu)

        self._menuBar.Append(self._ricetteMenu, u"Ricette")

        self._produzioneMenu = wx.Menu()
        self._visualizzaProduzioneMenu = wx.MenuItem(self._produzioneMenu, wx.ID_ANY, u"Visualizza Produzione",
                                                     wx.EmptyString, wx.ITEM_NORMAL)
        self._produzioneMenu.Append(self._visualizzaProduzioneMenu)

        self._menuBar.Append(self._produzioneMenu, u"Produzione")

        self.SetMenuBar(self._menuBar)

        self._visualizzaArticoliBook = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self._visualizzaArticoliBook,
                           wx.aui.AuiPaneInfo().Left().PinButton(True).Dock().Resizable().FloatingSize(wx.DefaultSize))

        self._ricercaVeloceArticoloPanel = wx.Panel(self._visualizzaArticoliBook, wx.ID_ANY, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer2 = wx.GridSizer(1, 1, 0, 0)

        gSizer2.SetMinSize(wx.Size(500, 500))
        self.m_splitter5 = wx.SplitterWindow(self._ricercaVeloceArticoloPanel, wx.ID_ANY, wx.DefaultPosition,
                                             wx.DefaultSize, wx.SP_3DSASH | wx.SP_NO_XP_THEME)
        self.m_splitter5.Bind(wx.EVT_IDLE, self.m_splitter5OnIdle)

        self._filtraArticoliPanel = wx.Panel(self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.RAISED_BORDER)
        gSizer6 = wx.GridSizer(3, 4, 0, 0)

        self.m_staticText5 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, u"Codice:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer6.Add(self.m_staticText5, 0, wx.ALL, 5)

        self._codiceArticoloText = wx.TextCtrl(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        gSizer6.Add(self._codiceArticoloText, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, u"Descrizione:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)

        self._descrizioneArticoloText = wx.TextCtrl(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer6.Add(self._descrizioneArticoloText, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, u"Data:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        gSizer6.Add(self.m_staticText7, 0, wx.ALL, 5)

        self._dataArticoloText = wx.adv.DatePickerCtrl(self._filtraArticoliPanel, wx.ID_ANY, wx.DefaultDateTime,
                                                   wx.DefaultPosition, wx.DefaultSize)
        gSizer6.Add(self._dataArticoloText, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, u"Ora:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        gSizer6.Add(self.m_staticText8, 0, wx.ALL, 5)

        self._oraArticoloText = wx.SpinCtrl(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 5)
        gSizer6.Add(self._oraArticoloText, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        gSizer6.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        gSizer6.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self._filtraArticoliPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        gSizer6.Add(self.m_staticText10, 0, wx.ALL, 5)

        self._cercaArticoliButton = wx.Button(self._filtraArticoliPanel, wx.ID_ANY, u"cerca", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        gSizer6.Add(self._cercaArticoliButton, 0, wx.ALL, 5)

        self._filtraArticoliPanel.SetSizer(gSizer6)
        self._filtraArticoliPanel.Layout()
        gSizer6.Fit(self._filtraArticoliPanel)
        self.m_panel5 = wx.Panel(self.m_splitter5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer4 = wx.GridSizer(1, 1, 0, 0)

        self.m_grid9 = wx.grid.Grid(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid9.CreateGrid(5, 5)
        self.m_grid9.EnableEditing(True)
        self.m_grid9.EnableGridLines(True)
        self.m_grid9.EnableDragGridSize(False)
        self.m_grid9.SetMargins(0, 0)

        # Columns
        self.m_grid9.EnableDragColMove(False)
        self.m_grid9.EnableDragColSize(True)
        self.m_grid9.SetColLabelSize(30)
        self.m_grid9.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.m_grid9.EnableDragRowSize(True)
        self.m_grid9.SetRowLabelSize(80)
        self.m_grid9.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid9.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gSizer4.Add(self.m_grid9, 0, wx.ALL, 5)

        self.m_panel5.SetSizer(gSizer4)
        self.m_panel5.Layout()
        gSizer4.Fit(self.m_panel5)
        self.m_splitter5.SplitHorizontally(self._filtraArticoliPanel, self.m_panel5, 0)
        gSizer2.Add(self.m_splitter5, 1, wx.EXPAND, 5)

        self._ricercaVeloceArticoloPanel.SetSizer(gSizer2)
        self._ricercaVeloceArticoloPanel.Layout()
        gSizer2.Fit(self._ricercaVeloceArticoloPanel)
        self._visualizzaArticoliBook.AddPage(self._ricercaVeloceArticoloPanel, u"a page", False, wx.NullBitmap)
        self._ricercaProfondaArticoloPanel = wx.Panel(self._visualizzaArticoliBook, wx.ID_ANY, wx.DefaultPosition,
                                                      wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer61 = wx.GridSizer(18, 4, 0, 0)

        self._daIDArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"(Da) ID :",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._daIDArticoloCheck, 0, wx.ALL, 5)

        self._daIDArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self._daIDArticoloText.Enable(False)

        gSizer61.Add(self._daIDArticoloText, 0, wx.ALL, 5)

        self._aIDArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"a ID:",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self._aIDArticoloCheck.Enable(False)

        gSizer61.Add(self._aIDArticoloCheck, 0, wx.ALL, 5)

        self._aIDArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self._aIDArticoloText.Enable(False)

        gSizer61.Add(self._aIDArticoloText, 0, wx.ALL, 5)

        self._codiceArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Codice:",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._codiceArticoloCheck, 0, wx.ALL, 5)

        self._codiceArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self._codiceArticoloText.Enable(False)

        gSizer61.Add(self._codiceArticoloText, 0, wx.ALL, 5)

        self.m_staticText221 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText221.Wrap(-1)
        gSizer61.Add(self.m_staticText221, 0, wx.ALL, 5)

        self.m_staticText231 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText231.Wrap(-1)
        gSizer61.Add(self.m_staticText231, 0, wx.ALL, 5)

        self._descrizioneArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Descrizione:",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._descrizioneArticoloCheck, 0, wx.ALL, 5)

        self._descrizioneArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self._descrizioneArticoloText.Enable(False)

        gSizer61.Add(self._descrizioneArticoloText, 0, wx.ALL, 5)

        self.m_staticText251 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText251.Wrap(-1)
        gSizer61.Add(self.m_staticText251, 0, wx.ALL, 5)

        self.m_staticText26 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        gSizer61.Add(self.m_staticText26, 0, wx.ALL, 5)

        self._daPesoArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"(Da) Peso: ",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._daPesoArticoloCheck, 0, wx.ALL, 5)

        self._daPesoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self._daPesoArticoloText.Enable(False)

        gSizer61.Add(self._daPesoArticoloText, 0, wx.ALL, 5)

        self._aPesoArticoloText = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"a Peso: ",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self._aPesoArticoloText.Enable(False)

        gSizer61.Add(self._aPesoArticoloText, 0, wx.ALL, 5)

        self._aPesoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self._aPesoArticoloText.Enable(False)

        gSizer61.Add(self._aPesoArticoloText, 0, wx.ALL, 5)

        self._rapportoArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Rapporto:",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._rapportoArticoloCheck, 0, wx.ALL, 5)

        self._rapportoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self._rapportoArticoloText.Enable(False)

        gSizer61.Add(self._rapportoArticoloText, 0, wx.ALL, 5)

        self.m_staticText27 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        gSizer61.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.m_staticText28 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)
        gSizer61.Add(self.m_staticText28, 0, wx.ALL, 5)

        self._insertoArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Inserto",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._insertoArticoloCheck, 0, wx.ALL, 5)

        self._insertoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self._insertoArticoloText.Enable(False)

        gSizer61.Add(self._insertoArticoloText, 0, wx.ALL, 5)

        self.m_staticText30 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        gSizer61.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.m_staticText31 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer61.Add(self.m_staticText31, 0, wx.ALL, 5)

        self._quantitaArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Quantita'",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._quantitaArticoloCheck, 0, wx.ALL, 5)

        self._quantitaArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        self._quantitaArticoloText.Enable(False)

        gSizer61.Add(self._quantitaArticoloText, 0, wx.ALL, 5)

        self.m_staticText34 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText34.Wrap(-1)
        gSizer61.Add(self.m_staticText34, 0, wx.ALL, 5)

        self.m_staticText35 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText35.Wrap(-1)
        gSizer61.Add(self.m_staticText35, 0, wx.ALL, 5)

        self._coloreArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Colore",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._coloreArticoloCheck, 0, wx.ALL, 5)

        self._coloreArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self._coloreArticoloText.Enable(False)

        gSizer61.Add(self._coloreArticoloText, 0, wx.ALL, 5)

        self.m_staticText36 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText36.Wrap(-1)
        gSizer61.Add(self.m_staticText36, 0, wx.ALL, 5)

        self.m_staticText37 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText37.Wrap(-1)
        gSizer61.Add(self.m_staticText37, 0, wx.ALL, 5)

        self._daPercentualeArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY,
                                                       u"(Da) Percentuale:", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._daPercentualeArticoloCheck, 0, wx.ALL, 5)

        self._daPercentualeArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self._daPercentualeArticoloText.Enable(False)

        gSizer61.Add(self._daPercentualeArticoloText, 0, wx.ALL, 5)

        self._aPercentualeArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"a Percentuale: ",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self._aPercentualeArticoloCheck.Enable(False)

        gSizer61.Add(self._aPercentualeArticoloCheck, 0, wx.ALL, 5)

        self._aPercentualeArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self._aPercentualeArticoloText.Enable(False)

        gSizer61.Add(self._aPercentualeArticoloText, 0, wx.ALL, 5)

        self._anticipoColoreArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY,
                                                        u"Anticipo colore:", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._anticipoColoreArticoloCheck, 0, wx.ALL, 5)

        self._anticipoColoreArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self._anticipoColoreArticoloText.Enable(False)

        gSizer61.Add(self._anticipoColoreArticoloText, 0, wx.ALL, 5)

        self.m_staticText38 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)
        gSizer61.Add(self.m_staticText38, 0, wx.ALL, 5)

        self.m_staticText39 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)
        gSizer61.Add(self.m_staticText39, 0, wx.ALL, 5)

        self._programmaC12ArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Programma C12: ",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._programmaC12ArticoloCheck, 0, wx.ALL, 5)

        self._programmaC12ArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self._programmaC12ArticoloText.Enable(False)

        gSizer61.Add(self._programmaC12ArticoloText, 0, wx.ALL, 5)

        self.m_staticText40 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText40.Wrap(-1)
        gSizer61.Add(self.m_staticText40, 0, wx.ALL, 5)

        self.m_staticText41 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText41.Wrap(-1)
        gSizer61.Add(self.m_staticText41, 0, wx.ALL, 5)

        self._programmaC25ArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Programma C25:",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._programmaC25ArticoloCheck, 0, wx.ALL, 5)

        self._programmaC25ArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self._programmaC25ArticoloText.Enable(False)

        gSizer61.Add(self._programmaC25ArticoloText, 0, wx.ALL, 5)

        self.m_staticText42 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText42.Wrap(-1)
        gSizer61.Add(self.m_staticText42, 0, wx.ALL, 5)

        self.m_staticText43 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        gSizer61.Add(self.m_staticText43, 0, wx.ALL, 5)

        self._programmaH120Check = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Programma H120:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._programmaH120Check, 0, wx.ALL, 5)

        self._programmaH120Text = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._programmaH120Text, 0, wx.ALL, 5)

        self.m_staticText44 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        gSizer61.Add(self.m_staticText44, 0, wx.ALL, 5)

        self.m_staticText45 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText45.Wrap(-1)
        gSizer61.Add(self.m_staticText45, 0, wx.ALL, 5)

        self._daDataArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"(Da) Data: ",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._daDataArticoloCheck, 0, wx.ALL, 5)

        self._daDataArticoloDate = wx.adv.DatePickerCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.DefaultDateTime,
                                                     wx.DefaultPosition, wx.DefaultSize)
        self._daDataArticoloDate.Enable(False)

        gSizer61.Add(self._daDataArticoloDate, 0, wx.ALL, 5)

        self._aDataArticoloCheck = wx.CheckBox(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"a Data:",
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        self._aDataArticoloCheck.Enable(False)

        gSizer61.Add(self._aDataArticoloCheck, 0, wx.ALL, 5)

        self._aDataArticoloDate = wx.adv.DatePickerCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.DefaultDateTime,
                                                    wx.DefaultPosition, wx.DefaultSize)
        self._aDataArticoloDate.Enable(False)

        gSizer61.Add(self._aDataArticoloDate, 0, wx.ALL, 5)

        self.m_staticText46 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText46.Wrap(-1)
        gSizer61.Add(self.m_staticText46, 0, wx.ALL, 5)

        self.m_staticText47 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText47.Wrap(-1)
        gSizer61.Add(self.m_staticText47, 0, wx.ALL, 5)

        self.m_staticText48 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText48.Wrap(-1)
        gSizer61.Add(self.m_staticText48, 0, wx.ALL, 5)

        self._cercaArticoloButton = wx.Button(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Esegui",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._cercaArticoloButton, 0, wx.ALL, 5)

        self.m_staticText49 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Nome comando:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText49.Wrap(-1)
        gSizer61.Add(self.m_staticText49, 0, wx.ALL, 5)

        self._nomeComandoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._nomeComandoArticoloText, 0, wx.ALL, 5)

        self.m_staticText51 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Descrizione:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)
        gSizer61.Add(self.m_staticText51, 0, wx.ALL, 5)

        self._descrizioneComandoArticoloText = wx.TextCtrl(self._ricercaProfondaArticoloPanel, wx.ID_ANY,
                                                           wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._descrizioneComandoArticoloText, 0, wx.ALL, 5)

        self.m_staticText52 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)
        gSizer61.Add(self.m_staticText52, 0, wx.ALL, 5)

        self.m_staticText54 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText54.Wrap(-1)
        gSizer61.Add(self.m_staticText54, 0, wx.ALL, 5)

        self.m_staticText55 = wx.StaticText(self._ricercaProfondaArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText55.Wrap(-1)
        gSizer61.Add(self.m_staticText55, 0, wx.ALL, 5)

        self._salvaComandoArticoloButton = wx.Button(self._ricercaProfondaArticoloPanel, wx.ID_ANY, u"Salva Comando",
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer61.Add(self._salvaComandoArticoloButton, 0, wx.ALL, 5)

        self._ricercaProfondaArticoloPanel.SetSizer(gSizer61)
        self._ricercaProfondaArticoloPanel.Layout()
        gSizer61.Fit(self._ricercaProfondaArticoloPanel)
        self._visualizzaArticoliBook.AddPage(self._ricercaProfondaArticoloPanel, u"a page", False, wx.NullBitmap)
        self._ricercheArticoloSalvatePanel = wx.Panel(self._visualizzaArticoliBook, wx.ID_ANY, wx.DefaultPosition,
                                                      wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer7 = wx.GridSizer(2, 2, 0, 0)

        _ricercheArticoloSalvateListChoices = []
        self._ricercheArticoloSalvateList = wx.ListBox(self._ricercheArticoloSalvatePanel, wx.ID_ANY,
                                                       wx.DefaultPosition, wx.DefaultSize,
                                                       _ricercheArticoloSalvateListChoices, 0)
        gSizer7.Add(self._ricercheArticoloSalvateList, 0, wx.ALL, 5)

        self.m_staticText56 = wx.StaticText(self._ricercheArticoloSalvatePanel, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText56.Wrap(-1)
        gSizer7.Add(self.m_staticText56, 0, wx.ALL, 5)

        self._ricercheArticoloSalvateEseguiButton = wx.Button(self._ricercheArticoloSalvatePanel, wx.ID_ANY, u"Esegui",
                                                              wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self._ricercheArticoloSalvateEseguiButton, 0, wx.ALL, 5)

        self._ricercheArticoloSalvateCancellaButton = wx.Button(self._ricercheArticoloSalvatePanel, wx.ID_ANY,
                                                                u"Cancella", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer7.Add(self._ricercheArticoloSalvateCancellaButton, 0, wx.ALL, 5)

        self._ricercheArticoloSalvatePanel.SetSizer(gSizer7)
        self._ricercheArticoloSalvatePanel.Layout()
        gSizer7.Fit(self._ricercheArticoloSalvatePanel)
        self._visualizzaArticoliBook.AddPage(self._ricercheArticoloSalvatePanel, u"a page", True, wx.NullBitmap)

        self._aggiungiArticoloBook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_mgr.AddPane(self._aggiungiArticoloBook,
                           wx.aui.AuiPaneInfo().Left().PinButton(True).Dock().Resizable().FloatingSize(wx.DefaultSize))

        self._aggiungiArticoloPanel = wx.Panel(self._aggiungiArticoloBook, wx.ID_ANY, wx.DefaultPosition,
                                               wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer8 = wx.GridSizer(15, 2, 0, 0)

        self.m_staticText12 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Codice:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        gSizer8.Add(self.m_staticText12, 0, wx.ALL, 5)

        self._aggiungiArticoloCodiceText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiArticoloCodiceText, 0, wx.ALL, 5)

        self.m_staticText13 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Descrizione:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        gSizer8.Add(self.m_staticText13, 0, wx.ALL, 5)

        self._aggiungiDescrizioneArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                            wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiDescrizioneArticoloText, 0, wx.ALL, 5)

        self.m_staticText14 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Peso:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        gSizer8.Add(self.m_staticText14, 0, wx.ALL, 5)

        self._aggiungiPesoArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                     wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiPesoArticoloText, 0, wx.ALL, 5)

        self.m_staticText15 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Rapporto:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText15.Wrap(-1)
        gSizer8.Add(self.m_staticText15, 0, wx.ALL, 5)

        self._aggiungiRapportoArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiRapportoArticoloText, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Inserto:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        gSizer8.Add(self.m_staticText16, 0, wx.ALL, 5)

        self._aggiungiInsertoArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiInsertoArticoloText, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Quantita':", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        gSizer8.Add(self.m_staticText17, 0, wx.ALL, 5)

        self._aggiungiQuantitaArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                         wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiQuantitaArticoloText, 0, wx.ALL, 5)

        self.m_staticText18 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Colore:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        gSizer8.Add(self.m_staticText18, 0, wx.ALL, 5)

        self._aggiungiColoreArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiColoreArticoloText, 0, wx.ALL, 5)

        self.m_staticText19 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"% Colore:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText19.Wrap(-1)
        gSizer8.Add(self.m_staticText19, 0, wx.ALL, 5)

        self._aggiungiPercentualeColoreArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY,
                                                                  wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiPercentualeColoreArticoloText, 0, wx.ALL, 5)

        self.m_staticText20 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Anticipo colore:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        gSizer8.Add(self.m_staticText20, 0, wx.ALL, 5)

        self._aggiungiAnticipoColoreText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiAnticipoColoreText, 0, wx.ALL, 5)

        self.m_staticText21 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Programma C12:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        gSizer8.Add(self.m_staticText21, 0, wx.ALL, 5)

        self._aggiungiProgrammaC12ArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                             wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiProgrammaC12ArticoloText, 0, wx.ALL, 5)

        self.m_staticText22 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Programma C25:",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        gSizer8.Add(self.m_staticText22, 0, wx.ALL, 5)

        self._aggiungiProgrammaC25ArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                             wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiProgrammaC25ArticoloText, 0, wx.ALL, 5)

        self.m_staticText23 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Data:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText23.Wrap(-1)
        gSizer8.Add(self.m_staticText23, 0, wx.ALL, 5)

        self._aggiungiDataArticoloDate = wx.adv.DatePickerCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.DefaultDateTime,
                                                           wx.DefaultPosition, wx.DefaultSize)
        gSizer8.Add(self._aggiungiDataArticoloDate, 0, wx.ALL, 5)

        self.m_staticText24 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, u"Ora:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText24.Wrap(-1)
        gSizer8.Add(self.m_staticText24, 0, wx.ALL, 5)

        self._aggiungiOraArticoloText = wx.TextCtrl(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString,
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiOraArticoloText, 0, wx.ALL, 5)

        self.m_staticText25 = wx.StaticText(self._aggiungiArticoloPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText25.Wrap(-1)
        gSizer8.Add(self.m_staticText25, 0, wx.ALL, 5)

        self._aggiungiArticoloButton = wx.Button(self._aggiungiArticoloPanel, wx.ID_ANY, u"aggiungi",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer8.Add(self._aggiungiArticoloButton, 0, wx.ALL, 5)

        self._aggiungiArticoloPanel.SetSizer(gSizer8)
        self._aggiungiArticoloPanel.Layout()
        gSizer8.Fit(self._aggiungiArticoloPanel)
        self._aggiungiArticoloBook.AddPage(self._aggiungiArticoloPanel, u"a page", False)

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

    def __del__(self):
        self.m_mgr.UnInit()

    def m_splitter5OnIdle(self, event):
        self.m_splitter5.SetSashPosition(0)
        self.m_splitter5.Unbind(wx.EVT_IDLE)


