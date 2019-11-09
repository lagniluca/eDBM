# -*- coding: utf-8 -*-

"""
Class used for creating a grid component
"""

# wx Libraries
import wx
import wx.grid


class GridPanel(wx.Panel):
    def __init__(self, parent):
        super(GridPanel, self).__init__(parent)
        self._InitUI()

    # Method used for defying the UI of the panel
    def _InitUI(self):
        # Grid component
        self._grid = wx.grid.Grid(self)
        self._grid.CreateGrid(10, 10)

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
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._grid, wx.ID_ANY, wx.EXPAND)

        self.SetSizer(sizer)
