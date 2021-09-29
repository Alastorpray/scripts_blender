import bpy

outputFile = "C:/Users/Nevan/Desktop/Nueva carpeta/test.txt"

val = bpy.context.selected_objects
data =[]

for i in val:
    data.append(i.name)

f = open(outputFile, "w")
f.writelines("%s\n" % l for l in data)
f.close()