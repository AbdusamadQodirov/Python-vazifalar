class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    def get_info(self):
        """ Shaxs haqida ma'lumot beradi """
        info = f"{self.ism} {self.familiya}, "
        info += f"Passport: {self.passport}"
        return info
    def get_age(self, yil):
        return yil - self.tyil
# class Talaba(Shaxs):
#     def __init__(self, ism, familiya, tyil, passport, id, manzil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.id = id
#         self.manzil = manzil
#         self.bosqich = 1
#     def get_id(self):
#         return self.id
#     def get_bosqich(self):
#         return self.bosqich
#     def bosqich_update(self):
#         self.bosqich += 1
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. Passport: {self.passport}, Id: {self.id}. {self.tyil} - yilda tug'ilgan. {self.get_age(2023)} yoshda"
#
# class Manzil:
#     def __init__(self, viloyat, shahar, tuman, uy):
#         self.viloyat = viloyat
#         self.shahar = shahar
#         self.tuman = tuman
#         self.uy = uy
#     def get_manzil(self):
#         return f"Yashash manzili: {self.viloyat} viloyati {self.shahar} shahri {self.tuman} tumani {self.uy} - uy."
# talaba1_manzil1 = Manzil("Toshkent", "Chirchiq", "Qibray", "12")
# talaba1 = Talaba("Abdusamad", "Qodirov", 2005, "1352524542", "!BK2422345", talaba1_manzil1)
# print(talaba1.manzil.get_manzil())
#
# print(talaba1.get_info())
# print(talaba1.get_age(2023))


                                            # Amaliyot

# class Talaba:
#     def __init__(self, ism, familiya, id, bosqich):
#         self.ism = ism
#         self.familiya = familiya
#         self.id = id
#         self.bosqich = bosqich
#         self.fanlar = []
#     def get_info(self):
#         return f"{self.ism.title()} {self.familiya.title()}. {self.bosqich} - bosqich. ID : {self.id}"
#     def fanga_yozil(self, fan):
#         self.fanlar.append(fan)
#     def yozilgan_fanlar(self):
#         return [j for j in self.fanlar]
#     def fan_remove(self, i):
#         if i in self.fanlar:
#             self.fanlar.remove(i)
#         else:
#             print("Siz bunday fanga yozilmagansiz")
#
# class Fanlar:
#     def __init__(self, nomi ):
#         self.nomi = nomi
# fan1 = Fanlar("Chiziqli algebra")
# fan2 = Fanlar("Differensial tenglamalar")
# fan3 = Fanlar("Dasturlash")
# talaba1 = Talaba("Abdusamad", "Qodirov", "1BK314346", 2)
# talaba2 = Talaba("Abdujalil", "Qodirov", "1Bk73567", 0)
# talaba1.fanga_yozil(fan1.nomi)
# talaba1.fanga_yozil(fan2.nomi)
# talaba1.fan_remove(fan2.nomi)
#
# print(talaba1.yozilgan_fanlar())


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, maqsadi, tyil):
        super().__init__(ism, familiya, tyil)
        self.maqsadi = maqsadi
        self.tarix = []
    def harakatlari_tarixi(self, malumot):
        self.tarix.append(malumot)
    def get_info(self):
        return f"{self.ism} {self.familiya}. Maqsadi: {self.maqsadi}, Tugilgan yili: {self.tyil}"
class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, tyil, passport, nimasotishi):
        super().__init__(ism, familiya, passport, tyil)
        self.buyumlar = nimasotishi
    def get_info(self):
        return f"{self.ism} {self.familiya}. Tugilgan yili: {self.tyil}, Sotadigan buyumlari: {self.buyumlar}"
sotuvchi1 = Sotuvchi("Akmal", "Sharipov", 2005, "oziq-ovqat", "kiyim")

print(sotuvchi1.tyil)
print(sotuvchi1.passport)

# class Mijoz(Sotuvchi):
#     def __init__(self, ism, familiya, tyil, passport):
#         pass







