from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone = Column(String)

    profiles = relationship("Profile", back_populates="user")
    

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    profile_picture = Column(String)

    user = relationship("User", back_populates="profiles")
