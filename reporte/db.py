from sqlalchemy import create_engine

user = 'lyni'
password = 'secret'
host = 'mysql'
db_name = 'cucu'

engine = create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8mb4" % (user, password, host, db_name))

conn = engine.connect()
