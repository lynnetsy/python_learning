from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship





class Owner(db.Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def register_owner(self):
        self.name = input('Introduce tu nombre con el que deseas registrarte:\n')
        self.email = input('Introduce tu email:\n')
    
    def save(self):
        db.session.add(self.name, self.email)
        db.session.commit()


    