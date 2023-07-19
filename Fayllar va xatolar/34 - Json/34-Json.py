import json
# x = 10
# x_json = json.dumps(x)
# print(x_json)

# bemor = {
#     'ism': 'Abdulaziz',
#     'familiya': 'Qodirov',
#     'oila': True,
#     'farzandlari': ('Ahmad', 'Bobur'),
#     'allergiya' : None,
#     'dorilar': [
#         {'nomi': 'Analgin', 'miqdori': 0.5},
#         {'nomi': 'Panadol', 'miqdori' : 1.2}
#     ]
# }
# bemor_json = json.dumps(bemor, indent = 2   )
# # print(bemor_json)

# with open('Bemor.json', 'w') as file:
#     json.dump(bemor, file)


# sonlar = (1, 2, 3, 4)

# with open('Sonlar.json', 'w') as file:
#     json.dump(sonlar, file)
# bemor2 = json.loads(bemor_json)
# print(bemor2)


# with open("Bemor.json") as file:
#     bemor = json.load(file)
# print(type(bemor))


                                        # Amaliyot
# data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json = json.dumps(data, indent = 3)
# print(data_json)

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(talaba['ism'], talaba['familiya'])

# with open('Data.json', 'w') as file:
#     json.dump(data, file)
# with open('Talaba.json', 'w') as file:
#     json.dump(talaba, file)

# student = {"student": [{"id": "01", "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"}, 
#              {"id": "02", "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"}, 
#              {"id": "03", "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}]}


# with open('students.json', 'r') as file:
#     student = json.load(file)
# print(type(student))
# for i in range(3):
#     print(student['student'][i]['name'], student['student'][i]['lastname'], student['student'][i]['year'],'-kurs', student['student'][i]['faculty'], 'talabasi')

with open('api-result.json', 'r') as file:
    result = json.load(file)
print(f"                            Title: {result['query']['pages']['13801']['title']}\nExtract: {result['query']['pages']['13801']['extract']}")
