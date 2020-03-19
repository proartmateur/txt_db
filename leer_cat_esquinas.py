import os
import typing
import io
import cchardet
import json

# CVEESQUINA,Street_Nam "CALLE", Street_N_1 "ESQUINA",CX,CY
# 1000,"52707","52707001","5270700103781","CENTRAL CHIAPAS O","",-92.680050,15.341500

from lista_esquinas import ListaEsquinas

if __name__ == "__main__":
    li = ListaEsquinas("CAT_ESQUINAS.txt")
    print(f"Total of rows: {li.count}")
    for item in li.get_data(4):
        print(item.id)

    print("*" * 50)

    for item in li.get_sorted_data("corner_name", 14):
        print(item.corner_name)

    print("-" * 50)

    res = li.find_by_key("corner_name", "TABASCO")
    print(res.dictionary)


