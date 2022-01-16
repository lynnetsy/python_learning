import xml.etree.ElementTree as ET

mytree = ET.parse('pets.xml')
pets = mytree.getroot()

info_pets = []
for pet in pets:      
    type = pet.find('Type')
    owner = pet.find('Owner')
    pet=pet.attrib
    pet['type'] = type.attrib['name']
    if owner is not None:
        pet['owner'] = owner.attrib['name']

    #Se hace un merge de diccionarios
    #pet.update(type.attrib)
    info_pets.append(pet)

print(info_pets)











lista = ['a', 'b', 'c', 'd']
tupla = ('a', 'b', 'c', 'd')
diccionario = { 'a': 0, 'b': 1, 'c': 2, 'd': 3}
dicc_2 = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd'}

print(lista[2])
print(tupla[1])
print(diccionario['d'])
print(dicc_2[0])

lista[2]= 'e'
print(lista)
diccionario['b'] = 10
print(diccionario)


diccionario['j'] = 10
print(diccionario)

print("--TUPLA--")
for item in tupla:
    print(item)

print("--LISTA--")
for item in lista:
    print(item)


print("--DICCIONARIO--")
for item in diccionario:
    print(diccionario[item])


print("--DICCIONARIO--")
for key, value in diccionario.items():
    print(key, value)

print(diccionario.items())


