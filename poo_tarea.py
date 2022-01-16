class mascota():
    nombre = None
    color = None
    especie = None
    hambre = 0
    sed = 0
    diversion = 0
    energia = 0
    def __init__(self, nombre):
        self.nombre = nombre
        print('Hola por fin nos vemos! Soy %s' %(self.nombre))
    
    def decir_nombre(self):
        self.nombre = input('\n Empecemos ponle un nombre a tu mascota!\n')

    def decir_especie(self):
        self.especie = input('Empecemos\n ¿Que animal deseas que sea %s?\n' %(self.nombre))

    def menu_inicio(self):
        print('Empecemos con las necesidades basicas de %s \n' %(self.nombre))
        print('Del 1 al 10 mediremos los niveles de diversion, hambre y sed de %s' %(self.nombre))
        self.energia=int(input('\n¿Cuanta energía tendrá %s?\n' %(self.nombre)))
        self.hambre=int(input('\n¿Cuanta hambre tendrá %s?\n' %(self.nombre)))
        self.sed=int(input('\n¿Cuanta sed tendrá %s?\n' %(self.nombre)))
        self.diversion=int(input('\n¿Cuanta diversión tendrá %s?\n' %(self.nombre)))

    def menu_actividades(self):
        print('\nActividades\n')
        opcion=input('\nPresiona 1 para darme de comer\n\nPresiona 2 para jugar conmigo\n\nPresiona 3 para mandarme a dormir\n\nPresiona 4 para darme agua\n\nPresiona 5 para ver mis estadisticas actuales\n\n')
        if opcion =='1':
            self.comer()
        elif opcion =='2':
            self.jugar()
        elif opcion =='3':
            self.dormir()
        elif opcion =='4':
            self.hidratacion(self.sed)
        elif opcion =='5':
            self.estadisticas()
        else:
            print('Escoge una de las 3 opciones\n')
            self.menu_actividades()
 
    def estadisticas(self):
        print('\n\nMis necesidades han cambiado a:\n\n')
        print('\n\nMi nivel de hambre esta en %s\n' %(self.hambre))
        print('\n\nMi nivel de hidratacion esta en %s\n' %(self.sed))
        print('\n\nMi nivel de sueño esta en %s\n' %(self.energia))
        print('\n\nMi nivel de diversion esta en %s\n' %(self.diversion))
        self.menu_actividades()
    def jugar(self):
            if self.diversion> 10:
                print('Ya no quiero jugar, ha sido demasiado')
                self.menu_actividades()
            else:
                jueguito=input('Juguemos!! Presiona Y para jugar conmigo\n')
                if jueguito =='Y':
                    print('gracias por jugar conmigo')
                    jueguito=2
                    self.diversion+=jueguito
                    self.hambre-=jueguito
                    self.sed-=jueguito
                    self.energia-=jueguito
                    print('Mi nivel de diversion esta en %s gracias a ti!!' %(self.diversion))
                    n=input('Seguimos jugando? Presiona 1 para continuar jugando\n')
                    if n == '1':
                        self.jugar()
                    else:
                        print('Que podemos hacer?')
                        self.menu_actividades()
                else:
                    print('Que podemos hacer?')
                    self.menu_actividades()

    def comer(self):
        if self.hambre >= 10: 
            print('Gracias pero no tengo hambre\n\n')
            print('\n\n\n')
            self.menu_actividades()
        elif self.hambre < 10:
            comidita=input('\n\nPresiona 1 para darme de comer\n\n')
            if comidita == '1':
                incremento=2
                self.hambre+=incremento
                self.diversion-=incremento
                self.energia-=incremento
                self.sed-=incremento
                print('Gracias! a ti mi hambre ahora esta en %s de 10\n\n' %(self.hambre))
                opcion=input('\n\n¿Quieres volver a darme de comer?\n\nPresiona 2\n\n')
                if opcion == '2':
                    self.comer()
                else:
                    print('\n\nEsta bien! Veamos que mas podemos hacer\n\n')
                    self.menu_actividades()
            else:
                    print('\n\nEsta bien! Veamos que mas podemos hacer\n\n')
                    self.menu_actividades()
        else: 
            print('\n\nIntroduce un valor del 1 al 10 para poder darme de comer!!\n\n')

    def hidratacion(self, sed):
        if self.sed < 10:
            print('\n\nPff tengo mucha sed!\n\n')
            opcion=input('\n\nPresiona 1 para darme agua\n\n')
            if opcion == '1':
                incremento=10
                self.sed=incremento
                print('\n\nMuchas gracias! Ya no tengo sed, mi nivel de hidratacion es %s' %(self.sed))
                self.menu_actividades()
            else:
                opciones=input('\n\n¿Te habras equivocado de boton?\n\nSelecciona una opcion:\n\n1.Darme agua\n\n2.Hacer otra cosa\n\n')
                if opciones == '1':
                    self.sed()
                elif opciones == '2':
                    self.menu_actividades()
        else:
                ('\n\nVeamos que mas podemos hacer\n\n')
                self.menu_actividades()

    def dormir(self):
        if self.energia in range(0,3):
            print('Muero de sueño\nZzZzZz\nZzZzZz\nZzZzZz\n')
            print('\nZzZzZz\nZzZzZz\nZzZzZz\n')
            self.menu_dormir()
        elif self.energia in range(4,9):
            print('No tengo tanto sueño pero una siesta no me caera mal\nZzZzZz\nZzZzZz\nZzZzZz\n')
            self.menu_dormir()
        else:
            print('No quiero dormir, hagamos otra cosa\n\n\n\n\n')
            self.menu_actividades()
    
    def menu_dormir(self):
        a_dormir=input('Quieres que duerma un poco?\n\nPresiona 1 para ponerme a dormir\n\n')
        if a_dormir =='1':
            incremento=2
            self.energia+=incremento
            print('Gracias a ti mi energía esta en %s de 10!!' %(self.energia))
            segundavuelta=input('\n\nPresiona 1 para volver a dormir\n\n')
            if segundavuelta == '1' and self.energia < 10:
                self.menu_dormir()
            else:
                print('\n\nOk hagamos otra cosa\n\n')
                self.menu_actividades()
        else:
            print('\n\nOk hagamos otra cosa\n\n')
            self.menu_actividades()


       




ejemplo = mascota('cucu')

ejemplo.menu_actividades()
