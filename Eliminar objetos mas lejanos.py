camera = bpy.context.scene.camera

# Crear un diccionario para almacenar las posiciones de los empties
empty_positions = {}

# Recorrer todos los empties en la escena
for empty in bpy.context.scene.objects:
    if empty.type == 'EMPTY':
        # Obtener la posición del empty
        position = empty.location
        # Almacenar la posición en el diccionario
        empty_positions[empty.name] = position
        # Obtener la distancia entre la cámara y el empty
        distance = (camera.location - position).length
        # Imprimir el nombre del empty y la distancia a la cámara
        print(empty.name, distance)

# Obtener el empty más cercano a la cámara
closest_empty = min(empty_positions, key=lambda k: (camera.location - empty_positions[k]).length)

# Imprimir el nombre del empty más cercano a la cámara
print("El empty más cercano a la cámara es:", closest_empty)