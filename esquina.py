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

    def get_table_columns(self):
        for key in self.dictionary:
            item = self.dictionary[key]
            print(key, "--", item, "---", type(item))
            if(type(item) == type(1)):
                print("INTEGER")
            elif (type(item) == type(1.0)):
                print("REAL")
            elif (type(item) == type("1")):
                print("TEXT")
