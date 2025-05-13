# app/routes/liked.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app import schemas, crud, models
from app.db import SessionLocal

router = APIRouter(prefix="")


# 의존성 주입: DB 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST /like : 좋아요 추가
@router.post("/like", response_model=schemas.LikedSongRead)
def like_song(song: schemas.LikedSongCreate, db: Session = Depends(get_db)):
    return crud.create_liked_song(db, song)


# GET /queue : 필터링된 좋아요 곡 큐 조회
@router.get("/queue", response_model=List[schemas.LikedSongRead])
def get_queue(
    genre: Optional[str] = None,
    release_year: Optional[int] = None,
    country: Optional[str] = None,
    mood: Optional[str] = None,
    artist: Optional[str] = None,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    return crud.get_liked_songs(
        db,
        genre=genre,
        release_year=release_year,
        country=country,
        mood=mood,
        artist=artist,
        limit=limit
    )
