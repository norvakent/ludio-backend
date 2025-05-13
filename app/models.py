# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LikedSong(Base):
    __tablename__ = "liked_songs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)  # 추후 OAuth 로그인 추가 시
    track_id = Column(String, index=True)  # Spotify나 자체 ID
    title = Column(String)
    artist = Column(String)
    genre = Column(String)
    release_year = Column(Integer)
    country = Column(String)
    mood = Column(String)
    liked_at = Column(DateTime, default=datetime.utcnow)

