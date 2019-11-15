# -*- coding: utf-8 -*-

"""
Class used for reading a file after a certain period
"""

from threading import Thread

import time

class eDBMThreadedFileReader(Thread):
    def __init__(self, file_input_path, file_output_data_path, file_output_index_path, period_s, window):
        Thread.__init__(self)

        self.__period_s = None
        self.__file_path = None
        self.__stop_reading = None
        self.__current_row = None
        self.__file_input_path = None
        self.__file_output_data_path = None
        self.__file_output_index_path = None
        self.__window = window

        self.__set_file_input_path(file_input_path)
        self.__set_file_output_data_path(file_output_data_path)
        self.__set_file_output_index_path(file_output_index_path)
        self.__set_period_s(period_s)
        self.__set_stop_reading(False)

    # Setters
    def __set_file_input_path(self, file_input_path):
        self.__file_input_path = file_input_path

    def __set_file_output_data_path(self, file_output_data_path):
        self.__file_output_data_path = file_output_data_path

    def __set_file_output_index_path(self, file_output_index_path):
        self.__file_output_index_path = file_output_index_path

    def __set_window(self, window):
        self.__window = window

    def __set_period_s(self, period_s):
        self.__period_s = period_s

    def __set_stop_reading(self, stop_reading):
        self.__stop_reading = stop_reading

    def stop_reading(self):
        self.__stop_reading = True

    # application
    def __read_file_output_index(self):
        file = open(self.__file_output_index_path, "r")
        self.__current_row = int(file.read())
        file.close()

    def __check_new_data_availability(self):
        in_file = open(self.__file_input_path, "r")
        input_file_path = in_file.read()
        in_file.close()

        input_file = open(input_file_path, "r")
        rows = input_file.readlines()
        if rows is not None:
            if len(rows) > self.__current_row:
                output_file = open(self.__file_output_data_path, "a")
                i = 0
                for row in rows :
                    if i >= self.__current_row:
                        output_file.write(row)
                    i = i + 1
                output_file.close()
                index_file = open(self.__file_output_index_path, "w")
                index_file.write(str(len(rows)))
                index_file.close()
                self.__window.added_sottoscorte_alert(self.__file_output_data_path)


    def run(self):
        if not self.__stop_reading:
            while not self.__stop_reading:
                self.__read_file_output_index()
                self.__check_new_data_availability()
                time.sleep(self.__period_s)

    # Getters
    def get_file_output_data_path(self):
        return self.__file_output_data_path

    def get_file_input_path(self):
        return self.__file_input_path

    def get_file_output_index_path(self):
        return self.__file_output_index_path

    def get_period_s(self):
        return self.__period_s

    def is_stop_reading(self):
        return self.__stop_reading