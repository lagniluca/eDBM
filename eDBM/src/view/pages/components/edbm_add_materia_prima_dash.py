# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la pagine riguardante l'aggiunta di una materia prima
"""

# Librerie wx
import traceback

import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.model.edbm_materia_prima import eDBMMateriaPrima
from eDBM.src.model.exceptions.edbm_exception import eDBMException
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog


class eDBMAddMateriaPrimaDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, dbm):
        super(eDBMAddMateriaPrimaDash, self).__init__(parent, style=wx.SIMPLE_BORDER)

        self._dbm = dbm

        self.SetupScrolling()
        self._InitUI()

    def _InitUI(self):
        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(10, 2, 9, 25)

        # codice
        codice = wx.StaticText(self, label='codice:')
        self._aggiungiCodiceMPText = wx.TextCtrl(self)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._aggiungiDescrizioneMPText = wx.TextCtrl(self)

        # lotto
        lotto = wx.StaticText(self, label='lotto:')
        self._aggiungiLottoMPText = wx.TextCtrl(self)

        # registrazione
        registrazione = wx.StaticText(self, label='registrazione:')
        self._aggiungiRegistrazioneMPText = wx.TextCtrl(self)

        # tipo
        tipo = wx.StaticText(self, label='inserto:')
        self._aggiungiTipoMPSpin = wx.SpinCtrl(self)

        # data
        data = wx.StaticText(self, label='data:')
        self._aggiungiDataMPPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)

        # ora
        ora = wx.StaticText(self, label='ora:')
        self._aggiungiOraMPPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        # ddt
        ddt = wx.StaticText(self, label='DDT:')
        self._aggiungiDDTMPText = wx.TextCtrl(self)

        # data ddt
        data_ddt = wx.StaticText(self, label='data DDT:')
        self._aggiungiDataDDTMPPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        #padding
        pad1 = wx.StaticText(self, label='')

        # bottone aggiungi
        self._aggiungiMPBtn = wx.Button(self, wx.ID_ANY, u"aggiungi")

        self._aggiungiMPBtn.Bind(wx.EVT_BUTTON, self._OnClick)

        fgs.AddMany([
            (codice), (self._aggiungiCodiceMPText, wx.ID_ANY, wx.EXPAND),
            (descrizione), (self._aggiungiDescrizioneMPText, wx.ID_ANY, wx.EXPAND),
            (lotto), (self._aggiungiLottoMPText, wx.ID_ANY, wx.EXPAND),
            (registrazione), (self._aggiungiRegistrazioneMPText, wx.ID_ANY, wx.EXPAND),
            (tipo), (self._aggiungiTipoMPSpin, wx.ID_ANY, wx.EXPAND),
            (data), (self._aggiungiDataMPPicker, wx.ID_ANY, wx.EXPAND),
            (ora), (self._aggiungiOraMPPicker, wx.ID_ANY, wx.EXPAND),
            (ddt), (self._aggiungiDDTMPText, wx.ID_ANY, wx.EXPAND),
            (data_ddt), (self._aggiungiDataDDTMPPicker, wx.ID_ANY, wx.EXPAND),
            (pad1), (self._aggiungiMPBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
        ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)

    def _OnClick(self, evt):
        try:
            # lettura dati inseriti dall'utente
            print("1 ")
            codice = self._aggiungiCodiceMPText.GetValue()
            print("2 " + codice)
            descrizione = self._aggiungiDescrizioneMPText.GetValue()
            print("3 ")
            lotto = self._aggiungiLottoMPText.GetValue()
            print("4 ")
            registrazione = self._aggiungiRegistrazioneMPText.GetValue()
            print("5 ")
            tipo = int(self._aggiungiTipoMPSpin.GetValue())
            print("6 ")
            data_dt = self._aggiungiDataMPPicker.GetValue()
            data = data_dt.Format("%d/%m/%Y")
            print("7 " + data)
            ora_dt = self._aggiungiOraMPPicker.GetValue()
            ora = ora_dt.Format("%H:%M:%S")
            print("8 " + ora)
            ddt = self._aggiungiDDTMPText.GetValue()
            print("9 ")
            data_ddt_dt = self._aggiungiDataDDTMPPicker.GetValue()
            data_ddt = data_ddt_dt.Format("%H:%M:%S")
            print("10 ")
            # creazione dell'oggetto
            materia_prima = eDBMMateriaPrima()
            print("11 ")
            materia_prima.setCodice(codice)
            print("12 ")
            if descrizione is not None :
                materia_prima.setDescrizione(descrizione)
            print("13 ")
            materia_prima.setLotto(lotto)
            print("14 ")
            materia_prima.setRegistrazione(registrazione)
            print("15 ")
            materia_prima.setTipo(tipo)
            print("16 ")
            materia_prima.setData(data)
            print("17 ")
            materia_prima.setOra(ora)
            print("18 ")
            if ddt is not None :
                materia_prima.setDDT(ddt)
            print("19 ")
            materia_prima.setDataDDT(data_ddt)

            # inserimento nel database
            query = materia_prima.generaAggiungiMateriaPrimaQuery()
            cursor = self._dbm.connessione().cursor()
            cursor.execute(query)
            self._dbm.connessione().commit()
            cursor.commit()

            eDBMMessageDialog("Aggiunta materia prima", "Materia prima aggiunta con successo", False).start()

        except eDBMException as e:
            eDBMMessageDialog("Errore aggiunta materia prima", e.getMessage(), True).start()
        except Exception as ex:
            track = traceback.format_exc()
            eDBMMessageDialog("Errore aggiunta materia prima", track, True).start()



