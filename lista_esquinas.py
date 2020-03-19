from esquina import Esquina


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

    def get_sorted_data(self, key, rows=None):
        return self.__sort_list_of_esquinas(self.get_data(rows), key)

    def find_by_key(self, key, objetivo):
        data = self.__sort_list_of_esquinas(self.get_data(self.count//2000), key)
        return self.__binary_search(data, 0, len(data), objetivo, key)

    def __binary_search(self, lista, comienzo, final, objetivo, key):

        medio = (comienzo + final) // 2
        item = getattr(lista[medio], key)
        if comienzo > final:
            return 0

        if item == objetivo:
            return lista[medio]
        elif item < objetivo:
            return self.__binary_search(lista, medio + 1, final, objetivo, key)
        else:
            return self.__binary_search(lista, comienzo, medio - 1, objetivo, final)

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
        elif key == "corner_name":
            newlist = sorted(esquinas, key=lambda x: x.corner_name, reverse=reverse)
        elif key == "cx":
            newlist = sorted(esquinas, key=lambda x: x.cx, reverse=reverse)
        elif key == "cy":
            newlist = sorted(esquinas, key=lambda x: x.cy, reverse=reverse)
        return newlist
