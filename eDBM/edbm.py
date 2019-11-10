#!/usr/bin/python3
# -*- coding: utf-8 -*-

import wx

from eDBM.src.view.edbm_window import eDBMWindow


def main():
    app = wx.App()
    window = eDBMWindow(None)
    window.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
