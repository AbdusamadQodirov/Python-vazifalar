# import datetime as dt
# hozir = dt.datetime.now()
# print(hozir)

# time = dt.datetime.now().strftime("%H:%M:%S")
# time1 = dt.datetime.now().strftime("%d/%m/%Y")
# time3 = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
# print(time3)
# print(time, time1)

# import math
# pi = math.pi
# print(pi)

# e = math.e
# print(e)

# radian = math.pi/2
# print(radian)
# radian = math.degrees(radian)
# print(radian)

# from pprint import pprint
# import json
# salom = {
#     'oquvchilar': ['Abdujalil', 'Fazilat', 'Abdurashid', 'Umida', 'Abdulaziz', 'Zilola'],
#     'Alochilar': ['Nima gap', 'qalesan', 'nima qivossan', 'yashil', 'kok', 'qizil', 'sariq', 'jigarrang', 'toq kok'],
#     'kim': 'salom'
# }
# json.dumps(salom)
# print(salom)
# pprint(salom)

# import re
# andoza = "^s...m$"
# print(re.match(andoza, 'salom'))
# print(re.match(andoza, 'salam'))
# print(re.match(andoza, 'sla'))

# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# print(re.match(andoza, 'nimagap@gmail.com'))

# Amaliyot

# import datetime as dt

# time = dt.date(2023, 8, 2)
# time_after_two_weeks = dt.date(2023, 8, 16)
# for i in range(14):
#     print(f"{time.day + i}/{time.month}/{time.year}")

# def birthday(time):
#     time = time.split(", ")
#     for i in range(len(time)):
#         time[i] = int(time[i])
#     print(time)
#     time1 = dt.date(time[2], time[1], time[0])   
#     today = dt.date.today()
#     return today - time1
# print(birthday('2, 2, 2023'))



import re
# str0 = 'Iltimos telefon raqamingizni kiriting:'
# str1 = input(str0)
# print(re.match('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', str1))

matn = """Maqolalar  2020-yilning 20-martiga qadar https://github.com/geongeorge/i-hate-regex elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
andoza = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
url = re.findall(andoza,matn)
print(url)
