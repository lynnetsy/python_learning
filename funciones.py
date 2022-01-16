def saludo():
    print('hola mundo')

saludo()


def validar_edad(edad,nombre,sexo=None):
    if edad>=18:
        texto='%s es mayor de edad porque tiene %s años' % (nombre, edad)
    else:
        texto='%s no es mayor de edad, tiene %s años' % (nombre, edad)
        
    if sexo!= None:
        texto2='y su sexo es %s' %(sexo)
    else:
        texto2='su sexo no esta definido'

    print(texto)
    print(texto2)

age=15
name='lynnete'
validar_edad(age,name)
validar_edad(15,'pollo')
validar_edad(nombre='lalo',edad=30)
validar_edad(nombre='lala',edad=22,sexo='femenino')
validar_edad(nombre='lolo',edad=15,sexo='masculino')
validar_edad(19, 'amiibo', 'masculino')

def suma(num,num2):
    resultado=num+num2
    return resultado

resultado=suma(2,3)

print(suma(5,6))
print(resultado)

#Para hacer que una funcion reciba n cantidad de parametros 
#se utiliza la palabra *args y declaramos una función

def suma2(*args):
    resultado=0
    for numero in args:
        resultado+=numero

    return resultado

print(suma2(1,2,3,4))


def edad(anio):
    actual=2021
    edad=actual-anio
    return edad


n=int(input('dime tu anioo de nacimiento para calcular tu edad: '))

print('tu edad es %s'% (edad(n)))
    