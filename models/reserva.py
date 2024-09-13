from peewee import AutoField, ForeignKeyField, Model, DateField, TimeField
from config.database import database
from models.usuario import UsuarioDB
from models.mesa import MesaDB



class ReservaDB(Model):
    id_reserva = AutoField()
    usuario_id = ForeignKeyField(model=UsuarioDB, backref='reservas')
    mesa_id = ForeignKeyField(model=MesaDB, backref='avaliacoes')
    data_reserva = DateField()
    hora_reserva = TimeField()


    class Meta:
        database = database
        table_name = 'reservas'