import bpy
from mathutils import Vector, Quaternion

# objects to consider
targets = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

# camera object which defines ray source
cam = bpy.context.scene.camera

# save current view mode
mode = bpy.context.area.type

# set view mode to 3D to have all needed variables available
bpy.context.area.type = "VIEW_3D"

# get vectors which define view frustum of camera
frame = cam.data.view_frame(scene=bpy.context.scene)
topRight = frame[0]
bottomRight = frame[1]
bottomLeft = frame[2]
topLeft = frame[3]

# number of pixels in X/Y direction
resolutionX = int(bpy.context.scene.render.resolution_x * (bpy.context.scene.render.resolution_percentage / 100))
resolutionY = int(bpy.context.scene.render.resolution_y * (bpy.context.scene.render.resolution_percentage / 100))

# setup vectors to match pixels
xRange = [0.5*(topLeft[0]+topRight[0])]
yRange = [0.5*(topLeft[1]+bottomLeft[1])]

# create a list of tuples containing the mesh and its distance to the camera
mesh_distances = []
for target in targets:
    distance = (target.location - cam.location).length
    mesh_distances.append((target, distance))

# sort the list by distance
mesh_distances.sort(key=lambda x: x[1])

# iterate over all targets
empty_list = []
for mesh_distance in mesh_distances:
    target = mesh_distance[0]
    # calculate origin
    matrixWorld = target.matrix_world
    matrixWorldInverted = matrixWorld.inverted()
    origin = matrixWorldInverted @ cam.matrix_world.translation

    # variables to store closest hit
    closestHit = None
    closestDist = float('inf')

    # iterate over all X/Y coordinates
    for x in xRange:
        for y in yRange:
            # get current pixel vector from camera center to pixel
            pixelVector = Vector((x, y, topLeft[2]))

            # rotate that vector according to camera rotation
            pixelVector.rotate(cam.matrix_world.to_quaternion())

            # calculate direction vector
            destination = matrixWorldInverted @ (pixelVector + cam.matrix_world.translation) 
            direction = (destination - origin).normalized()

            # perform the actual ray casting
            hit, location, norm, face =  target.ray_cast(origin, direction)

            if hit:
                # check if this hit is closer than previous closest hit
                dist = (location - cam.matrix_world.translation).length
                if dist < closestDist:
                    closestDist = dist
                    closestHit = location

    # create an empty at the location of the closest hit
    if closestHit is not None:
        empty = bpy.data.objects.new("Empty", None)
        empty.location = matrixWorld @ closestHit
        bpy.context.scene.collection.objects.link(empty)
        empty_list.append(empty)

# remove all emptys except the closest one
closest_empty = min(empty_list, key=lambda empty: (cam.location - empty.location).length)
closest_empty.name = "gaaaaaaaaa"

for empty in empty_list:
    if empty != closest_empty:
        bpy.data.objects.remove(empty, do_unlink=True)

print("El empty más cercano a la cámara es:", closest_empty.name)

# reset view mode
bpy.context.area.type = mode

# print message to confirm completion
print("Done.")
