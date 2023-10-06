import numpy as np
from PIL import Image
import random


def generate_array(path="art.jpg"):
    pillow_img = Image.open(path)
    color_array = np.array(pillow_img)
    return color_array


def get_random_code(colour_array, range_num):
    codes = []
    for lst1 in colour_array:
        for lst2 in lst1:
            codes.extend(lst2)
    non_white_codes = [code for code in codes if code > 100]

    random_color_codes = [random.choice(non_white_codes) for num in range(range_num)]

    return random_color_codes




