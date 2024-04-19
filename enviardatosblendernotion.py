import bpy
import requests
import json

selected_objects = bpy.context.selected_objects
object_names = [obj.name for obj in selected_objects]
object_types = [obj.type for obj in selected_objects]
print("Nombres de Objetos Seleccionados:", object_names)


def create_notion_table(token, database_id, object_names, object_types):
    url = f'https://api.notion.com/v1/pages'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16"
    }

    for name, obj_type in zip(object_names, object_types):
        payload = {
            "parent": {"database_id": database_id},
            "properties": {
                "Name": {  # Nombre de la propiedad en Notion para el nombre del objeto
                    "title": [
                        {
                            "text": {
                                "content": name
                            }
                        }
                    ]
                },
                "Tipo": {  # Modificado para coincidir con el tipo de dato esperado en Notion
                    "rich_text": [
                        {
                            "text": {
                                "content": obj_type
                            }
                        }
                    ]
                }
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            print(f"Error: {response.json()}")

# Aquí puedes poner tus valores de token y database_id
token = "secret_ahT2xizWZgNzpf8LZi3e2EyRGMslMOAQDjWwYIySYDr"
database_id = "db250e716b6048059a3f03586a007ec1"
#object_names = ["Objeto1", "Objeto2"]  # Reemplaza esto con los nombres obtenidos de Blender
object_types = ["Mesh" for _ in object_names]
create_notion_table(token, database_id, object_names, object_types)
