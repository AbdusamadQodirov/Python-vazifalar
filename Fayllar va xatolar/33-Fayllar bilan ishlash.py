# file = open("PI.txt")
# PI = file.read()
# print(PI)
# file.close()

# with open('PI.txt') as file:
#     pi = file.read()
# print(pi)

# pi = pi.rstrip()
# pi = pi.replace('\n', "")
# pi = float(pi)
# print(pi)

# file_name = 'PI.txt'
# with open(file_name) as file:
#     for l in file:
#         print(l)

# with open(file_name) as file:
#     malumotlar = file.readlines()
# print(malumotlar)
# malumotlar = [malumot.rstrip() for malumot in malumotlar]
# print(malumotlar)

# fayl_nomi = 'New_fayl.txt'
# ism = 'Abdusamad'
# familiya = 'Qodirov'
# tyil = 2005
# with open(fayl_nomi, 'w') as file:
#     file.write(ism + '\n')
#     file.write(familiya + '\n')
#     file.write(str(tyil) + '\n')
# with open(fayl_nomi) as file:
#     pi = file.read()
# print(pi)

# with open(fayl_nomi, 'a') as file:
#     file.write('Salom mening ismim Abdusamad')
# with open(fayl_nomi) as file:
#     print(file.read())

# import pickle

# talaba1 = {'ism' : 'Abdusamad', 'familiya' : 'Qodirov', 'tyil' : 2005}
# talaba2 = {'ism' : 'Abdulaziz', 'familiya' : 'Qodirova', 'tyil' : 2007}

# with open('talaba', 'wb') as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)

# with open('talaba', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
# print(talaba1, talaba2)


                                # Amaliyot

# matn = "1.Bugun men bu darsda fayllar bilan ishlash haqida o'rgandim.\n Faylni ochish uchun open faylni yopish uchun esa close funksiyasidan foydalaniladi. \n"
# matn1 = "2.Dasturni ochib yopish uchun esa bu koddan foydalaniladi 'with open('faylnomi.formati') as file: \n print(file.read()) \n"
# matn2 = "3.Agar with open(faylnomi, 'w') deb yozilsa bu faylni yozish un ochiladi \nAgar with open('wb') deb yozilsa bu fayl ikkilik sanoq sistemasida yoziladi\n"
# matn3 = "4.Dasturga obyektlarni o'zgaruvchilarni qo'shish uchun pickle kutubxonasini import qilish kerak.\n with open('faylnomi', 'wb') as file: \n pickle.dump(o'zgaruvchi yoki obyektni kiritishimiz kerak boladi, file) "

# with open("Python fayllar bilan ishlash.txt", 'w') as file:
#     file.write(matn)
#     file.write(matn1)
#     file.write(matn2)
#     file.write(matn3)
# with open('Python fayllar bilan ishlash.txt') as file:
#     print(file.read())

import pickle
with open('PI.txt') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')

pi1 = '02022005'
print(pi1 in pi)

pi = float(pi)

with open('PI', 'wb') as file:
    pickle.dump(pi, file)
 
while True:
    a = input("Yoqtirgan mashg'ulotlaringizni kiriting >>> (to'xtash uchun enter belgisini bosing)")
    if not a:
        break
    with open('mashgulotlar.txt', 'a') as file:
        file.write(a + '\n')
        
