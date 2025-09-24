
from app.database import Base, engine
from app.models.films import Film

def create_database():
    print("🔨 Creando la base de datos...")
    
    Base.metadata.create_all(bind=engine)
    
    print("✅ Base de datos creada exitosamente!")
    print("📍 Ubicación: app/database/movies.db")

if __name__ == "__main__":
    create_database()