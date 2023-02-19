from sqlalchemy.orm import Session
from sqlalchemy import or_
from models import User, Profile
from schemas import UserSchema, ProfileSchema, RequestProfile, RequestUser
from fastapi import HTTPException, UploadFile
import os
import uuid
from config import profiles_collection


def get_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: RequestUser, profile_picture: UploadFile):
    try:
        user_data = user.parameter.dict()
        email = user_data.get('email')
        phone = user_data.get('phone')
        if db.query(User).filter(or_(User.email == email, User.phone == phone)).first():
            raise HTTPException(status_code=400, detail="Email or Phone already registered")
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        filename = str(uuid.uuid4()) + "." + profile_picture.filename.split(".")[-1]
        with open(os.path.join("profiles", filename), "rb") as f:
            file_content = f.read()
        file_id = profiles_collection.insert_one(file_content).inserted_id

        profile = Profile(user_id=user.id, profile_picture=str(file_id))
        db.add(profile)
        db.commit()
        db.refresh(profile)

    except Exception as e:
        db.rollback()
        raise e


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

