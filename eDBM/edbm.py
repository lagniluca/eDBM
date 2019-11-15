#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Main class of the application (the one used for starting the application)
"""

import sys
import os
import traceback

import wx

from eDBM.src.controller.files.edbm_threaded_file_reader import eDBMThreadedFileReader
from eDBM.src.view.edbm_window import eDBMWindow
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog

#costanti
INPUT_FILE_PATH = "sottoscorte_file_path.txt"
OUTPUT_FILE_DATA_PATH = "sottoscorte_nuovi_dati.txt"
OUTPUT_FILE_INDEX_PATH = "sottoscorte_ultima_posizione.txt"

sottoscorte_thread = eDBMThreadedFileReader(INPUT_FILE_PATH, OUTPUT_FILE_DATA_PATH, OUTPUT_FILE_INDEX_PATH, 60*5,
                                                    None)

def main():
    app = wx.App()
    window = None
    try:
        #print(os.listdir())
        window = eDBMWindow(None, INPUT_FILE_PATH)
        window.Show(True)
        sottoscorte_thread = eDBMThreadedFileReader(INPUT_FILE_PATH, OUTPUT_FILE_DATA_PATH, OUTPUT_FILE_INDEX_PATH, 60*5,
                                                    window)
        sottoscorte_thread.start()

    except Exception as e:
        track = traceback.format_exc()
        eDBMMessageDialog('eDBM - Errore:', track, True).start()

    window.Bind(wx.EVT_CLOSE, OnExitApp)
    app.MainLoop()

def OnExitApp(self):
    sottoscorte_thread.stop_reading()
    self.Destroy()

if __name__ == '__main__':
    main()
    sys.exit()
