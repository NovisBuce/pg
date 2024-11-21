class BadDataError(Exception):
    pass


class Souradnice:

    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka

        def get_sirka(self):
            return self.sirka
        
        def set_sirka(self, nova_sirka):
            self.__sirka = nova_sirka

        @property
        def sirka(self):
            return self.__sirka
        
        @property
        def delka(self):
            return self.__delka
    
    def __str__(self) -> str:
        return f'Souradnice: {self.sirka}, {self.delka}'
    
    @classmethod
    def nacti_z_dat(cls, data):
        if "souradnice" not in data:
            raise BadDataError
        souradnice = data["souradnice"]
        if not isinstance(souradnice, dict):
            raise BadDataError
        if "sirka" not in souradnice or "delka" not in souradnice:
            raise BadDataError
        return cls(souradnice["sirka"], souradnice["delka"])


if __name__ == "__main__":

    data = {"souradnice": {"sirka": 50, "delka": 50}}
    s = Souradnice.nacti_z_dat(data)
    print(s)