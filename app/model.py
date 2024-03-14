from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DATETIME
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = "test_sensor"
    id = Column(Integer, primary_key=True, index=True)
    g = Column(String, nullable=False)
    col1 = Column(Integer)
    col2 = Column(Integer)
    col3 = Column(Integer)
    col4 = Column(Integer)
    col5 = Column(Integer)
    col6 = Column(Integer)
    col7 = Column(Integer)
    col8 = Column(Integer)
    col9 = Column(String)
    data_hora_post = Column(DATETIME)

