# comparar datos de usuario y contraseña con blender

import urllib.request
import urllib.error
import json

def make_api_request(url):
    """Realiza una solicitud GET a la API."""
    try:
        with urllib.request.urlopen(url) as response:
            # Asumiendo que la respuesta es JSON
            response_data = response.read()
            return json.loads(response_data)
    except urllib.error.URLError as e:
        print(f"Error en la solicitud: {e}")
        return None

# Variables con las que quieres comparar
mi_idcliente = '3'
mi_name = 'Dicmar'
mi_token = 'df34d05a-deee-4c1c-a1d8-5807d9a8ad53'

# URL base de tu API
base_url = "https://service-rbt.koyeb.app/rbt/api/v1/rbt/"

# Consulta por idcliente
response_idcliente = make_api_request(base_url + mi_idcliente)

# Comparar los resultados con tus variables
if response_idcliente:
    # Suponiendo que la respuesta es un diccionario y tiene claves como 'idcliente', 'name', 'token'
    if response_idcliente.get('idcliente') == int(mi_idcliente) and response_idcliente.get('name') == mi_name and response_idcliente.get('token') == mi_token:
        print("Los datos coinciden con mis variables.")
    else:
        print("Los datos no coinciden.")
else:
    print("No se recibió respuesta de la API.")
