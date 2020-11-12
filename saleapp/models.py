from sqlalchemy import  Column, Integer, Float, String
from saleapp import db

class Category(db.Model):
    __tablename__ ="category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)