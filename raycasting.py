import bpy
from mathutils import Vector

# get all mesh objects in the scene
mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

# camera object which defines ray source
cam = bpy.data.objects['Camera']

# save current view mode
mode = bpy.context.area.type

# set view mode to 3D to have all needed variables available
bpy.context.area.type = "VIEW_3D"

# get view vector from camera
view_vector = cam.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))

# generate multiple ray directions
ray_directions = [cam.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))] * 10

# initialize a variable to keep track if an intersection has been found
intersection_found = False

# initialize a list to keep track of distances to objects
distances = []

# iterate over all mesh objects in the scene
for obj in mesh_objects:
    # calculate distance from camera to object
    distance = (cam.location - obj.location).length
    distances.append((distance, obj))

# sort objects by distance from camera
distances.sort(key=lambda x: x[0])

# iterate over all objects sorted by distance
for distance, obj in distances:
    # iterate over all ray directions
    for direction in ray_directions:
        # calculate origin vector
        matrix_world = obj.matrix_world
        matrix_world_inverted = matrix_world.inverted()
        origin = matrix_world_inverted @ cam.matrix_world.translation
        
        # perform the actual ray casting
        hit, location, normal, face = obj.ray_cast(origin, direction)
        
        if hit and not intersection_found:
            # create an empty node at intersection point
            empty = bpy.data.objects.new("Empty", None)
            empty.location = matrix_world @ location
            bpy.context.scene.collection.objects.link(empty)
            print("Intersection at", empty.location)
            intersection_found = True
            break

    # check if an intersection was found and exit the loop
    if intersection_found:
        break

# create an empty node at the camera position
cam_empty = bpy.data.objects.new("Cam_Empty", None)
cam_empty.location = cam.location
bpy.context.scene.collection.objects.link(cam_empty)

# reset view mode
bpy.context.area.type = mode


#----------------MODIFICACION----------------------------

import bpy
from mathutils import Vector

# get all mesh objects in the scene
mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

# camera object which defines ray source
#cam = bpy.data.objects['Camera']

cam = bpy.context.active_object
if cam.type == 'CAMERA':


    # save current view mode
    mode = bpy.context.area.type

    # set view mode to 3D to have all needed variables available
    bpy.context.area.type = "VIEW_3D"

    # get view vector from camera
    view_vector = cam.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))

    # generate multiple ray directions
    ray_directions = [cam.matrix_world.to_quaternion() @ Vector((0.0, 0.0, -1.0))] * 10

    # initialize a variable to keep track if an intersection has been found
    intersection_found = False

    # initialize a list to keep track of distances to objects
    distances = []

    # iterate over all mesh objects in the scene
    for obj in mesh_objects:
        # calculate distance from camera to object
        distance = (cam.location - obj.location).length
        distances.append((distance, obj))

    # sort objects by distance from camera
    distances.sort(key=lambda x: x[0])

    # iterate over all objects sorted by distance
    for distance, obj in distances:
        # iterate over all ray directions
        for direction in ray_directions:
            # calculate origin vector
            matrix_world = obj.matrix_world
            matrix_world_inverted = matrix_world.inverted()
            origin = matrix_world_inverted @ cam.matrix_world.translation
            
            # perform the actual ray casting
            hit, location, normal, face = obj.ray_cast(origin, direction)
            
            if hit and not intersection_found:
                # create an empty node at intersection point
                empty = bpy.data.objects.new("Empty", None)
                empty.location = matrix_world @ location
                bpy.context.scene.collection.objects.link(empty)
                print("Intersection at", empty.location)
                intersection_found = True
                break

        # check if an intersection was found and exit the loop
        if intersection_found:
            break

    # create an empty node at the camera position
    cam_empty = bpy.data.objects.new("Cam_Empty", None)
    cam_empty.location = cam.location
    bpy.context.scene.collection.objects.link(cam_empty)

    # reset view mode
    bpy.context.area.type = mode

else:
    print("selecciona una camara")