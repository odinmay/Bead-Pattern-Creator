import os
import csv
from PIL import Image


def generate_pattern(file_name):
    im = Image.open(os.getcwd() + '\\' + file_name)
    pixels = im.load()
    pixel_array = [[pixels[y,x] for y in range(im.width)] for x in range(im.height)]
    unique_colors = set()
    for row in pixel_array:
        for color in row:
            unique_colors.add(color)

    print(f'There are {len(unique_colors)} unique colors in this design')
    test_dict = {v: k for k, v in enumerate(unique_colors)}
    for row in pixel_array:
        for i, color in enumerate(row):
            row[i] = test_dict[color]

    with open('pattern.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(pixel_array)

