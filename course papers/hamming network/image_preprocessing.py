
import numpy as np
from PIL import Image
import image_load as il


def pre_proc(path):
    image = Image.open(path)
    image = image.convert('L')
    image_as_npm = il.convert(np.array(image, dtype=int))

    one_pos = np.where(image_as_npm == 1)
    if list(one_pos[0]):
        y0 = one_pos[0][0]
        y1 = one_pos[0][-1]
    else:
        y0 = 2
        y1 = 254
    if list(one_pos[1]):
        x0 = min(one_pos[1])
        x1 = max(one_pos[1])
    else:
        x0 = 2
        x1 = 254

    # координаты текущего центра:
    c_x = int((x0 + x1) / 2)
    c_y = int((y0 + y1) / 2)

    # сдвиг:
    dx = c_x - 127
    dy = c_y - 127

    # сдвиг изначальной картинки:
    new_image_as_npm = -np.ones((256, 256))
    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            if image_as_npm[i, j] == 1:
                new_image_as_npm[i - dy, j - dx] = 1

    return new_image_as_npm.flatten()


# print(pre_proc('digits/new_test_1.jpg'))
