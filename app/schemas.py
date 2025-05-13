# app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# 좋아요 등록 요청용
class LikedSongCreate(BaseModel):
    track_id: str
    title: str
    artist: str
    genre: Optional[str] = None
    release_year: Optional[int] = None
    country: Optional[str] = None
    mood: Optional[str] = None
    user_id: Optional[str] = None  # 추후 로그인 기능용


# 조회 응답용 (DB에 저장된 liked_songs 레코드)
class LikedSongRead(BaseModel):
    id: int
    track_id: str
    title: str
    artist: str
    genre: Optional[str] = None
    release_year: Optional[int] = None
    country: Optional[str] = None
    mood: Optional[str] = None
    user_id: Optional[str] = None
    liked_at: datetime

    class Config:
        from_attributes = True  # SQLAlchemy 객체도 대응 가능하게 설정
