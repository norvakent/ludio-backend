# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional


def create_liked_song(db: Session, song: schemas.LikedSongCreate) -> models.LikedSong:
    db_song = models.LikedSong(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def get_liked_songs(
    db: Session,
    genre: Optional[str] = None,
    release_year: Optional[int] = None,
    country: Optional[str] = None,
    mood: Optional[str] = None,
    artist: Optional[str] = None,
    limit: int = 50
) -> List[models.LikedSong]:
    query = db.query(models.LikedSong)

    if genre:
        query = query.filter(models.LikedSong.genre == genre)
    if release_year:
        query = query.filter(models.LikedSong.release_year == release_year)
    if country:
        query = query.filter(models.LikedSong.country == country)
    if mood:
        query = query.filter(models.LikedSong.mood == mood)
    if artist:
        query = query.filter(models.LikedSong.artist == artist)

    return query.order_by(models.LikedSong.liked_at.desc()).limit(limit).all()
