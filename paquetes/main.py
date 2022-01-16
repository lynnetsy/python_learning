import calculadora
from models import mascota
from menu import menu, saludame


def main():
    saludame('lalo')
    total = calculadora.suma(1,2,3,4)
    print(total)
    cucu = mascota('cucu', 'gato')
    cucu.status()

    playing = True
    while playing:
        opt = menu()
        if opt == 1:
            cucu.jugar()
        elif opt == 2:
            cucu.comer()
        elif opt == 3:
            cucu.hidratarse()
        elif opt == 4:
            cucu.status()
        elif opt == 5:
            playing = False


if __name__=='__main__':
    main()
