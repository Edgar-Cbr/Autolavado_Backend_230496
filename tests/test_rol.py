# from fastapi.testclient import TestClient
# from main import app

# # Creamos un cliente de prueba a partir de nuestra aplicación FastAPI
# client = TestClient(app)

# def test_read_roles():
#     # Hacemos una petición GET a la ruta /rol/
#     response = client.get("/rol/")
    
#     # Comprobamos que el código de estado sea 200 (OK)
#     assert response.status_code == 200
    
#     # Comprobamos que la respuesta sea una lista (ya que devuelve List[schemas.schema_rol.Rol])
#     data = response.json()
#     assert isinstance(data, list)
