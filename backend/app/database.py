from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgres://xlkhvfpjvayitv:c27c88f2ef43151f4d461b358b3dd1f904efb3ee04c7062da462f309369496c5@ec2-52-200-68-5.compute-1.amazonaws.com:5432/d8r6vspeqgl44t"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
