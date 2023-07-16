        # Amaliyot
from uuid import uuid4
class Shaxs:
    __odamlar_soni = 0
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__yashagan_yili = 0
        Shaxs.__odamlar_soni += 1
    def set_yashagan_yili(self, yil):
        self.__yashagan_yili += (yil - self.tyil)
    def get_yashagan_yili(self):
        return f"Bu shaxs {self.__yashagan_yili}"
    @classmethod
    def get_odamlar_soni(cls):
        return f"Odamlar soni: {cls.__odamlar_soni}"
class Talaba:
    __talabalar_soni = 0
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__bosqich = 1
        self.__id = uuid4()
        Talaba.__talabalar_soni += 1
    def get_id(self):
        return f"Talabaning id raqami: {self.__id}"
    def update_id(self):
        self.__id = uuid4()
    def update_bosqich(self):
        self.__bosqich += 1
    def get_bosqich(self):
        return f"Talabaning o'quv bosqichi: {self.__bosqich}"
    @classmethod
    def get_talabalar_soni(cls):
        return f"Talabalar soni: {cls.__talabalar_soni}"
talaba1 = Talaba('Abdusamad', 'Qodirov', 2005)
shaxs1 = Shaxs("Javohir", 'Abdurashidov', 2004)
shaxs1 = Shaxs("Javohir", 'Abdurashidov', 2004)
# print(talaba1.get_id())
# print(talaba1.get_bosqich())
# print(talaba1.get_talabalar_soni())
# print(shaxs1.get_odamlar_soni())