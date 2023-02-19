from fastapi import APIRouter, HTTPException, Path, Depends, UploadFile
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import UserSchema, RequestUser, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create(request: RequestUser, profile_picture: UploadFile, db: Session = Depends(get_db)):
    crud.create_user(db, user=request.parameter, profile_picture=profile_picture)
    return Response(status="Ok", code="200", message="User created successfully").dict(exclude_none=True)

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _user = crud.get_user(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_user)

@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _user = crud.get_user_by_id(db, id)
    return Response(status="Ok", code="200", message="Success fetch data", result=_user).dict(exclude_none=True)
