# Mashhur1 = {
#     'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#     'tyil': 810,
#     'tjoy': 'Buxoro',
#     'umrkorgan': 60,
#     'mashhur asarlari': ['Al-jome as saxix', 'al-adab al-mufrat', 'al-tarix al-kabir', 'al-tarix as-sag\'ir']
# }
# Mashhur2 = {
#     'ism': 'Abdulla Qodiriy',
#     'tyil': 1894,
#     'tjoy': 'Toshkent',
#     'umrkorgan': 44,
#     'mashhur asarlari': ['Otkan kunlar', 'Mehrobdan Chayon', 'Obid ketmon']
# }
# Mashhur3 = {
#     'ism': 'Erkin Vohidov',
#     'tyil': 1936,
#     'tjoy': 'Farg\'onada',
#     'umrkorgan': 80,
#     'mashhur asarlari': ['Tong nafasi', 'Qoshiqlarim sizga', 'Ozbegim', 'Qiziquvchan Matmusa']
# }
# Mashhur4 = {
#     'ism': 'Alisher Navoiy',
#     'tyil': 1441,
#     'tjoy': 'Xirot',
#     'umrkorgan': 60,
#     'mashhur asarlari': ['Xamsa', 'Lison ut-tayr', 'mahbub ul-qulub']
# }
# Mashhur = [Mashhur1, Mashhur2, Mashhur3, Mashhur4]
# # for i in Mashhur:
# #     print(f"{i['ism']} {i['tyil']}da {i['tjoy']}da tavallud topgan. {i['umrkorgan']} - yil umr ko'rgan. ")
# for i in Mashhur:
#     print(f"{i['ism']}ning mashhur asarlari: ")
#     for j in i['mashhur asarlari']:
#         print(j)

# dostlar = {
#     'Ali': ['Terminator', 'rambo', 'titanic'],
#     'Vali': ['Tenet', 'Inception', 'Intersteller'],
#     'Hasan': ['Abdullajon', 'Bomba', 'Shaytanat'],
#     'Husan': ['Mahallada duv-duv gap', 'John Wick']
# }
# for key, value in dostlar.items():
#     print(f"{key.title()}ning sevimli kinolari:")
#     for j in value:
#         print(j.title())

# davlatlar = {
#     'ozbekiston': {
#
#     'poytaxti': 'Toshkent',
#     'hududi': 448978,
#     'aholisi': 33_000_000,
#     'pul birligi': "so'm"
#
#     },
#     'rossiya': {
#
#     'poytaxti': 'Moskva',
#     'hududi': 17098246,
#     'aholisi': 144_000_000,
#     'pul birligi': "rubl"
#
#     },
#     'aqsh': {
#
#     'poytaxti': 'Vashington',
#     'hududi': 9631418,
#     'aholisi': 327_000_000,
#     'pul birligi': "dollar"
#
#     },
#     'malayzia': {
#
#     'poytaxti': 'Kuala-Lumpur',
#     'hududi': 329750,
#     'aholisi': 25_000_000,
#     'pul birligi': "rinngit"
#
#     }
# }
# for k, v in davlatlar.items():
#     print(k.title())
#     for k1, v1 in v.items():
#         if k1 == 'hududi':
#             print(k1.capitalize(), ":", v1, "kv.km")
#         else:
#             print(k1.capitalize(), ":", v1)

# a = input("Davlat nomini kiriting:")
# keys = []
# for k, v in davlatlar.items():
#     keys.append(k)
#     if k == a:
#         print(k.title())
#         for k1, v1 in v.items():
#             if k1 == 'hududi':
#                 print(k1.capitalize(), ":", v1, "kv.km")
#             else:
#                 print(k1.capitalize(), ":", v1)
# j = 0
# for i in keys:
#     if i == a:
#         j += 1
# if j == 0:
#     print('Bizda bu davlat haqida malumot yoq')







