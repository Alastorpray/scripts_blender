import bpy


outputFile = "C:/Users/Nevan/Desktop/Nueva carpeta/test.txt"

obj = bpy.context.selected_objects
nom_obj = []
nom_mtls = []
obj_dic = {}
mtls = []
aux_mtl=[]

for i in obj:
    nom_obj.append(i.name) #almacenamos los nombres de los objetos de los cuales extraeremos el nombre de los materiales que contiene

for e in nom_obj: #una iteración tomando como base maxima el numero de objetos seleccionados de nom_obj
    mtls = bpy.data.objects[e].material_slots #mtls es la variable que almacena el nombre de los materiales
    for h in mtls:
        if "web" in h.name:
            aux_mtl.append(h.name + " TEXTURA EDITABLE")
        elif "logo" in h.name:
            aux_mtl.append(h.name + " TEXTURA EDITABLE")
        elif "P_" in h.name:
            aux_mtl.append(h.name + " TEXTURA EDITABLE")
        elif "_0" in h.name:
            aux_mtl.append(h.name + " COLOR EDITABLE")
        else:
            aux_mtl.append(h.name)
    aux_mtl = sorted(aux_mtl, key=lambda l: l[-1])        
    obj_dic[e]=aux_mtl
    aux_mtl = []   



with open(outputFile, "w") as f: # para escribir luego añadiremos "a" para agregar
    for key, value in obj_dic.items():    
        f.write("%s:%s\n" % (key, value))