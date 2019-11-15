"""
Classe contenente il cruscotto per il filtraggio della produizione
"""

# librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.view.pages.components.edbm_suggestion_combo_box import eDBMSuggestionComboBox


class eDBMProduzioneDashboard(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, dbm, gridPanel):
        super(eDBMProduzioneDashboard, self).__init__(parent, style=wx.SUNKEN_BORDER)

        self.SetupScrolling()

        self._dbm = dbm
        self._gridPanel = gridPanel

        self.__InitUI()

    # setup interfaccia grafica del cruscotto articoli
    def __InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 4, 9, 25)

        # codice
        self._articoloProduzioneCheck = wx.CheckBox(self, label='articolo:')
        cursor = self._dbm.connessione().cursor()
        cursor.execute("SELECT DISTINCT articolo FROM produzione_cosmec")
        articoli = list()
        records = cursor.fetchall()
        for record in records:
            articoli.append(str(record[0]))
        self._articoloProduzioneCombo = eDBMSuggestionComboBox(self, "", choices=articoli, style=wx.CB_SORT)
        self._articoloProduzioneCombo.Enable(False)

        # data
        self._dataProduzioneCheck = wx.CheckBox(self, label='data:')
        self._dataProduzionePicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)
        self._dataProduzionePicker.Enable(False)

        # ora
        self._oraProduzioneText = wx.StaticText(self, label='ultimo refresh: ')
        self._oraProduzionePicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)
        self._oraProduzionePicker.Enable(False)

        # padding
        pad1 = wx.StaticText(self, label='')
        pad2 = wx.StaticText(self, label='')

        # padding
        pad3 = wx.StaticText(self, label='')
        pad4 = wx.StaticText(self, label='')
        pad5 = wx.StaticText(self, label='')

        # check box bind
        self._articoloProduzioneCheck.Bind(wx.EVT_CHECKBOX, self._filtraArticoloProduzioneChecked)
        self._dataProduzioneCheck.Bind(wx.EVT_CHECKBOX, self._filtraDataProduzioneChecked)

        # filtra
        self._filtraMPBtn = wx.Button(self, label='Filtra')
        self._filtraMPBtn.Bind(wx.EVT_BUTTON, self._filtra)

        fgs.AddMany([(self._articoloProduzioneCheck), (self._articoloProduzioneCombo, wx.ID_ANY, wx.EXPAND | wx.ALL),
                     (self._dataProduzioneCheck), (self._dataProduzionePicker, wx.ID_ANY, wx.EXPAND | wx.ALL),
                     (self._oraProduzioneText), (self._oraProduzionePicker, wx.ID_ANY, wx.EXPAND | wx.ALL),
                     (pad1), (pad2, wx.ID_ANY, wx.EXPAND | wx.ALL),
                     (pad3), (pad4, wx.ID_ANY, wx.EXPAND | wx.ALL),
                     (pad5), (self._filtraMPBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
                     ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableCol(3, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)

    def _filtraArticoloProduzioneChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._articoloProduzioneCombo.Enable(enabled)

    def _filtraDataProduzioneChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._dataProduzionePicker.Enable(enabled)

    def _filtra(self, evt):
        articolo = None
        data = None

        if self._articoloProduzioneCheck.IsChecked():
            articolo = str(self._articoloProduzioneCombo.GetValue())

        if self._dataProduzioneCheck.IsChecked():
            data_dt = self._dataProduzionePicker.GetValue()
            data = data_dt.Format("%d/%m/%Y")

        self._gridPanel.filtraRisultato(articolo, data)
