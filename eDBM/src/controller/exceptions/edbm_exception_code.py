# -*- coding: utf-8 -*-

"""
Series of exception codes that can be rised by the application
"""

from enum import Enum

class EdbmExceptionCode(Enum):

    # Database related exceptions
    DATABASE_CONNECTION_NOT_ESTABLISHED = "Non è stato possibile stabilire una connessione con il database"
    DATABASE_CONNECTION_NOT_CLOSED      = "Non è stato possibile terminare la connessione con il database"
    DATABASE_CONNECTION_NOT_ESTABLISHED_YET = "La connessione con il database non è stata ancora stabilita"
    INVALID_QUERY_PROVIDED = "La query passata per l'esecuzione non e' valida"
    UNABLE_TO_PERFORM_QUERY = "Non e' stato possibile eseguire la query"
    UNABLE_TO_CLOSE_DATABASE_CURSOR = "Non e' stato possibile chiudere i records del database"

