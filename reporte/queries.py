from db import conn

def todos_los_usuarios():
    usuarios = conn.execute('select name, last_name from usuarios')
    print(usuarios)
    for usuario in usuarios:
        print('hola %s %s' % (usuario[0], usuario[1]))
