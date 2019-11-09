# -*- coding: utf-8 -*-

import wx

class BoxSizerExample(wx.Frame):
    def __init__(self, parent):
        super(BoxSizerExample, self).__init__(parent, title='BoxSizer example')

        self._InitUI()
        self.Center()

    def _InitUI(self):
        outerPanel = wx.Panel(self)
        outerPanel.SetBackgroundColour('#4f5049')

        innerPanel = wx.Panel(outerPanel)
        innerPanel.SetBackgroundColour('#ededed')

        # layout
        vbox = wx.BoxSizer(wx.VERTICAL)
        # Adding 20px border around the inner panel
        vbox.Add(innerPanel, wx.ID_ANY, wx.EXPAND | wx.ALL, 20) 

        outerPanel.SetSizer(vbox)

def main():
    app = wx.App()
    bse = BoxSizerExample(None)
    bse.Show(True)
    app.MainLoop()

if __name__ == '__main__' :
    main()
        
        
