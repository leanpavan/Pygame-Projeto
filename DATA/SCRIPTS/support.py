# imports
from csv import reader
from os import walk
import pygame

# imports self library
...

def import_csv_layout(path):

    with open(path) as level_map:
        terrain_map = []
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list

print("support.py loaded")
