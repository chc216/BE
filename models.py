from sqlalchemy import Column, Integer, VARCHAR, DateTime

from.database import Base

class Test(Base):
    __tablename__ = "test"
    geo_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    x = Column(Integer)
    y = Column(Integer)
    created_at = (DateTime)
    storage_URL = (VARCHAR(500))
    comment = (VARCHAR(500))
