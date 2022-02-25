import bpy

outputFile = "/home/nevan/Documentos/test.txt"

obj = bpy.context.selected_objects

nombres = []
num = 0
info = {}
title = []
hijos = []
hijos_aux=[]

for i in obj:
    title.append(i.name)
    
    
for e in title:
    hijos = bpy.data.objects[e].children
    for h in hijos:
        hijos_aux = h.name

    info[e]= "[" + hijos_aux +"]"
    hijos_aux = []





with open(outputFile, "w") as f: # para escribir luego añadiremos "a" para agregar
    for key, value in info.items():    
      f.write("%s:%s\n" % (key, value)) #escribimos solo la propiedad nombre