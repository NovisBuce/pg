class ImutableInteger:
    def __init__(self, number):
        self.number = number
        self.imutable = False

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number
    
if __name__ == "__main__":
    ii = ImutableInteger(5)
    print(ii.number)

    ii.imutable = True
    ii.number == 60

    ii.imutable = False
    ii.number == 60