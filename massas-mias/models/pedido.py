from peewee import AutoField, CharField, ForeignKeyField, Model, DateField, TimeField
from config.database import database
from models.usuario import UsuarioDB
from models.prato import PratoDB



class PedidoDB(Model):
    id_pedido = AutoField()
    usuario_id = ForeignKeyField(model=UsuarioDB, backref='pedidos')
    prato_id = ForeignKeyField(model=PratoDB, backref='pedidos')
    status_pedido = CharField()
    data_pedido = DateField()
    hora_pedido = TimeField()


    class Meta:
        database = database
        table_name = 'pedidos'