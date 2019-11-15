# -*- coding: utf-8 -*-

"""
functions used for geneating the lotto
"""

import datetime

LOTTO_LAST_DATE_FILE = "lotto_ultima_data.txt"
LOTTO_LAST_DATE_INDEX = "lotto_indice_registrazione.txt"


class eDBMLottoGenerator:
    def __init__(self):
        self.__current_date = None
        self.__current_time = None
        self.__last_lotto_date = None
        self.__last_lotto_index = None
        self.__lotto = None

        self.__init_current_date()
        self.__init_current_time()
        self.__init_lotto_last_date()
        self.__init_lotto_last_index()
        self.__generate_lotto()

    # Setters
    def __init_current_date(self):
        self.__current_date = datetime.date.today()

    def __init_current_time(self):
        now = datetime.datetime.now()
        self.__current_time = now.strftime("%H:%M:%S")

    def __init_lotto_last_date(self):
        f = open(LOTTO_LAST_DATE_FILE, "r")
        data = f.read()
        f.close()
        ultima_data = datetime.datetime.strptime(data, '%Y-%m-%d')
        self.__last_lotto_date = ultima_data.strftime('%Y-%m-%d')

    def __init_lotto_last_index(self):
        if str(self.__current_date) == str(self.__last_lotto_date):
            f = open(LOTTO_LAST_DATE_INDEX, "r")
            self.__last_lotto_index = int(f.read())
            f.close()
        else:
            self.__last_lotto_index = 0

    def __generate_lotto(self):
        anno = int(datetime.datetime.now().year)
        anno = anno - 2000
        mese_num = int(datetime.datetime.now().month)
        mese_str = ""
        giorno = int(datetime.datetime.now().day)
        self.__last_lotto_index = self.__last_lotto_index + 1

        if mese_num == 1:
            mese_str = "A"
        elif mese_num == 2:
            mese_str = "B"
        elif mese_num == 3:
            mese_str = "C"
        elif mese_num == 4:
            mese_str = "D"
        elif mese_num == 5:
            mese_str = "E"
        elif mese_num == 6:
            mese_str = "F"
        elif mese_num == 7:
            mese_str = "G"
        elif mese_num == 8:
            mese_str = "H"
        elif mese_num == 9:
            mese_str = "I"
        elif mese_num == 10:
            mese_str = "L"
        elif mese_num == 11:
            mese_str = "M"
        else:
            mese_str = "N"

        self.__lotto = ""

        self.__lotto += str(anno)
        self.__lotto += str(mese_str)
        self.__lotto += str(giorno)

        self.__lotto += str(self.__last_lotto_index)

    def get_lotto(self):
        return str(self.__lotto)

    def update_index(self):
        # updating the index
        f = open(LOTTO_LAST_DATE_INDEX, "w")
        f.write(str(self.__last_lotto_index))
        f.close()

        # updating the date
        f = open(LOTTO_LAST_DATE_FILE, "w")
        f.write(str(self.__current_date))
        f.close()
