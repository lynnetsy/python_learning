##TAREA 15/04/2021: EL USUARIO VA A INTRODUCIR UN NUMERO n
## Y TAMBIEN VA A INTRODUCIR LAS VECES QUE QUIEREN MULTIPLICAR EL NUMERO N

numero = int(input('que numero quieres calcular?'))
multiplicador = int(input('cuantas veces quieres multiplicarlo?'))
limite=multiplicador + 1

for i in range(0, limite):
    resultado = numero * i
    if i % 2 != 0:
        continue
    print('%s x %s = %s' % (numero, i, resultado))

    