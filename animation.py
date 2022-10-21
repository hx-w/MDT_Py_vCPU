import time
import trimesh
import numpy as np


base_dir = 'src/models/highpoly/horse-poses/'
poses = [
    (
        f'horse-{i:02}.obj',
        trimesh.load(f'{base_dir}horse-{i:02}.obj')
    ) for i in range(1, 11)
]
pointer = 0

def animation(scene: trimesh.Scene):
    time.sleep(0.5)
    # delete old, add new
    global pointer
    if poses[pointer][0] in scene.geometry_identifiers.values():
        scene.delete_geometry(poses[pointer][0])
    
    pointer = (pointer + 1) % len(poses)
    scene.add_geometry(poses[pointer][1])


if __name__ == '__main__':
    anm_sc = trimesh.Scene([poses[0][1]])
    # open the scene viewer and move a ball around
    anm_sc.show(callback=animation)
