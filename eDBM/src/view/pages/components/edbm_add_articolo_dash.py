# -*- coding: utf-8 -*-

"""
Classe che contiene il codice per la pagine riguardante l'aggiunta di un articolo
"""

# Librerie wx
import traceback

import wx
import wx.adv
import wx.lib.scrolledpanel

from eDBM.src.model.edbm_articolo import eDBMArticolo
from eDBM.src.model.exceptions.edbm_exception import eDBMException
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog


class eDBMAddArticoloDash(wx.lib.scrolledpanel.ScrolledPanel):
    def __init__(self, parent):
        super(eDBMAddArticoloDash, self).__init__(parent, style=wx.SIMPLE_BORDER)

        self.SetupScrolling()
        self._InitUI()

    def _InitUI(self):
        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(15, 2, 9, 25)

        # codice
        codice = wx.StaticText(self, label='codice:')
        self._aggiungiCodiceArticoloText = wx.TextCtrl(self)

        # descrizione
        descrizione = wx.StaticText(self, label='descrizione:')
        self._aggiungiDescrizioneArticoloText = wx.TextCtrl(self)

        # peso
        peso = wx.StaticText(self, label='peso:')
        self._aggiungiPesoArticoloText = wx.SpinCtrl(self)

        # rapporto
        rapporto = wx.StaticText(self, label='rapporto:')
        self._aggiungiRapportoArticoloText = wx.SpinCtrl(self)

        # inserto
        inserto = wx.StaticText(self, label='inserto:')
        self._aggiungiInsertoArticoloText = wx.TextCtrl(self)

        # quantità
        quantita = wx.StaticText(self, label="quantita':'")
        self._aggiungiQuantitaArticoloText = wx.SpinCtrl(self)

        # colore
        colore = wx.StaticText(self, label='colore:')
        self._aggiungiColoreArticoloText = wx.TextCtrl(self)

        # colore
        percentuale = wx.StaticText(self, label='percentuale colore:')
        self._aggiungiPercentualeColoreArticoloText = wx.TextCtrl(self)

        # anticipo colore
        anticipo = wx.StaticText(self, label="anticipo colore:'")
        self._aggiungiAnticipoColoreArticoloText = wx.SpinCtrl(self)

        # programma C12
        programma_c12 = wx.StaticText(self, label='programma C12:')
        self._aggiungiProgrammaC12ArticoloText = wx.TextCtrl(self)

        # programma C25
        programma_c25 = wx.StaticText(self, label='programma C25:')
        self._aggiungiProgrammaC25ArticoloText = wx.TextCtrl(self)

        # programma HP12
        programma_hp12 = wx.StaticText(self, label='programma HP12:')
        self._aggiungiProgrammaHP12ArticoloText = wx.TextCtrl(self)

        # data
        data = wx.StaticText(self, label='data:')
        self._aggiungiDataArticoloPicker = wx.adv.DatePickerCtrl(self, wx.ID_ANY, wx.DefaultDateTime)

        # ora
        ora = wx.StaticText(self, label='ora:')
        self._aggiungiOraArticoloPicker = wx.adv.TimePickerCtrl(self, wx.ID_ANY)

        #padding
        pad1 = wx.StaticText(self, label='')

        # bottone aggiungi
        self._aggiungiArticoloBtn = wx.Button(self, wx.ID_ANY, u"aggiungi")

        fgs.AddMany([
            (codice), (self._aggiungiCodiceArticoloText, wx.ID_ANY, wx.EXPAND),
            (descrizione), (self._aggiungiDescrizioneArticoloText, wx.ID_ANY, wx.EXPAND),
            (peso), (self._aggiungiPesoArticoloText, wx.ID_ANY, wx.EXPAND),
            (rapporto), (self._aggiungiRapportoArticoloText, wx.ID_ANY, wx.EXPAND),
            (inserto), (self._aggiungiInsertoArticoloText, wx.ID_ANY, wx.EXPAND),
            (quantita), (self._aggiungiQuantitaArticoloText, wx.ID_ANY, wx.EXPAND),
            (colore), (self._aggiungiColoreArticoloText, wx.ID_ANY, wx.EXPAND),
            (percentuale), (self._aggiungiPercentualeColoreArticoloText, wx.ID_ANY, wx.EXPAND),
            (anticipo), (self._aggiungiAnticipoColoreArticoloText, wx.ID_ANY, wx.EXPAND),
            (programma_c12), (self._aggiungiProgrammaC12ArticoloText, wx.ID_ANY, wx.EXPAND),
            (programma_c25), (self._aggiungiProgrammaC25ArticoloText, wx.ID_ANY, wx.EXPAND),
            (programma_hp12), (self._aggiungiProgrammaHP12ArticoloText, wx.ID_ANY, wx.EXPAND),
            (data), (self._aggiungiDataArticoloPicker, wx.ID_ANY, wx.EXPAND),
            (ora), (self._aggiungiOraArticoloPicker, wx.ID_ANY, wx.EXPAND),
            (pad1), (self._aggiungiArticoloBtn, wx.ID_ANY, wx.ALIGN_RIGHT)
        ])

        # resizable columns
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizerAndFit(hbox)
        hbox.Fit(self)
        fgs.Fit(self)

    def _OnClick(self, evt):
        try :

            # lettura dei dati inseriti dall'utente
            codice = self._aggiungiCodiceArticoloText.GetValue()
            descrizione = self._aggiungiDescrizioneArticoloText.GetValue()
            peso = int(self._aggiungiPesoArticoloText.GetValue())
            rapporto = int(self._aggiungiRapportoArticoloText.GetValue())
            inserto = self._aggiungiInsertoArticoloText.GetValue()
            quantita_str = self._aggiungiQuantitaArticoloText.GetValue()
            if quantita_str is not None:
                if quantita_str.isdigit():
                    quantita = int(quantita_str)
            colore = self._aggiungiColoreArticoloText.GetValue()
            percentuale_colore = int(self._aggiungiPercentualeColoreArticoloText.GetValue())
            anticipo_colore = int(self._aggiungiAnticipoColoreArticoloText.GetValue())
            programma_c12 = int(self._aggiungiProgrammaC12ArticoloText.GetValue())
            programma_c25 = int(self._aggiungiProgrammaC25ArticoloText.GetValue())
            programma_hp12 = int(self._aggiungiProgrammaHP12ArticoloText.GetValue())
            data = self._aggiungiDataArticoloPicker.GetValue()
            ora = self._aggiungiOraArticoloPicker.GetValue()

            # creazione dell'oggetto
            articolo = eDBMArticolo()

            articolo.setCodice(codice)
            if descrizione is not None:
                articolo.setDescrizione(descrizione)
            articolo.setPeso(peso)
            articolo.setRapporto(rapporto)
            articolo.setInserto(inserto)
            if quantita_str is not None:
                articolo.setQuantita(quantita)
            articolo.setColore(colore)
            articolo.setPercentualeColore(percentuale_colore)
            articolo.setAnticipoColore(anticipo_colore)
            articolo.setProgrammaC12(programma_c12)
            articolo.setProgrammaC25(programma_c25)
            articolo.setProgrammaHP12(programma_hp12)
            articolo.setData(data)
            articolo.setOra(ora)

            # creazione della query

        except eDBMException as e:
            eDBMMessageDialog("Errore aggiunta articolo", e, True)

        except Exception as ex:
            track = traceback.format_exc()
            eDBMMessageDialog("Errore aggiunta articolo", track, True)



