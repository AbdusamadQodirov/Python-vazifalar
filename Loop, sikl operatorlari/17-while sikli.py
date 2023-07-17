print("Istalgan sonning kvadratini hisoblovchi dastur:")
savol = "Sonni kiriting (Dasturni to'xtatish uchun exit deb yozing...) >>> "
qiymat = ""
while qiymat != "exit":
    qiymat = input(savol)
    if qiymat == "exit":
        break
    else:
        print(f"{qiymat}ning kvadrati:", float(qiymat)** 2)

son = 0
while son < 20:
    son += 1
    if son % 2 == 0:
        continue
    else:
        print(son)

while True:
    son = (input("Sonni kiriting (Dasturni to'xtatish uchun exit deb yozing...) >>> "))
    if son == "exit":
        break
    else:
        print(f"{son}ning kvadrati:", float(son)** 2)


                                    # Amaliyot
Kitoblar = []
while True:
    a = (input("Yoqtirgan kitobingiz nomini kiriting: "))
    if a == "stop":
        break
    else:
        Kitoblar.append(a)
print("Yoqtirgan kitoblaringiz ro'yxati:",Kitoblar)
print("Yoqtirmagan kitoblaringiz ro'yxati:",Kitoblar)

