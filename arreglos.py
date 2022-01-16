# LISTAS, TUPLAS, DICCIONARIOS

# Las listas en python son similares a los arreglos
# en otros lenguajes de programación, estos pueden
# contener cualquier cantidad de elementos y pueden
# ser de cualquier tipo y para acceder a ellos, se
# utiliza un indice y se inicializa en 0

lista_vacia=[]
lista_super=['tortillas', 'tomates', 'cebollas']
lista_multi_tipos=['hola', 1, 1.4, False]
print(lista_multi_tipos)

# acceder a un valor dentro de la list
flotante=lista_multi_tipos[2]
print(flotante)

# para asignar un valor a un indice en una lista
# se hace de la siguiente forma
lista_multi_tipos[2]=3.14
print(lista_multi_tipos)

# las tuplas son muy similares a las listas solo que estas
# no pueden ser modificadas :( 
tupla=(1, 2, 3, 4)
print(tupla)

# Diccionarios son similares a las listas solo que el indice 
# puede ser definido de forma explicita

diccionario={'a': 1, 'b': 2, 'c': 3}
diccionario['d']= 4
print(diccionario)
print(diccionario['b'])

# Para eliminar elementos de un diccionario o una lista
# se pueden utilizar del o el método pop

numeros=[1, 2, 3, 4, 5, 6]
del numeros[2]
print(numeros)

letras=['a', 'b', 'c', 'd', 'e', 'f']
letra=letras.pop(2)
print(letras)
print(letra)

# Agregar elementos a una lista
# .append() sirve para agregar elementos al final de la lista
# .insert() sirve para agregar elementos en el indice definido,
# el primer valor es el indice y el segundo el valor a asignar
# .insert(indice, valor)
numeros.append(7)
print(numeros)

numeros.insert(2,3)
print(numeros)


##TAREA CREAR UN DICCIONARIO DE 3 PALABRAS ASOCIADAS QUE NO 
##ESTEN EN EL DICCIONARIO PERO SE USEN DIA A DIA ASI COMO MIJO, CARNAL, COMPA
##ADEMAS UNA LISTA PARA LOS INGREDIENTES PARA UN PASTEL
## Y UNA TUPLA CON LOS NUMEROS DE PI SEPARADOS POR INDICE

diccionario_tarea={'huelesaobo': 'es un albur de que sobas la vagina o el pene','carnal': 'asi le dicen a un amigo o a alguien cercano','chale': 'es una palabra que se puede usar para expresar decepcion'}
tupla_tarea=(3,'.',1,4,1,5,9,2)
lista_tarea=['harina', 'huevo', 'leche', 'mantequilla', 'chocolate']

print('esto es el diccionario', '\n' , diccionario_tarea, '\n')
print('esta es la tupla', '\n', tupla_tarea, '\n')
print( 'esta es la lista','\n',lista_tarea,)