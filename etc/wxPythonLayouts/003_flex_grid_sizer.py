# -*- coding: utf-8 -*-

import wx
import wx.adv

class FlexGridSizerExample(wx.Frame):

    def __init__(self, parent):
        super(FlexGridSizerExample, self).__init__(parent, title='FlexGridSizer example')

        self._InitUI()
        self.Center()

    def _InitUI(self):
        panel = wx.Panel(self)

        # Layouts
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs  = wx.FlexGridSizer(4, 2, 9, 25)

        title = wx.StaticText(panel, label='Row 1')
        author = wx.StaticText(panel, label='Row 2')
        review = wx.StaticText(panel, label='Row 3')
        note = wx.StaticText(panel, label='Row 4')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE) # TextArea
        tc4 = wx.adv.TimePickerCtrl(panel, wx.ID_ANY)

        # Adding components to the frame
        fgs.AddMany([(title), (tc1, 1, wx.EXPAND),
                     (author), (tc2, 1, wx.EXPAND),
                     (review, 1, wx.EXPAND),
                     (tc3, 1, wx.EXPAND),
                     (note), (tc4, 1, wx.EXPAND)])

        """
        Making third row and second column growable
        """
        fgs.AddGrowableRow(2, 1) # la 3° riga può cambiare dimensione
        fgs.AddGrowableCol(1, 1) # la seconda colonna può cambiare dimensione

        hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=15)
        panel.SetSizer(hbox)

def main():

    app = wx.App()
    ex = FlexGridSizerExample(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
