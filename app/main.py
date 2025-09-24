from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def leer_raiz():
    """
    Esta función se ejecuta cuando alguien visita la raíz de nuestra API
    """
    return {"mensaje": "¡Hola! Esta es mi primera API"}
