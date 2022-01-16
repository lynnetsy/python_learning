def menu():
    opt = input("""
Introduce un numero:
1.Jugar
2.Comer
3.Beber agua
4.Cuentame de ti
5.Salir
    """)
    return int(opt)

def saludame(nombre):
    print('Hola %s\n' % (nombre))
    