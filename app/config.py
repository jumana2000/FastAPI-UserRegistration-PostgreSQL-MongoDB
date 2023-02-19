from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import pymongo

DATABASE_URL = 'postgresql://postgres:12345@localhost:5432/python_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["python_db"]
profiles_collection = db["profile"]