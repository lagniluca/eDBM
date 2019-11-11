#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import traceback

import wx

from eDBM.src.model.exceptions.edbm_exception import eDBMException
from eDBM.src.view.edbm_window import eDBMWindow
from eDBM.src.view.pages.components.edbm_message_dialog import eDBMMessageDialog


def main():
    app = wx.App()
    try:

        window = eDBMWindow(None)
        window.Show(True)
    except Exception as e:
        track = traceback.format_exc()
        eDBMMessageDialog('eDBM - Errore:', track, True).start()

    app.Bind(wx.EVT_CLOSE, OnExitApp)
    app.MainLoop()

def OnExitApp(self, event):
    self.Destroy()


if __name__ == '__main__':
    main()
    sys.exit()
