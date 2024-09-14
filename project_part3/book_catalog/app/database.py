from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://my_database_hb0p_user:8ZhoFcsAF2XetlIEBU7lkb5Ri5JJFhJH@dpg-crie34u8ii6s73f2cmn0-a.oregon-postgres.render.com/my_database_hb0p" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
