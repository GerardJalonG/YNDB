from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.films import Film
from ..schemas.films import FilmCreate, FilmResponse

router = APIRouter(
    prefix="/films",
    tags=["Películas"]
)

@router.post("/", response_model=FilmResponse, status_code=status.HTTP_201_CREATED)
def create_film(film_data: FilmCreate, db: Session = Depends(get_db)):
    
    new_film = Film(
        title=film_data.title,
        director=film_data.director,
        year=film_data.year,
        genre=film_data.genre,
        rating=film_data.rating
    )
    
    db.add(new_film)
    
    try:
        db.commit()
        db.refresh(new_film)
        
        return new_film
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear la película: {str(e)}"
        )

@router.get("/", response_model=List[FilmResponse])
def get_all_films(db: Session = Depends(get_db)):
    films = db.query(Film).all()
    return films