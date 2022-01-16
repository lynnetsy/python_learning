from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


user = 'root'
password = 'secret'
host = 'mysql'
db_name = 'pets'

engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % (user, password, host, db_name))

conn = engine.connect()

Session = sessionmaker(bind=engine)
##En esta línea vamos a crear una sesion a la que se le pasa la conexion
#A la base de datos
session = Session()

Base = declarative_base()
#SQLALCHEMY me da la clase para conectar mis modelos a las bases de datos
#este es declarative_base()

