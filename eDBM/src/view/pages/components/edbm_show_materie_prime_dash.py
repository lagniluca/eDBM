"""
Classe contenente il cruscotto per il filtraggio degli articoli
"""

# librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.view.pages.components.edbm_suggestion_combo_box import eDBMSuggestionComboBox


class eDBMShowMateriePrimeDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, dbm, gridPanel):
        super(eDBMShowMateriePrimeDash, self).__init__(parent, style=wx.SUNKEN_BORDER)

        self.SetupScrolling()

        self._dbm = dbm
        self._gridPanel = gridPanel

        self.__InitUI()

    # setup interfaccia grafica del cruscotto articoli
    def __InitUI(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 4, 9, 25)

        # codice
        self._codiceMPCheck = wx.CheckBox(self, label='codice:')
        cursor = self._dbm.connessione().cursor()
        cursor.execute("SELECT DISTINCT Codice FROM materie_prime")
        codici = list()
        records = cursor.fetchall()
        for record in records:
            codici.append(str(record[0]))
        self._codiceMPCombo = eDBMSuggestionComboBox(self, "", choices=codici, style=wx.CB_SORT)
        self._codiceMPCombo.Enable(False)

        # descrizione
        self._descrizioneMPCheck = wx.CheckBox(self, label='descrizione:')
        cursor = self._dbm.connessione().cursor()
        cursor.execute("SELECT DISTINCT Descrizione FROM materie_prime")
        descrizioni = list()
        records = cursor.fetchall()
        for record in records:
            descrizioni.append(str(record[0]))
        self._descrizioneMPCombo = eDBMSuggestionComboBox(self, "", choices=descrizioni, style=wx.CB_SORT)
        self._descrizioneMPCombo.Enable(False)

        # data
        self._dataMPCheck = wx.CheckBox(self, label='data:')
        self._dataMPPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)
        self._dataMPPicker.Enable(False)

        # ora
        self._oraMPText = wx.StaticText(self, label='ultimo refresh:')
        self._oraMPPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)
        self._oraMPPicker.Enable(False)

        # padding
        pad1 = wx.StaticText(self, label='')
        pad2 = wx.StaticText(self, label='')
        pad3 = wx.StaticText(self, label='')

        # check box bind
        self._codiceMPCheck.Bind(wx.EVT_CHECKBOX, self._filtraCodiceMPChecked)
        self._descrizioneMPCheck.Bind(wx.EVT_CHECKBOX, self._filtraDescrizioneMPChecked)
        self._dataMPCheck.Bind(wx.EVT_CHECKBOX, self._filtraDataMPChecked)

        # filtra
        self._filtraMPBtn = wx.Button(self, label='Filtra')
        self._filtraMPBtn.Bind(wx.EVT_BUTTON, self._filtra)

        fgs.AddMany([(self._codiceMPCheck), (self._codiceMPCombo, 1, wx.EXPAND | wx.ALL),  # (pad1),
                     (self._descrizioneMPCheck), (self._descrizioneMPCombo, 1, wx.EXPAND | wx.ALL),  # (pad2),
                     (self._dataMPCheck), (self._dataMPPicker, 1, wx.EXPAND | wx.ALL),
                     (self._oraMPText), (self._oraMPPicker, 1, wx.EXPAND | wx.ALL),
                     (pad1), (pad2), (pad3), (self._filtraMPBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
                     ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)
        fgs.AddGrowableCol(3, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)

    def _filtraCodiceMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked :
            enabled = True

        self._codiceMPCombo.Enable(enabled)

    def _filtraDescrizioneMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._descrizioneMPCombo.Enable(enabled)

    def _filtraDataMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._dataMPPicker.Enable(enabled)

    def _filtra(self, evt):
        codice = None
        descrizione = None
        data = None

        if self._codiceMPCheck.IsChecked() :
            codice = str(self._codiceMPCombo.GetValue())

        if self._descrizioneMPCheck.IsChecked():
            descrizione = str(self._descrizioneMPCombo.GetValue())
            if descrizione is None:
                descrizione = ''

        if self._dataMPCheck.IsChecked():
            data_dt = self._dataMPPicker.GetValue()
            data = data_dt.Format("%d/%m/%Y")

        self._gridPanel.filtraRisultato(codice, descrizione, data)




