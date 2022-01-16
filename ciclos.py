tupla=('a','b','c','d','e')
for letra in tupla:
    print(letra)

lista=[1,2,3,4,5,6]
diccionario={'a':1,'b':2,'c':3}
string='hola mundo'

for numero in lista:
    print(numero)

for letra in diccionario:
    print(letra, diccionario[letra])

#se utiliza el metodo .items
for indice, valor in diccionario.items():
    print(indice, valor)

for letra in string:
    print(letra)

for numero in range(0, 4):
    print('me estoy iterando por %s' % (numero))

for n in range(0,11):
    if not n%2==0: 
        continue  #sirve para saltarse a la siguiente iteracion
    print('%s es par' % n)

for n in range(0,11):
    if n>5:
        break    #sirve para detener el ciclo
    print('%s es menor que 6' % n)

for n in range(0,4):
    print(n)
else: ##se puede ejecutar el else aunque simplemente indexandolo a lado del for se hace lo mismo 
    print('ya se termino el for')

#asi:
#print('ya se termino el for')

i=0
while i<11:
    print(i)
    i+=2        # i = i + 2



