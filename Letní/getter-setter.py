class ZapornyZustatek(Exception):
    pass

class BankovnuUcet():
    def __init__(self):
        self.zustatek = 0


    @property
    def zustatek(self):
        return self.__zustatek


    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise ZapornyZustatek(f"Nelze zapsat zustatel {hodnota}")
        self.__zustatek = hodnota

if __name__ == "__main__":
    try:
        muj_ucet = BankovnuUcet()
        print(muj_ucet.zustatek)
        muj_ucet.zustatek = -100
        print(muj_ucet.zustatek)
    except ZapornyZustatek as e:
        print(str(e))
    