class Talaba:
        def __init__(self, tugilgan_yil, ism, familiya):
            self.name = ism
            self.sourname = familiya
            self.birthday = tugilgan_yil


# talaba1 = Talaba(2005, "Abdusamad", "Qodirov")
# print(talaba1.name)
# print(talaba1.birthday)
# print(talaba1.sourname)
# print(talaba1.get_age(2023))

# class User:
#     def __init__(self, ism, familiya, email, parol):
#         self.name = ism
#         self.lastname = familiya
#         self.email = email
#         self.password = parol
#     def get_info(self):
#         return f"Foydalanuvchining ismi: {self.name}\nFamiliyasi: {self.lastname}\nEmaili: {self.email}"
#     def get_fullname(self):
#         return f"{self.name} {self.lastname}"
# user1 = User("Abdulaziz", "Qodirov", "abdulazizqodirov233@gmail.com", "1234")
# print(user1.name)
# print(user1.get_info())
# print(user1.email)
#
# class Fan:
#     def __init__(self, nomi):
#         self.fan_nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
#     def add_students(self, talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#     def get_students(self):
#         return [user.get_fullname() for user in self.talabalar]
# def see_user(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]
# matem = Fan("Oliy matematika")
# matem.add_students(user1)
# user2 = User("Akbar", "Shokirov", "akbarshok@gmail.com", 12345678)
# matem.add_students(user2)
# print(matem.talabalar_soni)
# print(matem.fan_nomi)
# print(matem.talabalar)
# print(matem.get_students())
# print(dir(User))
# print(see_user(User))


                                            # Amaliyot topshiriq


# class Avto():
#     def __init__(self, model, rang, korobka, narh):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.kilometr = 0
#     def get_model(self):
#         return self.model
#     def get_rang(self):
#         return self.rang
#     def get_korobka(self):
#         return self.korobka
#     def get_narh(self):
#         return self.narh
#     def get_info(self):
#         return f"{self.rang.title()} rangdagi {self.korobka} karobkali {self.model.title()}ning narhi: {self.narh} sum "
#     def avto_update_kilometr(self, km):
#         self.kilometr += km
# class Avtosalon():
#     def __init__(self, nomi, manzili):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.sotuvdagi_avtomobillar = []
#         self.avtomobil_soni = 0
#     def add_avto(self, avtomobil):
#         self.sotuvdagi_avtomobillar.append(avtomobil)
#         self.avtomobil_soni += 1
#     def avtosalon_avtomobil_info(self):
#         return [avto.get_info() for avto in self.sotuvdagi_avtomobillar]
# avto1 = Avto("malibu", "qizil", "avtomat", 375_000_000)
# avto2 = Avto("Damas", "oq", "mexanika", 118_000_000)
# avto3 = Avto("Spark", "qora", "avtomat", 112_000_000)
#
# avtosalon = Avtosalon("Uz_avto_motors", "Tashkent")
# avtosalon1 = Avtosalon("ASACAR AUTOCENTER", "Tashkent")
# avtosalon3 = Avtosalon("DRIVER’S VILLAGE", "Tashkent")
# avtosalon.add_avto(avto1)
# avtosalon.add_avto(avto2)
# avtosalon.add_avto(avto3)
# print(avtosalon.sotuvdagi_avtomobillar)
#
# def see_method(klass):
#     return [method for method in dir(klass) if method.startswith("__") is False]
# print(see_method(avto1))





















