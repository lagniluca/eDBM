# -*- coding: utf-8 -*-

class eDBMException(Exception):

    def __init__(self, message):
        self._message = message

    def getMessage(self):
        return "Errore: " + self._message
    def __str__(self):
        return "Errore: " + self._message