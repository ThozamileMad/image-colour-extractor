import numpy as np
from PIL import Image
from collections import Counter


def generate_array(path):
    pillow_img = Image.open(path)
    color_array = np.array(pillow_img)
    return color_array


def get_common_codes(colour_array, range_num):
    codes = []
    for lst1 in colour_array:
        for lst2 in lst1:
            codes.extend(lst2)
    none_white_codes = [code for code in codes if code > 100]
    most_common = Counter(none_white_codes).most_common()[:range_num]

    return most_common






