
import numpy as np
import image_load as il

from image_preprocessing import pre_proc


# аткивационная функция (для numpy массива):
def f(z):
    new_z = np.array([], dtype=int)
    for i in z:
        if i <= 0:
            new_z = np.append(new_z, 0)
        else:
            new_z = np.append(new_z, i)
    return new_z


# digits = il.load_digits()


def hamming_network_digits(pth, dgts):

    # ---| обучение |---
    w = 0.5 * dgts  # матрица весовых коэффициентов
    t = 256*256/2  # пороговая величина нейронов

    e = np.eye(10, dtype=float)  # значения синапсов обратных связей нейронов сети Хопфилда
    for i in range(10):
        for j in range(10):
            if i != j:
                e[i, j] = -1 / 20

    e_max = 0.1  # максимально допустимое значение нормы разности векторов выхода сети

    # ---| применение |---
    test = pre_proc(pth)  # с центрированием изображения
    # test = il.load_image(pth)  # без центрирования изображения

    s1 = []  # состояние нейронов первого слоя
    for i in range(10):
        s = 0
        for j in range(256*256):  # сумма
            s += w[i, j] * test[j]
        s1.append(s)
    s1 = np.array(s1) + t

    y1 = f(s1)  # значения выходов нейронов первого слоя
    y2 = y1  # выходы нейронов второго слоя

    while True:  # рекурсивное уточнение нейрона-победителя
        s2 = []
        for i in range(10):
            s = 0
            for j in range(10):  # сумма
                if j != i:
                    s += y2[j]
            s2.append(y2[i] - (1/20) * s)
        s2 = np.array(s2)
        y2t = f(s2)
        if np.linalg.norm(y2t - y2) < e_max:
            break
        y2 = y2t

    result = np.sign(y2)
    if np.sum(result) != 1:
        return 'не удалось однозначно распознать изобржение'
    else:
        return np.where(result == 1)[0][0]


# print(hamming_network_digits('digits/preprocessing_test.jpg', digits))
