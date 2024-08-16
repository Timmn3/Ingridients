from sqlalchemy import Column, BigInteger, sql

from utils.db_api.db_gino import TimedBaseModel


class Ingredients(TimedBaseModel):
    __tablename__ = 'ingredients'
    number = Column(BigInteger, primary_key=True)
    coffee = Column(BigInteger)
    milk = Column(BigInteger)
    raf = Column(BigInteger)
    cacao = Column(BigInteger)
    glass = Column(BigInteger)
    cover = Column(BigInteger)
    syrup = Column(BigInteger)

    query: sql.select
