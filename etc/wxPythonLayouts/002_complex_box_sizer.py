# -*- coding: utf-8 -*-

import wx

class ComplexBoxSizerExample(wx.Frame):
    def __init__(self, parent):
        super(ComplexBoxSizerExample, self).__init__(parent, title='Complex BoxSizer example')

        self._InitUI()
        self.Center()

    def _InitUI(self):
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        # sizer used for the entire panel
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Section 1 of the UI
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        st1 = wx.StaticText(panel, label='first section:')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        tc1 = wx.TextCtrl(panel)
        hbox1.Add(tc1, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Section 2
        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='second section')
        st2.SetFont(font)
        hbox2.Add(st2)

        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        # Section 3
        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE) # TextArea example
        hbox3.Add(tc2, proportion=1, flag=wx.EXPAND) # Example of differe size in case of expansion

        vbox.Add(hbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        # Section 4
        vbox.Add((-1, 25)) # 25 because above we have a TextArea

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(panel, label='fourth section 1')
        cb1.SetFont(font)
        hbox4.Add(cb1)
        cb2 = wx.CheckBox(panel, label='fourth section 2')
        cb2.SetFont(font)
        hbox4.Add(cb2, flag=wx.LEFT, border=10)
        cb3 = wx.CheckBox(panel, label='fourth section 3')
        cb3.SetFont(font)
        hbox4.Add(cb3, flag=wx.LEFT, border=10)

        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        # Section 5
        vbox.Add((-1, 30)) # 30 for adding more space between input elements and buttons

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Ok', size=(70, 30))
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label='Close', size=(70, 30))
        hbox5.Add(btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        # General layout
        panel.SetSizer(vbox)

def main():

    app = wx.App()
    ex = ComplexBoxSizerExample(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
        
