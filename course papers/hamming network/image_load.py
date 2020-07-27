
from PIL import Image
import numpy as np


# "конвератирование" массива в массив из -1 и 1
def convert(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i, j] > 255/2:
                array[i, j] = -1
            else:
                array[i, j] = 1
    return array


# загрузка одного изображения
def load_image(pth):
    image = Image.open(pth)
    image = image.convert('L')
    return convert(np.array(image, dtype=int)).flatten()


# загрузка всех цифр
def load_digits():
    digits = []
    for i in range(10):
        digits.append(load_image('digits/{0}.jpg'.format(i)))
    return np.array(digits, dtype=int)
