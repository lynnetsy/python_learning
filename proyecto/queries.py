from db import conn
from models import owners
def todos_los_usuarios():
    usuarios = conn.execute('select name, email from owners')
    print(usuarios)
    for usuario in owners:
        print('hola %s \n email: %s' % (usuario[0], usuario[1]))
