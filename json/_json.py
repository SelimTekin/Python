# ----------------------- Farklı platformlar arası veri alışverişi -----------------------

import json

person_string = '{"name": "Selim", "languages":["python", "C#"], "surname":"Tekin", "a":"b"}' # Bu stringi json ile dictionary ' e döndürücez
person_dict = {"name": "Selim","languages":["python", "C#"]}
# JSON string to dictionary
# result = json.loads(person_string) # {'name': 'Selim', 'languages': ['python', 'C#']}
# result = result["name"] # Selim
# result = result["languages"] # ['python', 'C#']

# Dosyadan JSON bilgi okuma
# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])              # Selim
#     print(data["languages"])              # ['python', 'C#']


# Dictionary to JSON string

# result = json.dumps(person_dict)
# print(type(result)) # str
# print(result)
# print(result["name"]) # ulaşamayız hata verir çünkü artık bir string dictionary değil

# Dosyaya yazma
# with open("person.json", "w") as f:
#     json.dump(person_dict, f)7


person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent=4, sort_keys=True) # sort_keys=True alfabetik sıralıyor, indent girinti oluyor
print(person_dict)
print(result)