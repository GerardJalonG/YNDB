# 🎬 MoviesAPI - API para gestionar películas y series
from fastapi import FastAPI

from .routes.films_endpoints import router as films_router

app = FastAPI(
    title="🎬 MoviesAPI",
    description="API para gestionar películas, series, watchlists y ratings",
    version="1.0.0"
)

app.include_router(films_router)

@app.get("/")
def home():
    """
    🏠 Página principal de la API
    """
    return {
        "mensaje": "¡Bienvenido a MoviesAPI! 🎬",
        "descripcion": "API para gestionar películas y series",
        "endpoints_disponibles": {
            "films": "/films - Gestionar películas",
            "docs": "/docs - Documentación interactiva"
        }
    }
