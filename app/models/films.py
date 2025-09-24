from ..database import Base
from sqlalchemy import Column, Integer, String, Float

class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    director = Column(String, index=True, nullable=False)
    year = Column(Integer, index=True, nullable=False)
    genre = Column(String, index=True, nullable=False)
    rating = Column(Float, index=True, nullable=False)