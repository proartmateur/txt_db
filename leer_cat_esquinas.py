import os
import typing
import io
import cchardet
import json

# CVEESQUINA,Street_Nam "CALLE", Street_N_1 "ESQUINA",CX,CY
# 1000,"52707","52707001","5270700103781","CENTRAL CHIAPAS O","",-92.680050,15.341500

from lista_esquinas import ListaEsquinas

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

    print("*" * 50)

    for item in li.get_sorted_data("corner_name", 14):
        print(item.corner_name)

    print("-" * 50)

    res = li.find_by_key("corner_name", "TABASCO")
    print(res.dictionary)
