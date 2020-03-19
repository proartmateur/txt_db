import os
import typing
import io
import cchardet
import json


# CVEESQUINA,Street_Nam "CALLE", Street_N_1 "ESQUINA",CX,CY
# 1000,"52707","52707001","5270700103781","CENTRAL CHIAPAS O","",-92.680050,15.341500
class Esquina:
    def __init__(self, row: str = None):
        self.cve = None
        self.street_name = None
        self.corner_name = None
        self.cx = 0
        self.cy = 0
        self.__column_names = ["id", "col1", "col2", "cve", "street_name", "corner_name", "cx", "cy"]
        self.dictionary = {}
        if row is not None:
            self.__get_data_from_row(row)

    def __proccess_type(self, data):
        """
        PRIVATE

        Evalúa si el dato puede convertirse a otro tipo de dato,
        como int, float o str.

        :arg: data es una cadena que necesita evaluarse
        """
        clean_data = None
        if '"' in data:
            clean_data = data.replace('"', '').strip()
        elif '.' in data:
            clean_data = float(data)
        else:
            clean_data = int(data)

        return clean_data

    def __get_data_from_row(self, row: str):
        """
        PRIVATE

        Obtiene los datos de la cadena de texto y los pasa al objeto Esquina.

        :arg row es una cadena que contiene los datos de la esquina. Viene de un txt.
        """
        data_split = row.split(",")
        if len(self.__column_names) == len(data_split):
            for i in range(0, len(data_split)):
                self.dictionary[self.__column_names[i]] = self.__proccess_type(data_split[i])

            self.cve = self.dictionary["cve"]
            self.street_name = self.dictionary["street_name"]
            self.corner_name = self.dictionary["corner_name"]
            self.cx = self.dictionary["cx"]
            self.cy = self.dictionary["cy"]
            self.id = self.dictionary["id"]
            self.col1 = self.dictionary["col1"]
            self.col2 = self.dictionary["col2"]


class ListaEsquinas:
    def __init__(self, file_txt):
        self.__esquinas = self.__read_esquinas(file_txt)
        self.count = len(self.__esquinas)

    def get_data(self, rows=None):
        return_data = []
        if rows is None:
            for item in self.__esquinas:
                return_data.append(Esquina(item))
        else:
            for i in range(0, rows):
                return_data.append(Esquina(self.__esquinas[i]))

        return return_data

    def get_sorted_data(self, rows=None):
        return self.__sort_list_of_esquinas(self.get_data(rows), "id")

    def __read_esquinas(self, file_txt):
        with open(file_txt, 'r', encoding='ISO-8859-1') as f:
            s1 = f.readlines()
        return s1

    def __sort_list_of_esquinas(self, esquinas: list, key: str, reverse=False) -> list:
        newlist = []
        if key == "id":
            newlist = sorted(esquinas, key=lambda x: x.id, reverse=reverse)
        elif key == "cve":
            newlist = sorted(esquinas, key=lambda x: x.cve, reverse=reverse)
        elif key == "street_name":
            newlist = sorted(esquinas, key=lambda x: x.street_name, reverse=reverse)
        elif key == "cx":
            newlist = sorted(esquinas, key=lambda x: x.cx, reverse=reverse)
        elif key == "cy":
            newlist = sorted(esquinas, key=lambda x: x.cy, reverse=reverse)
        return newlist


if __name__ == "__main__":
    data = [

        '1000, "52707", "52707001", "5270700103781", "CENTRAL CHIAPAS O", "", -92.680050, 15.341500',
        '821, "52707", "52707001", "5270700103781", "", "CENTRAL CHIAPAS O", -92.680050, 15.341500',
        '1123, "52707", "52707001", "5270700103782", "AVENIDA 16 DE SEPTIEMBRE N", "TABASCO", -92.669740, 15.346070',
        '1001, "52707", "52707001", "5270700103782", "TABASCO", "AVENIDA 16 DE SEPTIEMBRE N", -92.669740, 15.346070',
    ]
    li = ListaEsquinas("CAT_ESQUINAS.txt")
    for item in li.get_data(4):
        print(item.id)

    for item in li.get_sorted_data(4):
        print(item.id)
