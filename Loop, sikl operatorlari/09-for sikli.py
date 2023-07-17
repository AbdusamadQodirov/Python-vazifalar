# dostlar = ["Nizom", "Fayoz", "Sherzod", "Samandar", "Abdulaziz", "Shohjahon"]

# for dost in dostlar:
#     print("Salom bugun choyxonaga kelasanmi", dost)

# sonlar = list(range(0, 21, 2))
# for son in sonlar: 
#     print(f"{son} ning kvadrati = {son ** 2}")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son ** 2)
# print(sonlar)
# print(sonlar_kvadrati)

# n = int(input())
# sonlar = list(range(n))
# j = 0
# for i in sonlar:
#     sonlar[j] = int(input())
#     j += 1
# print(sonlar[-2:])

# n = str(input())
# j = 0
# k = 0
# for i in range(int(len(n)) + 1):
#     if n[i] == '0':
#         k += 1 
# print(k)


                                        #  Amaliyot

# ismlar = ["Akmal", "Alam", "Akbar", "Alisher", "Anvar"]
# for ism in ismlar:
#     print(f" Salom {ism}")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# toq_sonlar = list(range(11, 100, 2))
# toq_sonlarning_kubi = []
# for son in toq_sonlar:
#     toq_sonlarning_kubi.append(son ** 3)
# print(toq_sonlarning_kubi)

# eng_zor_kinolar = []
# for i in range(5):
#     eng_zor_kinolar.append(input())
# print(eng_zor_kinolar)

# suhbatlashganlar_soni = []
# a = int(input("Bugun nechta inson bilan suhbatlashdingiz >>>"))
# for i in range(a):
#     suhbatlashganlar_soni.append(input(f"{i + 1} - suhbat qilgan insoningiz: "))
# print("Suhbatlashgan insonlaringiz :) ->", suhbatlashganlar_soni)

for i in range(1, 5):
    for j in range(1, 5):
        if i + j >= 5:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
print()

""" for i in range(1, 5):
    for j in range(1, 5):
        if i + j <= 5:
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print()
print()
for i in range(1, 5):
    for j in range(1, 5):
        if i <= j:
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print()
print()
for i in range(1, 5):
    for j in range(1, 5):
        if i >= j:
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print()
print()
for i in range(1, 5):
    for j in range(1, 5):
            if j % 2 == 0 & i % 2 == 0:
                print("*", end = " ")
            else:
                print(" ",end = " ")
    print()    
print()

for i in range(1, 5):
    for j in range(1, 5):
        if i + j >= 5:
            print("*", end = " ")
        else:
            print(" ",end = " ")
    print()
for i in range( 1, 6):
    for j in range(1,  6):
            if i + j <= 2 or (i + j >= 2 and i + j <= 4):

                print("*", end = " ")
            else:
                print(" ",end = " ")
    print()
print() """


      
