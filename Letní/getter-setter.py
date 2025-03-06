class BankovnuUcet():
    self.zustatek = 0


    @property
    def zustatek(self):
        return self.__zustatek


    @zustatek.setter
    def zustatek(self, hodnota):
        self.__zustatek = hodnota

if __name__ == "__main__":
    muj_ucet = BankovnuUcet()
    print(muj_ucet.zustatek)
    muj_ucet.zustatek = -100
    print(muj_ucet.zustatek)