"""
Classe contenente il cruscotto per il filtraggio degli articoli
"""

# librerie wx
import wx
import wx.adv
import wx.lib.scrolledpanel

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
        self._codiceMPText = wx.TextCtrl(self)
        self._codiceMPText.Enable(False)

        # descrizione
        self._descrizioneMPCheck = wx.CheckBox(self, label='descrizione:')
        self._descrizioneMPText = wx.TextCtrl(self)
        self._descrizioneMPText.Enable(False)

        # data
        self._dataMPCheck = wx.CheckBox(self, label='data:')
        self._dataMPPicker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime)
        self._dataMPPicker.Enable(False)

        # ora
        self._oraMPCheck = wx.CheckBox(self, label='ora:')
        self._oraMPCheck.Enable(False)
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
        self._oraMPCheck.Bind(wx.EVT_CHECKBOX, self._filtraOraMPChecked)

        # filtra
        self._filtraMPBtn = wx.Button(self, label='filtra')
        #self._filtraMPBtn.Enable(False)
        self._filtraMPBtn.Bind(wx.EVT_BUTTON, self._filtra)

        fgs.AddMany([(self._codiceMPCheck), (self._codiceMPText, 1, wx.EXPAND | wx.ALL),  # (pad1),
                     (self._descrizioneMPCheck), (self._descrizioneMPText, 1, wx.EXPAND | wx.ALL),  # (pad2),
                     (self._dataMPCheck), (self._dataMPPicker, 1, wx.EXPAND | wx.ALL),
                     (self._oraMPCheck), (self._oraMPPicker, 1, wx.EXPAND | wx.ALL),
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

        self._codiceMPText.Enable(enabled)
        #self._abilitaFiltraBtn()

    def _filtraDescrizioneMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._descrizioneMPText.Enable(enabled)
        #self._abilitaFiltraBtn()

    def _filtraDataMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._dataMPPicker.Enable(enabled)
        #self._abilitaFiltraBtn()

    def _filtraOraMPChecked(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        enabled = False

        if isChecked:
            enabled = True

        self._oraMPPicker.Enable(enabled)
        #self._abilitaFiltraBtn()

    def _abilitaFiltraBtn(self):
        enable = False

        enable = enable or self._codiceMPCheck.IsChecked()
        enable = enable or self._descrizioneMPCheck.IsChecked()
        enable = enable or self._dataMPCheck.IsChecked()
        enable = enable or self._oraMPCheck.IsChecked()

        self._filtraMPBtn.Enable(enable)

    def _filtra(self, evt):
        codice = None
        descrizione = None
        data = None
        ora = None

        if self._codiceMPCheck.IsChecked() :
            codice = str(self._codiceMPText.GetValue())

        if self._descrizioneMPCheck.IsChecked():
            descrizione = str(self._descrizioneMPText.GetValue())
            if descrizione is None:
                descrizione = ''

        if self._dataMPCheck.IsChecked():
            data_dt = self._dataMPPicker.GetValue()
            data = data_dt.Format("%d/%m/%Y")

        if self._oraMPCheck.IsChecked():
            ora_dt = self._oraMPPicker.GetValue()
            ora = ora_dt.Format("%H:%M:%S")

        self._gridPanel.filtraRisultato(codice, descrizione, data, ora)




