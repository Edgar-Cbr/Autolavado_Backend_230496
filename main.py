from fastapi import FastAPI
from routes import routes_rol, routes_user, routes_auto, routes_services, routes_auto_servicio

app = FastAPI(
    title="Autolavado Backend",
    description="API para gestionar autos, servicios y usuarios del autolavado",
    version="1.0.0"
)

# Incluir routers
app.include_router(routes_rol.router)
app.include_router(routes_user.router)
app.include_router(routes_auto.router)
app.include_router(routes_services.router)
app.include_router(routes_auto_servicio.router)

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la API del Autolavado",
        "version": "1.0.0",
        "endpoints": {
            "roles": "/roles",
            "usuarios": "/usuarios",
            "autos": "/autos",
            "servicios": "/servicios",
            "auto-servicios": "/auto-servicios"
        }
    }