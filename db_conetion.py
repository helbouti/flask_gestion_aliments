<<<<<<< HEAD
from peewee import *
import datetime

db=SqliteDatabase("data.db",pragmas=[('foreign_keys', 'on')])

class BaseModel(Model):
    class Meta:
        database=db

class Producteur(BaseModel):
    username=CharField()
    tel=CharField(default="0")
    collecteur=CharField(default="")

class Moves(BaseModel):
    producteur=ForeignKeyField(Producteur,backref="moves",on_delete='CASCADE')
    moves_type=CharField(default="")
    note=TextField(default="")
    prix_u=FloatField(default=1)
    qtt=FloatField(default=0)
    moves_date=DateTimeField(default=datetime.datetime.now)

class Facture(BaseModel):
    producteur=ForeignKeyField(Producteur,backref="moves",on_delete='CASCADE')
    



def initialize():
    db.connect()
=======
from peewee import *
import datetime

db=SqliteDatabase("data.db",pragmas=[('foreign_keys', 'on')])

class BaseModel(Model):
    class Meta:
        database=db

class Producteur(BaseModel):
    username=CharField()
    tel=CharField(default="0")
    collecteur=CharField(default="")

class Moves(BaseModel):
    producteur=ForeignKeyField(Producteur,backref="moves",on_delete='CASCADE')
    moves_type=CharField(default="")
    note=TextField(default="")
    prix_u=FloatField(default=1)
    qtt=FloatField(default=0)
    moves_date=DateTimeField(default=datetime.datetime.now)



def initialize():
    db.connect()
>>>>>>> 064a1ad8fc32c26ea00738208d144939b52c8acd
    db.create_tables([Producteur,Moves],safe=True)