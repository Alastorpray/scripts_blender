import bpy

outputFile = "/home/nevan/Documentos/test.txt"

obj = bpy.context.selected_objects

with open(outputFile, "w") as f: # para escribir luego añadiremos "a" para agregar
    for i in obj:    
      f.write("%s\n" % i.name) #escribimos solo la propiedad nombre