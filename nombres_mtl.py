import bpy

obj = bpy.context.active_object
mtledit = []
mtlnormal = []
mtlfull = []

outputFile = "C:/Users/Nevan/Desktop/Nueva carpeta/test.txt"

val = bpy.context.active_object.material_slots

for i in val:
    if "_001" in i.name:
        mtledit.append(i.name + ' editable')
    else:
        mtlnormal.append(i.name)
mtlfull = mtledit + mtlnormal

f = open(outputFile, "w")
f.writelines("%s\n" % l for l in mtlfull)
f.close()