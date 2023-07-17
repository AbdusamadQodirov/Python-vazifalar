# ism = ["Nizom", "Fayoz", "Samandar", "Sherzod", "Abdulaziz", "Shohjahon"]
# print(f"{ism[0]} bugun choyxonaga kelasanmi \n {ism[1]}, {ism[2]}, {ism[3]}, {ism[4]}, {ism[5]} sanlachi")

# sonlar = [123, -23, 23.5, -98.8,]
# sonlar.remove(123)
# sonlar.insert(0, 345)
# sonlar[3] = sonlar[1] + sonlar[2]
# print(sonlar)

# t_shaxslar = ["Enshteyn", "Bill Geyts", "Zuckerberg"]
# z_shaxslar = ["Elon Musk", "Stiv Jobs", "Muhammadali"]
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan {z_shaxslar.pop(0)} ni uchrashishini xohlar edim")

friends = []
friends.append("Nizom")
friends.append("Fayoz")
friends.append("Samandar")
friends.append("Sherzod")
friends.append("Abdulaziz")
friends.append("Shohjahon")

friends.remove("Shohjahon")
friends.remove("Abdulaziz")
friends.insert(0, "Alisher")
friends.insert(-1, "Javohir")
friends.insert(3, "San'at")
print(friends)

mehmonlar = []
mehmonlar.append("Nizom") 
del mehmonlar[0]
mehmonlar.append(friends.pop(0))
mehmonlar.insert(-1, "Javohir")
print(friends)

print(mehmonlar)


