# -*- coding: utf-8 -*-

"""
Class used for creating a grid component
"""

# wx Libraries
import wx
import wx.grid

#Access libraries
import pyodbc

class eDBMGridPanel(wx.Panel):
    def __init__(self, parent):
        super(eDBMGridPanel, self).__init__(parent, style=wx.BORDER_RAISED)
        self._InitUI()

    # Method used for defying the UI of the panel
    def _InitUI(self):
        # Grid component
        self._grid = wx.grid.Grid(self)
        self._grid.CreateGrid(20, 20)

        btn = wx.Button(self, wx.ID_ANY, u'elimina')

        # Example of column header setting
        # self._grid.SetColLablValue(0, "ID")
        # self._grid.SetColLablValue(1, "Codice")

        # Example of setting the value of a cell
        # self._grid.SetCellValue(0, 0, "cell 0")
        # self._grid.SetCellBackgroundColour(0, 0, wx.RED)
        # self._grid.SetCellTextColour(0, 0, wx.WHITE)
        # self._grid.SetReadOnly(0, 0, True)

        # Example of custom type grid cell
        # self._grid.SetCellEditor(1, 1, wx.grid.GridCellNumberEditor(1, 20))

        # Placement of the grid component inside the panel
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(1, 2, 9, 25)

        fgs.AddMany([
            (btn, wx.ID_ANY, wx.ALIGN_RIGHT),
            (self._grid, 1, wx.EXPAND)
        ])

        fgs.AddGrowableCol(1, 1)

        sizer.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.SetSizer(sizer)
        sizer.Fit(self)

