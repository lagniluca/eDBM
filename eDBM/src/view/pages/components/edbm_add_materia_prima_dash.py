# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la pagine riguardante l'aggiunta di una materia prima
"""

# Librerie wx
import traceback

import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.controller.exceptions.edbm_exception import eDBMException
from eDBM.src.controller.files.edbm_lotto_generator import eDBMLottoGenerator
from eDBM.src.model.edbm_materia_prima import eDBMMateriaPrima
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog


class eDBMAddMateriaPrimaDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent, window, dbm):
        super(eDBMAddMateriaPrimaDash, self).__init__(parent, style=wx.SIMPLE_BORDER)

        self._dbm = dbm

        self.__window = window

        self.SetupScrolling()
        self._InitUI()

    def _InitUI(self):
        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(9, 2, 9, 25)

        # codice
        codice = wx.StaticText(self, label='(*)codice:')
        self._aggiungiCodiceMPText = wx.TextCtrl(self)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._aggiungiDescrizioneMPText = wx.TextCtrl(self)

        # lotto
        lotto = wx.StaticText(self, label='(*)lotto:')
        self._aggiungiLottoMPText = wx.TextCtrl(self)
        self.__lotto_g = eDBMLottoGenerator()
        lotto_str = self.__lotto_g.get_lotto()
        self._aggiungiLottoMPText.SetValue(lotto_str)


        # registrazione
        registrazione = wx.StaticText(self, label='registrazione:')
        self._aggiungiRegistrazioneMPText = wx.TextCtrl(self)

        # tipo
        tipo = wx.StaticText(self, label='(*)tipo:')
        opzioni = ['componente', 'inserto']
        self._aggiungiTipoMPCombo = wx.ComboBox(self, choices=opzioni, style=wx.CB_READONLY)
        self._aggiungiTipoMPCombo.SetValue(opzioni[0])
        # data
        data = wx.StaticText(self, label='(*)data:')
        self._aggiungiDataMPPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)

        # ora
        ora = wx.StaticText(self, label='(*)ora:')
        self._aggiungiOraMPPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        # ddt
        ddt = wx.StaticText(self, label='DDT:')
        self._aggiungiDDTMPText = wx.TextCtrl(self)

        # data ddt
        data_ddt = wx.StaticText(self, label='(*)data DDT:')
        data_ddt.Show(False)
        self._aggiungiDataDDTMPPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY)
        self._aggiungiDataDDTMPPicker.Show(False)

        #padding
        pad1 = wx.StaticText(self, label='(*) = campi che richiedono obbligatoriamente un valore')

        # bottone aggiungi
        self._aggiungiMPBtn = wx.Button(self, wx.ID_ANY, u"Aggiungi")

        self._aggiungiMPBtn.Bind(wx.EVT_BUTTON, self._OnClick)

        fgs.AddMany([
            (codice), (self._aggiungiCodiceMPText, wx.ID_ANY, wx.EXPAND),
            (descrizione), (self._aggiungiDescrizioneMPText, wx.ID_ANY, wx.EXPAND),
            (lotto), (self._aggiungiLottoMPText, wx.ID_ANY, wx.EXPAND),
            (registrazione), (self._aggiungiRegistrazioneMPText, wx.ID_ANY, wx.EXPAND),
            (tipo), (self._aggiungiTipoMPCombo, wx.ID_ANY, wx.EXPAND),
            (data), (self._aggiungiDataMPPicker, wx.ID_ANY, wx.EXPAND),
            (ora), (self._aggiungiOraMPPicker, wx.ID_ANY, wx.EXPAND),
            (ddt), (self._aggiungiDDTMPText, wx.ID_ANY, wx.EXPAND),
            #(data_ddt), (self._aggiungiDataDDTMPPicker, wx.ID_ANY, wx.EXPAND),
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
            codice = self._aggiungiCodiceMPText.GetValue()
            descrizione = self._aggiungiDescrizioneMPText.GetValue()
            lotto = self._aggiungiLottoMPText.GetValue()
            registrazione = self._aggiungiRegistrazioneMPText.GetValue()
            opzione = self._aggiungiTipoMPCombo.GetValue()
            if opzione == 'componente':
                tipo = 1
            else:
                tipo = 2
            data_dt = self._aggiungiDataMPPicker.GetValue()
            data = data_dt.Format("%d/%m/%Y")
            ora_dt = self._aggiungiOraMPPicker.GetValue()
            ora = ora_dt.Format("%H:%M:%S")
            ddt = self._aggiungiDDTMPText.GetValue()
            data_ddt_dt = self._aggiungiDataDDTMPPicker.GetValue()
            data_ddt = data_ddt_dt.Format("%H:%M:%S")

            # creazione dell'oggetto
            materia_prima = eDBMMateriaPrima()
            materia_prima.setCodice(codice)
            if descrizione is not None :
                materia_prima.setDescrizione(descrizione)
            materia_prima.setLotto(lotto)
            materia_prima.setRegistrazione(registrazione)
            materia_prima.setTipo(tipo)
            materia_prima.setData(data)
            materia_prima.setOra(ora)
            if ddt is not None :
                materia_prima.setDDT(ddt)
            materia_prima.setDataDDT(data_ddt)

            # inserimento nel database
            query = materia_prima.generaAggiungiMateriaPrimaQuery()
            cursor = self._dbm.connessione().cursor()
            cursor.execute(query)
            self._dbm.connessione().commit()
            cursor.commit()

            self.__lotto_g.update_index()
            self.__window.aggiornaAggiungiMateriePrime()

            eDBMMessageDialog("Aggiunta materia prima", "Materia prima aggiunta con successo", False).start()

        except eDBMException as e:
            eDBMMessageDialog("Errore aggiunta materia prima", e.getMessage(), True).start()
        except Exception as ex:
            track = traceback.format_exc()
            eDBMMessageDialog("Errore aggiunta materia prima", track, True).start()



