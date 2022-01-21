import datetime

from backend.app.database import Base
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey


class Meet(Base):
    __tablename__ = 'meets'

    id = Column(Integer, primary_key=True, index=True)
    join_code = Column(String, index=True, unique=True)
    create_date = Column(DateTime, default=datetime.datetime.utcnow())


class MeetUser(Base):
    __tablename__ = 'meet_user'

    meet_id = Column(Integer, ForeignKey('meets.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
