yil = input("Yoshingizni kiriting ")
try:
    yil = int(yil)
except ValueError:
    print('Siz butun son kiritishingiz kerak')
else:
    print(f"Siz {2023 - yil} yilda tug'ilgansiz ")



try:
    x = int(input('x = '))
except ValueError:
    print('Butun son kiriting')

try:
    y = int(input('y ='))
except ValueError:
    print('Butun son kiriting')

try:
    x = x / y
except ZeroDivisionError:
    print("Sonni 0 ga bolish mumkin emas")
except NameError:
    print("Iltimos dasturni qayta ishga tushiring")
else:
    print(x)
