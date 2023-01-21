from app import db
from sqlalchemy import Column, Integer, String, Float, Text, Boolean

class ProductosModel(db. Model):
    __tablename__= 'productos'

    id =Column(Integer, primary_key=True, autoincrement=True)
    nombre= Column(String(45),nullable=False)
    precio = Column(Float, nullable=False)
    imagen = Column(Text, nullable=False)
    estado = Column(Boolean, default=True)

    def _init__(self, nombre, precio, imagen, estado) -> None:
        self.nombre = nombre
        self.preccio= precio
        self.imagen= imagen
        self.estado= estado