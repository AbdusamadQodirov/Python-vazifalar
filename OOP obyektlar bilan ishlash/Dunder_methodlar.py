# class Avto:
#     def __init__(self, nomi, rangi, narxi, yili):
#         self.nomi = nomi
#         self.rangi = rangi
#         self.narxi = narxi
#         self.yili = yili
#     def __repr__(self):
#         return f"Avto: {self.nomi}, {self.narxi}"
# avto1 = Avto('malibu', 'qora', 40000, 2019)
# print(avto1)

# Amaliyot
from uuid import uuid4
class Talaba:
    __talabalar_soni = 0
    def __init__(self, ism, familiya, tyil, bosqich):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = bosqich
        Talaba.__talabalar_soni += 1
        self.__id = uuid4()
    def get_id(self):
        return self.__id
    def update_bosqich(self):
        self.bosqich += 1
    # def __lt__(self, bosqich):
    #     return self.bosqich < bosqich.bosqich
    # def __eq__(self, bosqich):
    #     return self.bosqich == bosqich.bosqich
    # def __le__(self, bosqich):
    #     return self.bosqich <= bosqich.bosqich

talaba1 = Talaba('Abdusamad', 'Qodirov', 2005, 1)
talaba2 = Talaba('Sherzod', 'Muhiddinov', 2004, 2)
talaba3 = Talaba('Nizom', 'Dostmuhammedov', 2005, 1)
talaba4 = Talaba('Fayoz', 'Xusanov', 2004, 2)
talaba5 = Talaba('Samandar', 'Yodgorov', 2004, 2)
talaba6 = Talaba('Abdulaziz', 'Abduraimov', 2004, 2)
talaba7 = Talaba('Hamza', 'Toshpolatov', 2004, 2)

# print(talaba1 == talaba3)
# print(talaba1 >= talaba3)

class Fan:
    __fanlar_soni = 0
    def __init__(self, nomi):
        self.nomi = nomi
        self.fan_talabalari = []
        Fan.__fanlar_soni += 1
    def __repr__(self):
        return f"{self.nomi} fani"

    def add_student(self, *talabalar):
        i = 1
        for talaba in talabalar:
            if isinstance (talaba, Talaba):
                self.fan_talabalari.append(talaba)
            else:
                print(f"{i} - qo'shilgan obyekt talaba emas")
            i += 1

    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.fan_talabalari[index] = value
    def __len__(self):
        return len(self.fan_talabalari)
    
    def get_fan_studentlari(self):
        return [i.ism for i in self.fan_talabalari]



    @classmethod
    def get_fanlar_soni(cls):
        return cls.__fanlar_soni
    
    def __add__(self, qiymat):
        if isinstance (qiymat, Fan):
            yangi_fan = Fan(f"{self.nomi} {qiymat.nomi}")
            yangi_fan.fan_talabalari = self.fan_talabalari + qiymat.fan_talabalari
            return yangi_fan


fan1 = Fan('Ona tili')
fan2 = Fan('matematika')
fan3 = Fan('Rus tili')

fan2.add_student(talaba1, talaba2, talaba3)
fan1.add_student(talaba4, talaba5, talaba6, talaba7)

# print(fan.fan_talabalari)
# print(fan1.get_fan_studentlari())

fan4 = fan1 + fan2

print(fan4.get_fan_studentlari())

    
        
    