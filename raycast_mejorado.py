import bpy
from mathutils import Vector, Quaternion

# objects to consider
targets = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

# camera object which defines ray source
cam = bpy.data.objects['camera']

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

# variables to store the closest distance and empty object
closest_distance = float('inf')
closest_empty = None

# iterate over all targets
for target in targets:
    # calculate origin
    matrixWorld = target.matrix_world
    matrixWorldInverted = matrixWorld.inverted()
    origin = matrixWorldInverted @ cam.matrix_world.translation

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
                # check if this hit is closer than the previous closest hit
                distance = (cam.location - location).length
                if distance < closest_distance:
                    # update closest distance and closest empty object
                    closest_distance = distance

                    # create an empty at the location of the hit
                    if closest_empty:
                        bpy.data.objects.remove(closest_empty, do_unlink=True)
                    closest_empty = bpy.data.objects.new("Empty", None)
                    closest_empty.location = matrixWorld @ location
                    bpy.context.scene.collection.objects.link(closest_empty)

# reset view mode
bpy.context.area.type = mode

print("Done.")
