# -*- coding: utf-8 -*-

from threading import Thread

from eDBM.src.view.pages.components.edbm_sottoscorte_dialog import eDBMSottoscorteDialog


class eDBMThreadedSottoscorteDialog(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        dia = eDBMSottoscorteDialog(None)
        dia.Show(True)