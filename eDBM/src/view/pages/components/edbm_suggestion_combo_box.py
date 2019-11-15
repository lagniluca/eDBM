# -*- coding: utf-8 -*-

"""
Class that implements a combo box that is able to autosuggest possible values for a given search base on the character
passed so far
"""

# user interfaces libraries
import wx

class eDBMSuggestionComboBox(wx.ComboBox):

    def __init__(self, parent, value, choices=[], style=0, **par):
        wx.ComboBox.__init__(self, parent, wx.ID_ANY, value, style=style | wx.CB_DROPDOWN, choices=choices, **par)

        self.choices = choices
        self.ignoreEvtText = False

        self.Bind(wx.EVT_TEXT, self.EvtText)
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox)

    def EvtComboBox(self, event):
        self.ignoreEvtText = True
        event.Skip()

    def EvtChar(self, event):
        if event.GetKeyCode() == 8:
            self.ignoreEvtText = True

        event.Skip()

    def EvtText(self, event):
        if self.ignoreEvtText :
            self.ignoreEvtText = False
            return
        currentText = event.GetString()
        found = False
        for choice in self.choices:
            if choice.startswith(currentText):
                self.ignoreEvtText = True
                self.SetValue(choice)
                self.SetInsertionPoint(len(currentText))
                self.SetMark(len(currentText), len(choice))
                found = True
                break

        if not found :
            event.Skip()