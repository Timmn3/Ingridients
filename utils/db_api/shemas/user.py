from sqlalchemy import Column, BigInteger, String, sql, Float

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    referral_id = Column(BigInteger)
    status = Column(String(30))
    balance = Column(Float)

    query: sql.select
