import numpy as np
import matplotlib.pyplot as plt

import model_visualization as mymodel_vis
import model_analysis as mymodel_an


default_v_max = 5
default_p_brake = 0.2

# m_p = [3600, np.array([]), 10820, 5, 0.2, [[1000, 1020]], [[1021, 1820]], 1, [], t]
# get_steps(n, array, road_len, v_max, p_brake, convergence_zone=0, obstruction_zone=0, aadd=0, addit_cars=[], random_addition=0)
def model_an(v_max, p_brake):
    points_avv_all, points_avv_conv, points_avv_obstr = [], [], []
    points_d_all, points_d_conv, points_d_obstr = [], [], []
    for t in range(10, 501):
        print('quantity of cars is {0}'.format(t))  # delete it
        steps = mymodel_vis.get_steps(3600, np.array([]), 10820, v_max, p_brake, [[1000, 1020]], [[1021, 1820]], 1, [], t)
        # average v
        points_avv_all.append([t, mymodel_an.average_v_global(steps[1:])])
        points_avv_conv.append([t, mymodel_an.average_v_conv(steps[1:], [[1000, 1020]])])
        points_avv_obstr.append([t, mymodel_an.average_v_obstr(steps[1:], [[1021, 1820]])])
        # density
        points_d_all.append([t, mymodel_an.density_global(steps[1:])])
        points_d_conv.append([t, mymodel_an.density_conv(steps[1:], [[1000, 1020]])])
        points_d_obstr.append([t, mymodel_an.density_obstr(steps[1:], [[1021, 1820]])])
    return [points_avv_all, points_avv_conv, points_avv_obstr, points_d_all, points_d_conv, points_d_obstr]


def data_sum(all_pieces):
    all_p = []
    for i in range(6):
        all_p.append()

# data = model_an(default_v_max, default_p_brake)


v = np.transpose(data[0])
x0 = v[0]
y0 = v[1]
v = np.transpose(data[1])
x1 = v[0]
y1 = v[1]
v = np.transpose(data[2])
x2 = v[0]
y2 = v[1]
v = np.transpose(data[3])
x3 = v[0]
y3 = v[1]
v = np.transpose(data[4])
x4 = v[4]
y4 = v[4]
v = np.transpose(data[5])
x5 = v[5]
y5 = v[5]


fig = plt.figure()

ax0 = fig.add_subplot(231)
ax1 = fig.add_subplot(232)
ax2 = fig.add_subplot(233)
ax3 = fig.add_subplot(234)
ax4 = fig.add_subplot(235)
ax5 = fig.add_subplot(236)

ax0.scatter(x0, y0)
ax0.set_title('Вся дорога')
ax0.set_xlabel('Количество машин')
ax0.set_ylabel('Средняя скорость')

ax1.scatter(x1, y1)
ax1.set_title('Зона сужения')
ax1.set_xlabel('Количество машин')
ax1.set_ylabel('Средняя скорость')

ax2.scatter(x2, y2)
ax2.set_title('Зона с заблокированной полосой')
ax2.set_xlabel('Количество машин')
ax2.set_ylabel('Средняя скорость')

ax3.scatter(x3, y3)
# ax3.set_title('Вся дорога')
ax3.set_xlabel('Количество машин')
ax3.set_ylabel('Плотность машин')

ax4.scatter(x4, y4)
# ax4.set_title('Зона сужения')
ax4.set_xlabel('Количество машин')
ax4.set_ylabel('Плотность машин')

ax5.scatter(x5, y5)
# ax5.set_title('Зона с заблокированной полосой')
ax5.set_xlabel('Количество машин')
ax5.set_ylabel('Плотность машин')


plt.show()
