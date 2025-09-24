from pydantic import BaseModel, Field
class FilmCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Título de la película")
    director: str = Field(..., min_length=1, max_length=100, description="Director de la película")
    year: int = Field(..., ge=1888, le=2030, description="Año de lanzamiento (desde 1888 hasta 2030)")
    genre: str = Field(..., min_length=1, max_length=50, description="Género de la película")
    rating: float = Field(..., ge=0.0, le=10.0, description="Calificación de 0.0 a 10.0")

    class Config:
        schema_extra = {
            "example": {
                "title": "El Padrino",
                "director": "Francis Ford Coppola", 
                "year": 1972,
                "genre": "Drama",
                "rating": 9.2
            }
        }

class FilmResponse(BaseModel):
    id: int
    title: str
    director: str
    year: int
    genre: str
    rating: float

    class Config:
        from_attributes = True