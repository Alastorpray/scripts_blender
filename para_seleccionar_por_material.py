import bpy

listobj = []
obj = bpy.context.visible_objects


for i in obj: 
    listobj.append(i.name)


for e in obj: #una iteración tomando como base maxima el numero de valores de nom_obj
    mtls = bpy.data.objects[e.name].material_slots #mtls es la variable que almacena el nombre de los materiales
    for h in mtls:
        if "M_crishtmas_ball" == h.name:
            e.select_set(True)

