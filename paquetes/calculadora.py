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
    