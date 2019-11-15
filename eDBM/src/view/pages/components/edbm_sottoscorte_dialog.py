# -*- coding: utf-8 -*-

"""
Classe usata per rappresentare un dialog box nel caso di sottoscorte
"""

#librerie tkinter
from tkinter import *
from tkinter.ttk import Frame, Label

class eDBMSottoscorteDialog(Tk):
    def __init__(self, title, icon):
        super().__init__()

        self.title(title)
        self.resizable(False, False)

        self._InitUI(title)


    def _InitUI(self, title):

        f = Frame(self)
        f.pack(fill=BOTH, expand=1)

        xscrollbar = Scrollbar(f, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=N + S + E + W)

        yscrollbar = Scrollbar(f, orient=VERTICAL)
        yscrollbar.grid(row=0, column=1, sticky=N + S + E + W)

        self.text = Text(f, wrap=NONE,
                         xscrollcommand=xscrollbar.set,
                         yscrollcommand=yscrollbar.set)
        self.text.grid(row=0, column=0)

        xscrollbar.config(command=self.text.xview)
        yscrollbar.config(command=self.text.yview)


    def append_items(self, items):
        item = ""
        for i in items:
            if i is not None:
                item = item + i + "\n"
        self.text.insert(END, item)
        self.mainloop()

