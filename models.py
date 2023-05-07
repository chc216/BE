from sqlalchemy import Column, Integer, String, Date

from .database import Base

class test(Base):
    __tablename__ = "test"
    geo_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    x = Column(Integer)
    y = Column(Integer)
    created_at = (Date)
    storage_URL = (String(500))
    comment = (String(500))
