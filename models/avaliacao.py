from peewee import AutoField, ForeignKeyField, Model, DateField, TimeField, IntegerField, TextField
from config.database import database
from models.usuario import UsuarioDB



class AvaliacaoDB(Model):
    id_avaliacao = AutoField()
    estrela_avaliacao = IntegerField()
    usuario_avaliacao = TextField()
    usuario_id = ForeignKeyField(model=UsuarioDB, backref='avaliacoes')
    data_avaliacao = DateField()
    hora_avaliacao = TimeField()


    class Meta:
        database = database
        table_name = 'avaliacoes'