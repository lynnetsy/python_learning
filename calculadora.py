def suma(*args):
    resultado=0
    for numero in args:
        resultado+=numero

    return resultado


def resta(*args):
    resultado=args[0]
    for numero in args[1:]:
        resultado-=numero
        
    return resultado


def multiplica(*args):
    resultado=1
    for numero in args:
        resultado*=numero
        
    return resultado


def divide(*args):
    resultado=args[0]
    for numero in args[1:]:
        resultado/=numero
    return resultado
    

print(suma(1,2,4))
print(resta(5,2,1))
print(multiplica(2,4,2))
print(divide(100,2,5))


##seleccion multiple ctrl d
### bloqnum apagado 7 para ir al inicio de una linea y 1 para ir al final
