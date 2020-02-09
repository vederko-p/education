import numpy as np

import model_visualization as mymodel_vis
import model_analysis as mymodel_an


default_v_max = 5
default_p_brake = 0.2


def model_an(v_max_two_lane=5, v_max_conv_zone=2, v_max_obstr_zone=3, p_brake=0.2):
    points_avv_all, points_avv_conv, points_avv_obstr = [], [], []
    points_d_all, points_d_conv, points_d_obstr = [], [], []
    for t in range(73, 74):
        print('quantity of cars is {0}'.format(t))  # delete it
        steps = mymodel_vis.get_steps(1200, np.array([]), 100, v_max_two_lane, v_max_conv_zone, v_max_obstr_zone, p_brake, [[50, 52]], [[53, 73]], 1, [], t)
        # average v
        points_avv_all.append([t, mymodel_an.average_v_global(steps[1:])])
        points_avv_conv.append([t, mymodel_an.average_v_conv(steps[1:], [[50, 52]])])
        points_avv_obstr.append([t, mymodel_an.average_v_obstr(steps[1:], [[53, 73]])])
        # density
        points_d_all.append([t, mymodel_an.density_global(steps[1:])])
        points_d_conv.append([t, mymodel_an.density_conv(steps[1:], [[50, 52]])])
        points_d_obstr.append([t, mymodel_an.density_obstr(steps[1:], [[53, 73]])])
    return [points_avv_all, points_avv_conv, points_avv_obstr, points_d_all, points_d_conv, points_d_obstr]


data = model_an(5, 2, 3, 0.2)

d = open('data_73-96.txt', 'w')
d.write(str(data))
d.close()
