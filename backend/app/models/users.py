from backend.app.database import Base
from sqlalchemy import String, Integer, Column


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
